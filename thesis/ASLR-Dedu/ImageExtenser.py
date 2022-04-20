# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021-2022
from capstone import *
import lief
import argparse
import sys

class Image:
	def __init__(self,elfFile,libList):
		self.elfFile = elfFile
		self.libList = libList
		#Maps the libs with their functions (name)
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
	
	def correct_calls(self,disass):
		instList = disass.disasm(self.textSec.content.tobytes(),self.textSec.virtual_address)
		maxPos = self.textSec.virtual_address+self.textSec.size
		#Generate new absolute calls
		for inst in instList:
			patch = b'\x50\x48\xc7\xc0'
			#If its a hexadecimal operand
			try:
				funcInfo = self.functionPos.get(int(inst.op_str,16))
			#If it's a register
			except ValueError:
				funcInfo = None
				#TODO
			if inst.mnemonic == "call" and funcInfo is not None:
			
				relAddress = funcInfo[1]#-inst.address-5
				if relAddress != None:
					patch += relAddress.to_bytes(4,'little') + b'\xff\xd0\x58'
					self.elfFile.patch_address(inst.address,bytearray(patch))
				else:
					print("[Info] - ",hex(inst.address),funcInfo[0].name," \
						Couldn't be relocated, it's missing in the indirection table")
		
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
			if lib not in self.libList:
				#Padding
				code += b'\x90' * padding
				byteCount += padding
			else:
				for func in self.funcLibMap.get(lib):
					writeFunc = self.elfFuncDict.get(func.name)
					if writeFunc is not None:
						self.functionPos.get(writeFunc.address)[1] = libSec.virtual_address+byteCount
						relAddress = writeFunc.address-(libSec.virtual_address+byteCount)-5
						if relAddress <= 0 :
							relAddress = negative_offset(relAddress)
						code += b'\xe8'+relAddress.to_bytes(4,'little')+b'\xc3'
						
					else:
						code += b'\x90\x90\x90\x90\x90\x90'
					byteCount += 6
		print("[Info] - Created .ind segment from "+hex(libSec.virtual_address)+" : "+hex(libSec.virtual_address+byteCount)+".")
		
		if  libSec.virtual_address <  self.textSec.virtual_address and libSec.virtual_address+byteCount >= self.textSec.virtual_address:
			print("[Error] - the indirection table rewrites the text section, change the configuration file.")
			sys.exit()
		libSec.content = bytearray(code)
		libSec.flags = 0x4+0x2 #No need to write this section
	
	def map_function_with_library(self,elfFile,buildPath):
		#Work around since get_function_address doesn't seem to send back good addresses
		#Builds a dict that maps addresses to functions
		for function in elfFile.functions:
			self.elfFuncDict[function.name] = function
		
		if len(self.elfFuncDict) == 0:
			print("[Error] - No function found in the binary.")
			return
	
		for libName in self.libList:
			#Loads the object file from the lib
			lib = open(buildPath+"/"+libName+".o","rb")
			if lib == None:
				print("[Error] - Couldn't find the file "+libName+".o in the build folder.")
				continue
			self.funcLibMap[libName] = []
			objFile = lief.ELF.parse(lib)
			funcNames = objFile.functions
			
			for name in funcNames:
				funct = self.elfFuncDict.get(name.name)
				self.funcLibMap[libName].append(name)
				if funct != None:
					#None is the destination address that should be further filled.
					self.functionPos[funct.address] = [funct,None]
				else:
					print("Function "+ name +" from "+libName+" is never used in ELF")

	def print_info(self):
		for libs in self.libList:
			print(libs+" :")
			for function in self.funcLibMap[libs]:
				print("\t "+function.name +" at address "+str(hex(function.address))+ " in lib")
def negative_offset(offset):
	return (offset & (2**32-1))

def check_file(elfFile):

	if len(elfFile) > 4 and elfFile[1:4] == b'ELF':
		if elfFile[4] == 2:
			return True
		else:
			print("[ERROR] - The file should be a x86 binary file.")
	else:
			print("[ERROR] - Entered file is not an ELF file.")
	return False

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
	functDic = img.map_function_with_library(elfFile,params.build)
	img.add_indirection_table(conf)
	img.correct_calls(disass)
	#img.print_info()
	#Write back the modifications
	elfFile.write(params.path+"_modified")
	
