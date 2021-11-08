# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021

from Analyzer import Analyzer
import sys
from argparse import ArgumentParser
import random

def printSymTable(table):
	for element in table:
		print( element[0] + " | " + element[1])

def main(openFile,debug):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	
	if debug:
		printSymTable(table)
	#For now randomizes current address (. = 0x....) but doesn't swap regions
	for element in table:
		
		if(element[0] == "curAdd"):
			element[1] = '0x'+''.join('{:02X}'.format(int(element[1],16)+(8*random.randint(-500,500))))
	if debug:
		printSymTable(table)
		
	printBack(openFile,table)
	
	return 0

def printBack(openFile,table):

	#clears the file
	openFile.seek(0)
	openFile.truncate()
	
	#Writes back
	openFile.write("SECTIONS\n{\n")
	for element in table:
		if element[0] == "curAdd":
			openFile.write(". = "+element[1]+";\n")
		else:
			openFile.write("."+element[0]+":"+element[1]+"\n")
	
	openFile.write("}")
	return 0

if __name__ == '__main__':
	#Gets back the path of the linker script to modify
	parser = ArgumentParser(prog="Unikraft ASLR, linker script implementation")

	parser.add_argument('--file_path', dest='path', default='./', help="Path leading to the file.")

	parser.add_argument('--debug', dest='debug', default='False', 
		help="Prints on the standard input debug informations.")

	params , _ = parser.parse_known_args(sys.argv[1:])
	
	openFile = open(params.path,"r+")

	if(openFile == None):
		print("Couldn't open the file, path may be wrong.")
	else:
		main(openFile,params.debug)
		openFile.close()
	
	
