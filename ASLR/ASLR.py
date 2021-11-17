# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021

from Analyzer import Analyzer
from argparse import ArgumentParser
import sys
import random

def printSymTable(table):
	for element in table:
		print( element[0] + " | " + element[1]+ " | " + str(element[2]))

def main(openFile,debug):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	regionTable = []
	
	if debug == 'True':
		printSymTable(table)
	
	index = 0
	lastFixedAssign = -1;
	lastFixedAdd = -1;
	#For now randomizes current address (. = 0x....) and swap the regions (not subregions)
	#Swap the regions between the fixed addresses (can we swap with the others ?) 
	for element in table:
		if(element[0]=="assign"):
			if lastFixedAssign != -1:
				regionTable.append([lastFixedAssign,index])
				lastFixedAssign = -1
			else:
				lastFixedAssign = index
		elif(element[0] == "curAdd" and not element[1].startswith('ALIGN')):
			#Swap memory regions

			swapRegions(table,regionTable)
			#Resets the table after the swaping
			regionTable = []
			
			element[1] = '0x'+''.join('{:02X}'.format(int(element[1],16)+(8*random.randint(-500,500))))
			lastFixedAdd = index
		index += 1
	#Swap the last memory regions
	swapRegions(table,regionTable)
	
	printBack(openFile,table)
	
	return 0

def swapRegions(table,regionTable):
	iterations = len(regionTable)
	
	#if there's only one element there's no point swapping it.
	if iterations > 0:
		secRand = random.SystemRandom()
		#Copies the regions to assign
		tmpArray = table.copy()[regionTable[0][0]:regionTable[iterations-1][1]]
		
		for index in range(iterations):
			tmpRegion = secRand.choice(regionTable)
			table[tmpRegion[0]:tmpRegion[1]+1] = tmpArray[tmpRegion[0]-1:tmpRegion[1]]
			regionTable.remove(tmpRegion)

def printBack(openFile,table):

	#clears the file
	openFile.seek(0)
	openFile.truncate()
	
	#Writes back
	openFile.write("SECTIONS\n{\n")
	for element in table:
		if element[0] == "curAdd":
			openFile.write(". = "+element[1]+";\n")
		elif element[0] == "assign":
			openFile.write(element[1]+"= .;\n")
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
	
	
