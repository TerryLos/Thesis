# Written by Loslever Terry 
# University of Liege
# Contact : terry.loslever@student.uliege.be
# 2021
# foo_start = .;
# ....
# foo_end = .; is considered to be a region.
#
# .foo : { } is also a region if not between the elements defined upper.

from Analyzer import Analyzer
from argparse import ArgumentParser
import sys
import random

def printSymTable(table):
	for element in table:
		if len(element) == 3:
			print( element[0] + " | " + element[1]+ " | " + str(element[2]))
		else:
			print( element[0] + " | " + element[1])

#Takes 2 string and returns the longest prefix/suffix between them
def alike(s1,s2):
	lenS1 = len(s1)
	lenS2 = len(s2)
	
	lettersPre = 0
	lettersSuf = 0
	
	stopPre = False
	stopSuf = False
	#Prefix
	for i in range(lenS1):
		if i >= lenS2 or (stopSuf and stopPre):
			break
		if s1[lenS1-i-1] == s2[lenS2-i-1] and not stopSuf:
			lettersSuf +=1
		else:
			stopSuf = True
		
		if s1[i]==s2[i] and not stopPre:
			lettersPre +=1
		else:
			stopPre = True
	
	if lettersPre > lettersSuf :
		return lettersPre
	else :
		return lettersSuf

# Pairs naively the xxx = .; elements 
def primaryRegionHandler(table):
	regionTable = []
	index = 0
	lastFixedAssign = -1;
	#For now randomizes current address (. = 0x....) and swap the regions (not subregions)
	#And swaps the regions while keeping the other elements at the same place.
	for element in table:
		if(element[0]=="assign"):
			if lastFixedAssign != -1:
				regionTable.append([lastFixedAssign,index])
				lastFixedAssign = -1
			else:
				lastFixedAssign = index
		elif(element[0] == "curAdd" and not element[1].startswith('ALIGN')):
			element[1] = '0x'+''.join('{:02X}'.format(int(element[1],16)+(8*random.randint(-500,500))))

		index += 1
	return regionTable
	
# Tries to pair the xxx = .; elements which share the longuest prefix
#TODO ajouter un poids décroissant quand on avance loin dans le script
#Pas très concluant pour l'instant
def secondaryRegionHandler(table):
	tableLen = len(table)
	regionTable = []
	
	#For now randomizes current address (. = 0x....) and swap the regions (not subregions)
	for i in range(tableLen): 
		maxCompatIndex = 0
		maxCompat = 0
		compat = 0
		atEnd = False
		tableSize = len(regionTable)
		if table[i][0] == "assign":
			for j in range(i+1,tableLen):
				if table[j][0] != "assign":
					continue

				compat = alike(table[i][1],table[j][1]) / (j-i)
				if compat > maxCompat:
					maxCompat = compat
					maxCompatIndex = j
					
			#Checks if the elements that starts the region closes already another one
			for j in range(tableSize):
				if regionTable[tableSize-1-j][1] == i or i < regionTable[tableSize-1-j][1]:
					atEnd = True
					break
			if (tableSize == 0 or not atEnd) and i <= maxCompatIndex:
				regionTable.append([i,maxCompatIndex])
		#if not assign or curAdd -> independant section
		if table[i][0] != "assign" and table[i][0] != "curAdd" and tableSize>0 and \
			not (regionTable[tableSize-1][0]< i and i <regionTable[tableSize-1][1]):
				regionTable.append([i,i])
		
	return regionTable
def main(openFile,debug):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	regionTable = []
	
	if debug == 'True':
		printSymTable(table)
	
	regionTable1 = primaryRegionHandler(table)
	regionTable2 = secondaryRegionHandler(table)
	
	print(regionTable1)
	print(regionTable2)
	#Swap memory regions
	table = swapRegions(table,regionTable2)
	
	printBack(openFile,table)
	
	return 0

def swapRegions(table,regionTable):
	iterations = len(regionTable)
	regionCopy = regionTable.copy()
	regionTableIndex = 0
	newTable = []
	secRand = random.SystemRandom()
	index = 0
	maxInter = len(table)
	
	#if there's only one element there's no point swapping it.
	if iterations > 0:
		while index < maxInter:

			#If it's a region
			if regionTableIndex < iterations and index == regionCopy[regionTableIndex][0]:
				#Takes an element at random without replacement
				tmpRegion = secRand.choice(regionTable)
				index = regionCopy[regionTableIndex][1]
				#Append the region to the newtable
				newTable += table[tmpRegion[0]:tmpRegion[1]+1]
				regionTable.remove(tmpRegion)
				regionTableIndex += 1
			#If it's a singleton
			else:
				newTable.append(table[index])
			index += 1
		return newTable
	return table

def printBack(openFile,table):

	#clears the file and save headers
	openFile.seek(0)
	header = openFile.read().split("SECTIONS\n{\n")
	openFile.seek(0)
	openFile.truncate()
	
	#Writes back
	openFile.write(header[0]+"SECTIONS\n{\n")
	for element in table:
		if element[0] == "curAdd":
			openFile.write(". = "+element[1]+";\n")
		elif element[0] == "assign":
			if len(element) == 3:
				openFile.write(element[1]+"= ."+element[2]+";\n")
			else:
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
	
	
