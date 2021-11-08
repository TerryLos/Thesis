# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021

from Analyzer import Analyzer
import sys
from argparse import ArgumentParser

def printSymTable(table):
	for element in table:
		print( element[0] + " | " + element[1])

def main(openFile,debug):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	
	if debug:
		printSymTable(table)

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
