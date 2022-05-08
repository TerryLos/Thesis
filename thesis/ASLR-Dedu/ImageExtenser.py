# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021-2022
from capstone import *
import lief
import argparse
import sys
import subprocess
import re

pointerRex = re.compile("\[.*?\]")

class Image:
	def __init__(self,elfFile,libList):
		self.elfFile = elfFile
		self.libList = libList
		self.libInInd = {}
		#Maps the libs with their functions/symbols (name)
		self.funcLibMap = {}
		#Maps the function position to its new address and func object
		self.functionPos = {}
		#Maps a name to the function object
		self.elfFuncDict = {}
		#Only needs to disass the .text section
		
		self.textSec = self.elfFile.get_section(".text")
		if self.textSec is None :
			print("[Error] - Couldn't find the .text section")
			return None
	def _find_lib(self,addr):
		for libs in self.libList:
			if len(self.funcLibMap[libs])> 0 and addr >= self.funcLibMap[libs][0][2] \
				and addr <= self.funcLibMap[libs][-1][2]:
				
				return libs,(self.funcLibMap[libs][0][2],self.funcLibMap[libs][-1][2])
		return None , None
	
	def _handle_move(self,operand):
		after = operand.split(", ")
		translatedOp = []
		for op in after:
			tmp = str_to_hex(op)
			if tmp == None:
				split = re.search(pointerRex,op)
				inside = None
				if split:
					inside = str_to_hex(split.group(0)[1:-1])
				
				if inside:
					translatedOp.append(inside)
				else:
					translatedOp.append(op)
			else:
				translatedOp.append(tmp)
		return translatedOp
	
	def correct_calls(self,disass):
		stackInit = self.elfFile.get_static_symbol("bootstack")
		if not stackInit:
			print("[Error] - Couldn't find the bootstack symbol")
			sys.exit()
		instList = disass.disasm(self.textSec.content.tobytes(),self.textSec.virtual_address)
		maxPos = self.textSec.virtual_address+self.textSec.size
		textRange = [self.textSec.virtual_address,maxPos]
		roData = self.elfFile.get_section(".rodata")
		
		if roData is None :
			print("[Error] - Couldn't find the .bss section")
			roData = [0,0]
		else:
			roData = [roData.virtual_address,roData.virtual_address+roData.size]
		
		dataRange = self.elfFile.get_section(".data")
		if dataRange is None :
			print("[Error] - Couldn't find the .data section")
			dataRange = [0,0]
		else:
			dataRange = [dataRange.virtual_address,dataRange.virtual_address+dataRange.size]
		
		#Generate new absolute calls
		for inst in instList:
			_ , rangeLib = self._find_lib(inst.address)
			patch = b'\xc7\xc0'
	
			#Get back the same function from elf
			funcInfo = self.functionPos.get(str_to_hex(inst.op_str))
			#Checks if the operands are refering to symbols
			varInfo = self._handle_move(inst.op_str)
			
			if inst.mnemonic == "call" and funcInfo is not None:
				relAddress = funcInfo[1]
				if relAddress != None:
					patch += relAddress.to_bytes(4,'little') + b'\xff\xd0'
					self.elfFile.patch_address(inst.address,bytearray(patch))
				else:
					print("[Info] - ",hex(inst.address),funcInfo[0].name," \
						Couldn't be relocated, it's missing in the indirection table")
			
			if jump_mnemonic(inst.mnemonic) and (funcInfo is not None and rangeLib is not None ) \
				and (funcInfo[0].address < rangeLib[0] or funcInfo[0].address > rangeLib[1]):
					print("[Warn] Jump left unpatched ",hex(inst.address)," to ",funcInfo[0].name,
					"out of its own lib")
			
			if inst.mnemonic == "mov" or inst.mnemonic == "lea" or inst.mnemonic == "mov":
				tmp  , _ =self._find_lib(inst.address)

				for var in varInfo:
					if type(var) is int and (var in range(roData[0],roData[1]) \
						or var in range(dataRange[0],dataRange[1]) or var in range(textRange[0],textRange[1])): 
						#Patches the address by a jump
						self._patch_memory_access(inst,varInfo,stackInit)
	
	def _patch_memory_access(self,inst,varInfo,stackInit):
	
		movSize = len(inst.bytes)
		#checks its lib
		lib , _ = self._find_lib(inst.address)
		#Gets its indirection table
		ind = self.libInInd.get(lib)
		if movSize <= 5:
			return
		
		if ind and (varInfo[0] != stackInit.value and varInfo[1] != stackInit.value):
			#Adds it in the .ind table at its lib offset
			#Jumps towards the table
			fill = b'\x68'+ind[1].to_bytes(4,'little')+b'\xc3'
			if movSize > 6:
				fill += b'\x90'*(movSize-6)
			self.elfFile.patch_address(inst.address,bytearray(fill))
			#Fills the table with the instruction and jumps back
			tableCode = inst.bytes
			#+1 because of the return instruction c3
			tableCode += b'\xe9'+compute_offset(inst.address-(ind[1]+movSize-1)).to_bytes(4,'little')
			self.elfFile.patch_address(ind[1],bytearray(tableCode))
			ind[1] += movSize + 5
			
		else :
			print("[Error] - Couldn't patch mov/lea at address",inst.address," no lib found.")
	def add_indirection_table(self,conf):
		addr = conf.pop(0)
		padding = int(addr[1],16)
		libSec = self.elfFile.get_section(".ind")
		if libSec is None:
			print("[Error] - indirection table not created by the linker script.")
			sys.exit()
		
		
		libSec.type = self.textSec.type #same type as .text section
		byteCount = 0
		code =  b''
		for lib in conf:
			#Regsiter the lib indirection's table position
			#.ind.lib start address
			self.libInInd[lib] = [int(addr[0],16)+byteCount,0,int(addr[0],16)+byteCount+padding]
			
			if lib not in self.libList:
				#Padding
				code += b'\x90' * padding
				byteCount += padding
			else:
				#Adds indirection for functions
				for func in self.funcLibMap.get(lib):
					writeFunc = self.elfFuncDict.get(func[0])
					if writeFunc is not None:
						self.functionPos.get(writeFunc.address)[1] = libSec.virtual_address+byteCount
						relAddress = writeFunc.address-(libSec.virtual_address+byteCount)-5
						relAddress = compute_offset(relAddress)
						code += b'\xe9'+relAddress.to_bytes(4,'little') #relative jump to the function
						
					else:
						code += b'\x90\x90\x90\x90\x90'
					byteCount += 5
					
			self.libInInd[lib][1] = int(addr[0],16)+byteCount
			#.ind.lib last instruction address
			code += b'\x90'*(self.libInInd[lib][2] - (int(addr[0],16)+byteCount))
			byteCount += self.libInInd[lib][2] - (int(addr[0],16)+byteCount)
			
		print("[Info] - Created .ind segment from "+hex(libSec.virtual_address)+" : "+hex(libSec.virtual_address+byteCount)+".")
		
		if  libSec.virtual_address <  self.textSec.virtual_address and libSec.virtual_address+byteCount >= self.textSec.virtual_address:
			print("[Error] - the indirection table rewrites the text section, change the configuration file.")
			sys.exit()
		libSec.content = bytearray(code)
		libSec.flags = 0x4+0x2 #No need to write this section
	
	def map_symbols_with_library(self,buildPath):
		#Work around since get_function_address doesn't seem to send back good addresses
		#Builds a dict that maps addresses to functions
		for function in self.elfFile.functions:
			self.elfFuncDict[function.name] = function
	
		if len(self.elfFuncDict) == 0 :
			print("[Error] - No function found in the binary.")
			sys.exit()
		
		for libName in self.libList:
			#Loads the object file from the lib
			lib = open(buildPath+"/"+libName+".o","rb")
			if lib == None:
				print("[Error] - Couldn't find the file "+libName+".o in the build folder.")
				continue
				
			self.funcLibMap[libName] = []
			
			objFile = lief.ELF.parse(lib)
			
			funcNames = objFile.functions
			
			#Maps the function from the ELF with its library and its current address
			#If the element is not present in the ELF, we'll pad it later
			for name in funcNames:
				funct = self.elfFuncDict.get(name.name)
				if funct is not None:
					self.funcLibMap[libName].append((name.name,name.address,funct.value))
					#None is the destination address that should be further filled.
					self.functionPos[funct.address] = [funct,None]
				else:
					self.funcLibMap[libName].append((name.name,name.address,None))
					print("Function "+ name.name +" from "+libName+" is never used in ELF")

	def print_info(self):
		for libs in self.libList:
			print(libs+" :")
			for function in self.funcLibMap[libs]:
				print("\t "+" fct :"+function[0] +" at address "+str(hex(function[1]))+ " in lib "+\
					str(hex(function[2]))+ " in elf.")

def jump_mnemonic(mnemo):
	if mnemo == "jmp" or mnemo == "je" or mnemo == "jne" or mnemo == "jg" or mnemo == "jge" or mnemo == "ja" \
		or mnemo == "jae" or mnemo == "jl" or mnemo == "jle" or mnemo == "jb" or mnemo == "jo" \
		or mnemo == "jno" or mnemo == "jz" or mnemo == "jns" or mnemo == "jjcxz" or mnemo == "jecxz" \
		or mnemo == "jrcxz":
		return True
	return False
def symbol_types(symType):
	if lief.ELF.SYMBOL_TYPES(0) == symType or lief.ELF.SYMBOL_TYPES(5) == symType or \
		lief.ELF.SYMBOL_TYPES(1) == symType or lief.ELF.SYMBOL_TYPES(6) == symType:
		return True
	return False
	
def compute_offset(offset):
	if offset <= 0 :
		return (offset & (2**32-1))
	else:
		return offset

def get_assembly(name,operands):
	fileS = open("tmp_assembly.S",'w')
	if fileS is None:
		print("[Error] couldn't generate patched assembly")
		sys.exit()
	
	fileS.write(".intel_syntax noprefix\n"+name+" "+operands[0]+","+operands[1]+"\n")
	fileS.close()
	
	subprocess.call("as  --64 -o tmp_assembly tmp_assembly.S ",shell=True, \
		stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
	
	sec = lief.ELF.parse("tmp_assembly")
	if sec is None :
		return None
	content = sec.get_section(".text").content
	return content.tobytes()

def check_file(elfFile):

	if len(elfFile) > 4 and elfFile[1:4] == b'ELF':
		if elfFile[4] == 2:
			return True
		else:
			print("[ERROR] - The file should be a x86 binary file.")
	else:
			print("[ERROR] - Entered file is not an ELF file.")
	return False

def str_to_hex(op):
	try:
		#It's an address
		tmp = int(op,16)
	except ValueError:
		#it's a register
		tmp = None
	
	return tmp
def extract_libs(string):
	"""
	In : string
	"""
	wordList = []
	returnList = []
	if string != None:
		wordList = string.split()
		
	for libs in wordList:
		if not libs.startswith("lib"):
			continue
		else:
			if(type(libs) is list):
				print("[ERROR] - The aslr-dediplication file is not in a proper format.")
				sys.exit()
			returnList.append(libs)
		
	return returnList
def extract_conf(openConf):
	'''
	In : openConf is the config file.
	Returns a dictionnary that maps the name of the lib with an address.
	Skips comments : #This is a comment
	'''
	content = openConf.readlines()
	conf = []
	for line in content:
		if not line.startswith("#"):
			words = line.split()
			if len(words) > 1 :
				conf.append([words[0],words[1].rstrip("\n")])
				continue
			conf.append(line.rstrip("\n"))
	
	if type(conf[0]) is not list :
		print("[Error] - the config file doesn't respect the format.")
		sys.exit()
	return conf

if __name__ == '__main__':
	#Gets back the path of the linker script to modify
	parser = argparse.ArgumentParser(prog="Unikraft ASLR, binary rewriter")

	parser.add_argument('--file_path', dest='path', default='./', help="Path leading to the ELF file.")
	
	parser.add_argument('--build_path', dest='build', default='./', help="Path leading to the build folder.")
	
	parser.add_argument('--conf_file', dest='conf', default='./', help="Path leading to the configuration file.")

	parser.add_argument('--obj_file', dest='obj', default='./', help="List of object files.")	
	
	
	params , _ = parser.parse_known_args(sys.argv[1:])
	confFile = open(params.conf,"r")
	if confFile is None:
		print("[Error] - coudln't open the configuration file.")
		sys.exit()
	
	conf = extract_conf(confFile)
	confFile.close()

	elfFile = lief.ELF.parse(params.path)
	
	disass = Cs(CS_ARCH_X86,CS_MODE_64)
	disass.skipdata = True
	
	img = Image(elfFile,extract_libs(params.obj))
	functDic = img.map_symbols_with_library(params.build)
	img.add_indirection_table(conf)
	img.correct_calls(disass)
	img.print_info()
	#Write back the modifications
	elfFile.write(params.path+"_modified")
	
