# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021

import re

class Analyzer:
	
	def __init__(self,openFile):
		self.file = openFile;
		self.keywords = ["ENTRY","SECTIONS"]
		self.symbolTable = [];
		self.buffer = '';
		self.braceCounter = 0
		self.parCounter = 0
		
	def __handlesLine(self,string):
		for letter in string:
			match letter:
				case '{':
					self.braceCounter += 1
				case '(':
					self.parCounter += 1
				case '}':
					self.braceCounter -= 1
					#Flushes the section in the table
					if(self.braceCounter == 0):
						self.buffer += letter
						secSplit = re.split("\.(.*)=", self.buffer)[1:]
						self.symbolTable.append([secSplit[0],secSplit[1]])
						self.buffer = ''
				case ')':
					self.parCounter += 1
			self.buffer += letter
			
	def analyze(self):
		
		for lines in self.file:
			self.__handlesLine(lines)
		
		return self.symbolTable.copy()
