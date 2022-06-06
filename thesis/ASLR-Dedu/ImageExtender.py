#!/usr/bin/env python3
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
from utils import check_file,str_to_hex,extract_libs,extract_conf

pointerRex = re.compile("\[.*?\]")
DEBUG = False
class Image:
	def __init__(self,elfFile,config):
		self.elfFile = elfFile
		self.config = config
		#Deletes the first line which is not used in this script
		self.config.pop(0)
		
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
		self.libSec = self.elfFile.get_section(".ind")
		if self.libSec is None:
			print("[Error] - indirection table not created by the linker script.")
			sys.exit()
		self.baseAddr = self.libSec.virtual_address
	
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
		currentFunction = None
		currentSize = 0
		currentLib = None
		
		
		instList = disass.disasm(self.textSec.content.tobytes(),self.textSec.virtual_address)
		
		maxPos = self.textSec.virtual_address+self.textSec.size
		textRange = [self.textSec.virtual_address,maxPos]
		roData = self.elfFile.get_section(".rodata")

		if roData is None :
			print("[Error] - Couldn't find the .rodata section")
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
			#Changes the parent function of the instruction
			if self.functionPos.get(inst.address):
				currentFunction = self.functionPos.get(inst.address)[0]
				currentSize = currentFunction.size
				#Gets the current lib based on the function
				currentLib = self.functionPos.get(inst.address)[2]

			#if lib and function not in the config file
			elif currentFunction and currentFunction.value + currentSize < inst.address:
				currentFunction = currentLib = None
				currentFunctionSize = 0
			
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
				elif DEBUG:
					print("[Info] - ",hex(inst.address),funcInfo[0].name," \
						Couldn't be relocated, it's missing in the indirection table")
			
			elif jump_mnemonic(inst.mnemonic) and DEBUG and (funcInfo is not None and currentFunction is not None) \
				and funcInfo[0] == currentFunction:
					print("[Warn] Jump left unpatched ",hex(inst.address)," to ",funcInfo[0].name,
					"out of its own function")
			#Patches instructions that does direct addressing in their operands
			elif varInfo and (inst.mnemonic=="mov" or inst.mnemonic=="movh" or inst.mnemonic=="lea"):
				for var in varInfo:
					if type(var) is int and (var in range(roData[0],roData[1]) \
						or var in range(dataRange[0],dataRange[1]) or var in range(textRange[0],textRange[1])): 
						#Patches the address by a jump
						self._patch_memory_access(inst,currentLib,varInfo)
		#check sizes
		for lib in self.config:
			ind = self.libInInd.get(lib[0])
			if ind and ind[1] > ind[2]:
				print("[ERROR] - couldn't pach the instruction, missing space for "+lib[0]+\
					" at least "+ str(ind[1]-ind[2])+" bytes.")
			
	
	def _patch_memory_access(self,inst,currentLib,varInfo):
	
		movSize = len(inst.bytes)
		if movSize <= 5:
			return
		#Gets its indirection table
		ind = self.libInInd.get(currentLib)
		
		if ind :
			#Adds it in the .ind table at its lib offset
			#Jumps towards the table
			fill = b'\x68'+ind[1].to_bytes(4,'little')+b'\xc3'
			
			if movSize > 6:
				fill += b'\x90'*(movSize-6)
			
			#Doesn't write after the table but keepts counting to
			if ind[1] < ind[2]:
				self.elfFile.patch_address(inst.address,bytearray(fill))
				#Fills the table with the instruction and jumps back
				tableCode = inst.bytes
				#+1 because of the return instruction c3
				tableCode += b'\xe9'+compute_offset(inst.address-(ind[1]+movSize-1)).to_bytes(4,'little')
				self.elfFile.patch_address(ind[1],bytearray(tableCode))
			ind[1] += movSize + 5
		
		elif DEBUG :
			print("[WARN] - Couldn't patch mov/lea at address",inst.address," no lib found.")
	def add_indirection_table(self):
		
		self.libSec.type = self.textSec.type #same type as .text section
		byteCount = 0
		code =  b''
		for lib in self.config:
			padding = int(lib[1],16)
			#Regsiter the lib indirection's table position
			#.ind.lib start address
			self.libInInd[lib[0]] = [self.baseAddr+byteCount,0,self.baseAddr+byteCount+padding]
			if self.funcLibMap[lib[0]] is None:
				#Padding
				code += b'\x90' * padding
				byteCount += padding
			else:
				#Adds indirection for functions
				for func in (self.funcLibMap.get(lib[0])):
					writeFunc = self.elfFuncDict.get(func[0])
					if writeFunc is not None:
						self.functionPos.get(writeFunc.value)[1] = self.libSec.virtual_address+byteCount
						relAddress = writeFunc.value-(self.libSec.virtual_address+byteCount)-5
						relAddress = compute_offset(relAddress)
						code += b'\xe9'+relAddress.to_bytes(4,'little') #relative jump to the function
					else:
						code += b'\x90\x90\x90\x90\x90'
					byteCount += 5
					
			self.libInInd[lib[0]][1] = self.baseAddr+byteCount
			#.ind.lib last instruction address
			code += b'\x90'*(self.libInInd[lib[0]][2] - (self.baseAddr+byteCount))
			byteCount += (self.libInInd[lib[0]][2] - (self.baseAddr+byteCount))
			if self.libInInd[lib[0]][1] > self.libInInd[lib[0]][2]:
				print("[Error] - The space reserved for lib "+lib[0]+" is too small, add at least",\
					(self.libInInd[lib[0]][1]-self.libInInd[lib[0]][2]),"bytes.")
				sys.exit()
		
		print("[Info] - Created .ind segment from "+hex(self.libSec.virtual_address)\
			+" : "+hex(self.libSec.virtual_address+byteCount)+".")
			
		if self.libSec.virtual_address <  self.textSec.virtual_address and \
			self.libSec.virtual_address+byteCount >= self.textSec.virtual_address:
			print("[Error] - the indirection table rewrites the text section, change the configuration file.")
			sys.exit()
		
		self.libSec.content = bytearray(code)
		self.libSec.flags = self.textSec.flags
	
	def map_symbols_with_library(self,buildPath):
		#Work around since get_function_address doesn't seem to send back good addresses
		#Builds a dict that maps addresses to functions
		for function in get_function(self.elfFile):
			self.elfFuncDict[function.name] = function
	
		if len(self.elfFuncDict) == 0 :
			print("[Error] - No function found in the binary.")
			sys.exit()
		
		for library in self.config:
			libInElf = False
			#Loads the object file from the lib
			try:
				lib = open(buildPath+"/"+library[0]+".o","rb")
			except FileNotFoundError:
				self.funcLibMap[library[0]] = None
				continue
			
			self.funcLibMap[library[0]] = []
			
			objFile = lief.ELF.parse(buildPath+"/"+library[0]+".o")
			
			#funcNames = objFile.functions
			funcNames = get_function(objFile)

			#Maps the function from the ELF with its library and its current address
			#If the element is not present in the ELF, we'll pad it later
			for name in funcNames:
				funct = self.elfFuncDict.get(name.name)
				if funct is not None:
					self.funcLibMap[library[0]].append((name.name,name.value,funct.value))
					#None is the destination address that should be further filled.
					self.functionPos[funct.value] = [funct,None,library[0]]
					libInElf = True
				else:
					#Consider functions that are not included in the elf so that absolute addresses
					#matches
					self.funcLibMap[library[0]].append((name.name,name.value,None))
			
			#No function was found in the binary, pad this lib
			if libInElf == False:
				self.funcLibMap[library[0]] = None

	def print_info(self):
		for libs in self.config:
			print(libs[0]+" :")
			if self.funcLibMap.get(libs[0]):
				for function in self.funcLibMap.get(libs[0]):
					if function[2]:
						print("\t "+" fct :"+function[0] +" at address "+str(hex(function[1])) \
						+ " in lib "+str(hex(function[2]))+ " in elf.")
					else:
						print("\t "+" fct :"+function[0] +" at address "+str(hex(function[1])) \
							+ " in lib not in elf.")
			else:
				print("\t Filled with padding.")
	def get_lib_limits(self,functionList):
		start = float('inf')
		end = 0
		lastName = None
		index = 0
		endIndex = len(functionList)
		
		for index in range(endIndex):
			if functionList[index][2] and start > functionList[index][2] :
				start = functionList[index][2]
			if functionList[index][2] and end < functionList[index][2] :
				lastName = functionList[index][0]
				end = functionList[index][2]
		#The end of the lib is the last byte of the last function
		end += (self.elfFuncDict[lastName].size-1)
	
		return (start,end)

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
def get_function(binaryFile):
	"""
		This is a work around made because the property .functions doesn't always
		work in lief for some reason
	"""
	sym = binaryFile.symbols
	retList = []
	for symbol in sym:
		if symbol.is_function:
			retList.append(symbol)
	return retList
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
if __name__ == '__main__':
	#Gets back the path of the linker script to modify
	parser = argparse.ArgumentParser(prog="Unikraft ASLR, binary rewriter")

	parser.add_argument('--file_path', dest='path', default='./', help="Path leading to the ELF file.")
	
	parser.add_argument('--build_path', dest='build', default='./', help="Path leading to the build folder.")
	
	parser.add_argument('--conf_file', dest='conf', default='./', help="Path leading to the configuration file.")
	
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
	
	img = Image(elfFile,conf)
	functDic = img.map_symbols_with_library(params.build)
	img.add_indirection_table()
	img.correct_calls(disass)
	#img.print_info()
	#Write back the modifications
	elfFile.write(params.path+"_deduplication")
	
