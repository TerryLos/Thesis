import matplotlib.pyplot as plt
import argparse
import sys
import math
from random import SystemRandom

def load(openFile):
	toRet = []
	for line in openFile.readlines():
		comp = line.split()
		if len(comp) == 3:
			tmp = []
			for val in comp:
				tmp.append(int(val,16))
			toRet.append(tmp)
		else:
			print(tmp)
			print("[Entropy] {Error} One of the given file doesn't respect the proper format.")
			sys.exit()
	if len(toRet) == 1:
		return toRet[0]
	
	return toRet
def xorAndCount(val1,val2):
	count = 0
	xor = str(bin(val1^val2))
	for bit in xor:
		if bit == '1':
			count +=1

	return count
def avgBitModified(modified,source):
	textSec = 0
	stackSec = 0
	globalVar = 0

	for el in modified:
		textSec += xorAndCount(el[0],source[0])
		stackSec +=  xorAndCount(el[1],source[1])
		globalVar +=  xorAndCount(el[2],source[2])
	modLen = len(modified)
	textSec = abs(round(textSec / modLen))
	stackSec =  abs(round(stackSec / modLen))
	globalVar =  abs(round(globalVar / modLen))
	
	return [textSec,stackSec,globalVar]

def varModified(data):
	text = [0,0]
	Stack =  [0,0]
	globalVar = [0,0]
	for el in data:
		text[0] += el[0]
		Stack[0] += el[1]
		globalVar[0] += el[2]
	
	modLen = len(data)
	text[0] /= modLen
	Stack[0] /= modLen
	globalVar[0] /= modLen
	
	for el in data:
		text[1] = (el[0] - text[0])**2
		Stack[1] = (el[1] - Stack[0])**2
		globalVar[1] = (el[2] - globalVar[0])**2
	
	return (text[1],Stack[1],globalVar[1])
def computeEntropy(array,index):
	dictAddr = {}
	total = 0
	entropy = 0
	for el in array:
		if dictAddr.get(el[index]) is None:
			dictAddr[el[index]] = 1
		else:
			dictAddr[el[index]] = dictAddr[el[index]] + 1
		total += 1
	
	for addr in dictAddr:
		proba = (dictAddr[addr]/total)
		entropy += proba*math.log(1/proba,2)
	
	return entropy
def drawEntropy(addrArray,Range,index):
	x = []
	y = []
	for element in addrArray:
		addrBin = format(element[index],"032b")
		x.append(int(addrBin[31-Range[0][1]:31-Range[0][0]],2))
		y.append(int(addrBin[31-Range[1][1]:31-Range[1][0]],2))
	
	plt.figure(num=None, figsize=(5.5, 4), dpi=80, facecolor='w', edgecolor='k')
	ax = plt.subplot(111)
	ax.scatter(x,y,c='b', label='Byte 0', edgecolor='none', s=5)
	
	if index == 0:
		plt.title("Text Section Entropy")
	if index == 1:
		plt.title("Stack Entropy")
	if index == 2:
		plt.title("Data Section Entropy")
	plt.xticks((0,0x40,0x7F,0xBF,0xFF))
	plt.xlabel("Lower bits")
	plt.yticks((0,0x40,0x7F,0xBF,0xFF))
	plt.ylabel("Higher bits")
	plt.show()
def verifyUnif(limit):
	sysRand = SystemRandom()
	valDict = {}
	i = 0
	while i<limit:
		val = sysRand.randint(0,limit)
		if valDict.get(val):
			valDict[val] += 1
		else:
			valDict[val] = 1
		i+=1
	plt.hist(valDict)
	plt.title("Uniformity test of the library on N="+str(limit))
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.show()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(prog="Entropy plotter.")
	
	parser.add_argument('--ASLR_file', dest='ASLR', default='./', help="Path leading to the ASLR data file.")
	
	parser.add_argument('--NOASLR_file', dest='NOASLR', default='./', help="Path leading to the source data file.")
	
	params , _ = parser.parse_known_args(sys.argv[1:])
	
	ASLRFile = open(params.ASLR,"r")
	NoASLRFile = open(params.NOASLR,"r")
	if ASLRFile is None:
		print("[Entropy] {Error} Couldn't open the ASLR data file, path may be wrong.")
		sys.exit()
	elif NoASLRFile is None:
		print("[Entropy] {Error} Couldn't open the source data file, path may be wrong.")
		sys.exit()
	
	ASLRData = load(ASLRFile)
	print("The file is "+str(len(ASLRData))+" lines long.")
	NoASLRData = load(NoASLRFile)
	#verifyUnif(100000)
	drawEntropy(ASLRData,[[3,11],[12,20]],0)
	print("Entropy is ",computeEntropy(ASLRData,0),computeEntropy(ASLRData,1),computeEntropy(ASLRData,2),\
		" Max theo entropy is ",math.log(len(ASLRData),2))
	print(avgBitModified(ASLRData,NoASLRData))
	print(varModified(ASLRData))
