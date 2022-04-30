# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021-2022

import re

class Analyzer:
	
	def __init__(self,openFile):
		self.file = openFile;
		self.keywords = re.compile("SECTIONS")
		self.symbolTable = [];
		self.buffer = '';
		self.braceCounter = 0
		self.address = re.compile("\.\s*=\s*(.*)\s*;")
		self.assign = re.compile("(.*)=\s*\.(.*);")
		self.region = re.compile("\.\s*(.*)\s*:\s*")
		self.skippedBraces = 0
	
	def __handles_line(self,string):
		"""
		In : a string which contains a line of a linker script, tokenize the line in a set of elements. 
		Adds the tokens into the symbol tables.
		"""
		#If that's header elements we skip it
		strLen = len(string)
		string = re.sub(self.keywords,'',string)
		if(len(string) != strLen):
			self.skippedBraces += 1
		
		#Proceed with analysis
		for letter in string:
			self.buffer += letter
			#Checks for current address assignement for outside pointers
			#They are usually around memoryblocks
			secSplit = re.split(self.assign, self.buffer)[1:]
			if len(secSplit) > 0 and self.braceCounter==0:
				if(secSplit[1] != ''):
					self.symbolTable.append(["assign",secSplit[0],secSplit[1]])
				else:
					self.symbolTable.append(["assign",secSplit[0]])
				self.buffer = ''
			
			#Checks for fixed addresses
			secSplit = re.split(self.address, self.buffer)[1:]
			if len(secSplit) > 0 and self.braceCounter==0:
				self.symbolTable.append(["curAdd",secSplit[0]])
				self.buffer = ''
			
			if letter == '{':
				if(self.skippedBraces == 0):
					self.braceCounter += 1
				elif len(self.buffer)  == 1:
					letter = ''
			elif letter == '}':
				self.braceCounter -= 1
				#Means that we skipped an opening brace before
				if(self.braceCounter < 0):
					self.skippedBraces -= 1
					self.braceCounter += 1
				#Flushes the section in the table
				if( self.braceCounter == 0):
					secSplit = re.split(self.region, self.buffer)[1:]

					if len(secSplit) > 0:
						self.symbolTable.append([secSplit[0],secSplit[1]])
						self.buffer = ''
			#Wildcard
			else:
				continue
	def analyze(self):
		"""
		Feeds the lines of the file to the line handler.
		Once the file is parsed, return the symbol table.
		"""
		lines = self.file.readlines()
		for line in lines:
			self.__handles_line(line)
		
		return self.symbolTable.copy()
