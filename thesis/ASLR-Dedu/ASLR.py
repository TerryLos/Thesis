#!/usr/bin/env python3.10
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
import sys
from random import SystemRandom
import argparse

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
# Tries to pair the xxx = .; elements which share the longuest prefix
def regionHandler(table,sysRand,libList,debug):
	tableLen = len(table)
	regionTable = []
	textRegion = None
	#For now randomizes current address (. = 0x....) and swap the regions (not subregions)
	for i in range(tableLen): 
		maxCompatIndex = 0
		maxCompat = 0
		compat = 0
		atEnd = False
		tableSize = len(regionTable)
		if table[i][0] == "assign":
			for j in range(i+1,tableLen):
			
				#Qemu expects text to be the first region
				#and bss the last one, so we don't swap them
				#Breaks a second time not to take the ending pointer 
				#for another region
				if table[j][0] == "bss " or table[j-2][0] == "bss ":
					break
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
				#Modifies the lib position
				if table[i][1] == ' _text ' :
					table[i+1] = libraryRegion(table[i+1],sysRand,libList,debug)
				
				#Tries to drag pre-configured memory layout with it
				if i-1 >= 0 and table[i-1][0] == "curAdd" and table[i-1][1].startswith('ALIGN'):
					regionTable.append([i-1,maxCompatIndex])
				else:
					regionTable.append([i,maxCompatIndex])
		
		#Randomizes static addresses
		elif(table[i][0] == "curAdd" and not table[i][1].startswith('ALIGN')):
			#doesn't modify 0x100000 to respect qemu assumptions
			if int(table[i][1],16) != int("0x100000",16): 
				table[i][1] = '0x'+''.join('{:02X}'.format(int(table[i][1],16)+(8*sysRand.randint(-500,500))))
	
	return regionTable, table

def libraryRegion(textRegion,sysRand,libList,debug):
	#Allows to see memory modifications in readelf
	#Left temporary to readers to test the program
	if debug == 'True':
		index = textRegion[1].find("*(.text)")
		padding = '. = . + 0x'+''.join('{:02X}'.format(sysRand.randint(0,1000)))+";\n"
		modfiedRegion = textRegion[1][0:index] + padding +"}"
		nextLib = libList.pop(0)
		modfiedRegion += "  .text."+nextLib+" . :{ "+nextLib+".o (.text);}\n"
		while len(libList) != 0:
			padding = '. = . + 0x'+''.join('{:02X}'.format(sysRand.randint(0,1000)))+";\n"
			nextLib = sysRand.choice(libList)
			libList.remove(nextLib)
			modfiedRegion += "  .text."+nextLib+" . :{ "
			if sysRand.randint(0,4) == 1:
				modfiedRegion += padding+"  "
			modfiedRegion += nextLib+".o (.text);}\n"
		
		textRegion[1] = modfiedRegion
		return textRegion
	else:
		index = textRegion[1].find("*(.text)")
		padding = '. = . + 0x'+''.join('{:02X}'.format(sysRand.randint(0,1000)))+";\n"
		modfiedRegion = textRegion[1][0:index] + padding
		while len(libList) != 0:
			padding = '. = . + 0x'+''.join('{:02X}'.format(sysRand.randint(0,1000)))+";\n"
			nextLib = sysRand.choice(libList)
			libList.remove(nextLib)
			modfiedRegion += "  "
			if sysRand.randint(0,4) == 1:
				modfiedRegion += padding
			modfiedRegion += nextLib+".o (.text);\n"
		
		textRegion[1] = modfiedRegion+textRegion[1][index-2:]
		return textRegion

def main(openFile,debug,libList):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	regionTable = []
	sysRand = SystemRandom()
	if debug == 'True':
		printSymTable(table)
	
	regionTable, table = regionHandler(table,sysRand,libList,debug)
	#Swap memory regions
	table = swapRegions(table,regionTable,sysRand)
	if table == None:
		return -1
	
	printBack(openFile,table,debug)
	
	return 0

def swapRegions(table,regionTable,sysRand):
	regionCopy = regionTable.copy()
	iterations = len(regionCopy)
	regionTableIndex = 0
	maxInter = len(table)
	newTable = []
	index = 0
	#Set text,uk_*tab as first regions in order to avoid errors.
	toDel = []
	added = False
	setRoData = False

	for ind in regionCopy :
		if table[ind[1]][1] == " uk_inittab_end " or \
		table[ind[1]][1] == " _etext " or \
		table[ind[1]][1] == " uk_ctortab_end ":
			toDel.append(ind)
	
	if len(toDel) == 0:
		print("[ASLR] {Error} Missing important memory regions : _text, uk_inittab_start, uk_ctortab_start",file=sys.stderr)
		return None
	
	#if there's only one element there's no point swapping it.
	if iterations > 0:
		while index < maxInter:
		
			if len(toDel) != 0 and index == toDel[0][0] and added:
				index = toDel[0][1]
				toDel.pop(0)
			elif regionTableIndex < iterations and index == regionTable[regionTableIndex][0]:
				#Set text,uk_*tab as first regions in order toclear avoid errors.
				if regionTableIndex == 0 and added != True:
					for el in toDel:
						newTable += table[el[0]:el[1]+1]
						regionCopy.remove(el)
						regionTable.remove(el)
						added = True
						iterations -= 1
					continue
				else:
					#Takes an element at random without replacement
					tmpRegion = None
					while tmpRegion == None or (table[tmpRegion[1]][1] == ' _edata ' and not setRoData):
						tmpRegion = sysRand.choice(regionCopy)

					if table[tmpRegion[1]][1] == " _erodata ":
						setRoData = True
					#Makes the right jump in the table
					index = regionTable[regionTableIndex][1]
					#Append the region to the newtable
					newTable += table[tmpRegion[0]:tmpRegion[1]+1]
					regionCopy.remove(tmpRegion)
					regionTableIndex += 1
			#If it's a singleton
			else :
				newTable.append(table[index])

			index += 1
		return newTable
	return table

def printBack(openFile,table,debug):

	#clears the file and save headers
	openFile.seek(0)
	header = openFile.read().split("SECTIONS\n{\n")
	openFile.seek(0)
	openFile.truncate()
	
	#Writes back
	previous = ""
	if debug:
		#Doesn't set ENTRY in debug mode otherwise causes double import
		openFile.write("SECTIONS\n{\n")
	else :
		openFile.write(header[0]+"SECTIONS\n{\n")
	
	for element in table:
		if element[0] == "curAdd":
			#Avoid having ALIGN cascade
			if not (previous.startswith('ALIGN') and element[1].startswith('ALIGN')):
				openFile.write(". = "+element[1]+";\n")
		elif element[0] == "assign":
			if len(element) == 3:
				openFile.write(element[1]+"= ."+element[2]+";\n")
			else:
				openFile.write(element[1]+"= .;\n")
		else:
			openFile.write("."+element[0]+":"+element[1]+"\n")
		previous = element[1]
	openFile.write("}")
	return 0
def extractLibs(string):
	wordList = []
	if string != None:
		wordList = string.split()
		
	return wordList
	
if __name__ == '__main__':
	#Gets back the path of the linker script to modify
	parser = argparse.ArgumentParser(prog="Unikraft ASLR, linker script implementation")

	parser.add_argument('--file_path', dest='path', default='./', help="Path leading to the file.")

	parser.add_argument('--build_dir', dest='build', default='./', help="Path leading to the build file.")	
	
	parser.add_argument('--debug', dest='debug', default='False', 
		help="Prints on the standard input debug informations.")

	params , _ = parser.parse_known_args(sys.argv[1:])
	
	openFile = open(params.path,"r+")
	if(openFile == None):
		print("Couldn't open the file, path may be wrong.")
	else:
		libList = extractLibs(params.build)
		if len(libList) == 0:
			print("[ASLR] {Error} No lib list given to the program abort.",file=sys.stderr)
		
		main(openFile,params.debug,libList)
		openFile.close()
	
	
