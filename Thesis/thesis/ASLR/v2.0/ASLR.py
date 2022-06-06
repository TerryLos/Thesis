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
import random
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
			#Qemu and linker don't like having addresses under it
			if int(element[1],16) <= int("0x100000",16): 
				element[1] = '0x'+''.join('{:02X}'.format(int(element[1],16)+(8*random.randint(0,1000))))
			else:
				element[1] = '0x'+''.join('{:02X}'.format(int(element[1],16)+(8*random.randint(-500,500))))

		index += 1
	return regionTable
	
# Tries to pair the xxx = .; elements which share the longuest prefix
def secondaryRegionHandler(table):
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
					textRegion = j
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
				#Tries to drag pre-configured memory layout with it
				if i-1 >= 0 and table[i-1][0] == "curAdd" and table[i-1][1].startswith('ALIGN'):
					regionTable.append([i-1,maxCompatIndex])
				else:
					regionTable.append([i,maxCompatIndex])
		
		#Randomizes static addresses
		elif(table[i][0] == "curAdd" and not table[i][1].startswith('ALIGN')):
			#doesn't modify 0x100000 to respect qemu assumptions
			if int(table[i][1],16) != int("0x100000",16): 
				table[i][1] = '0x'+''.join('{:02X}'.format(int(table[i][1],16)+(8*random.randint(-500,500))))

		#if not assign or curAdd -> independant section
		""""
		Causes error with the linker and colliding memory
		if table[i][0] != "assign" and table[i][0] != "curAdd" and tableSize>0 and \
			not (regionTable[tableSize-1][0]< i and i <regionTable[tableSize-1][1]):
				regionTable.append([i,i])
		"""
		
	return regionTable,textRegion
def main(openFile,debug):
	
	analyzer = Analyzer(openFile)
	table = analyzer.analyze()
	regionTable = []
	
	if debug == 'True':
		printSymTable(table)
	
	#regionTable1 = primaryRegionHandler(table)
	regionTable, textRegion = secondaryRegionHandler(table)
	
	#Swap memory regions
	table = swapRegions(table,regionTable)
	
	printBack(openFile,table)
	
	return 0

def swapRegions(table,regionTable):
	regionCopy = regionTable.copy()
	iterations = len(regionCopy)
	regionTableIndex = 0
	maxInter = len(table)
	newTable = []
	secRand = random.SystemRandom()
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
						tmpRegion = secRand.choice(regionCopy)

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

def printBack(openFile,table):

	#clears the file and save headers
	openFile.seek(0)
	header = openFile.read().split("SECTIONS\n{\n")
	openFile.seek(0)
	openFile.truncate()
	
	#Writes back
	previous = ""
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

if __name__ == '__main__':
	#Gets back the path of the linker script to modify
	parser = argparse.ArgumentParser(prog="Unikraft ASLR, linker script implementation")

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
	
	
