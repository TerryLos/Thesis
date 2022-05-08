import matplotlib.pyplot as plt
import argparse
import sys

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
			print("[Entropy] {Error} One of the given file doesn't respect the proper format.")
			sys.exit()
	if len(toRet) == 1:
		return toRet[0]
	
	return toRet

def avgBitModified(modified,source):
	textSec = 0
	stackSec = 0
	globalVar = 0

	for el in modified:
		print(el[0],bin(el[0]),source[0],bin(source[0]),len(bin(el[0]^source[0])))
		textSec += len(bin(el[0]^source[0]))
		stackSec +=  len(bin(el[1]^source[1]))
		globalVar +=  len(bin(el[2]^source[2]))
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
	NoASLRData = load(NoASLRFile)
	
	print(avgBitModified(ASLRData,NoASLRData))
	print(varModified(ASLRData))
