from codecs import open	
from Normalize import Normalize
from time import localtime, strftime
import datrie

def BuildIndex(DataPath, OutputPath):
	print("Enter %s" %DataPath)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	with open(DataPath, 'r', "utf-8") as DataFile:
		print("Open %s" %DataPath)
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		LinePosition = 0
		for line in DataFile:
			print("Process %s in line %s" %(line, LinePosition))
			print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
			LinePosition = LinePosition + 1
			updateNewIndexFrom(line)
	print("Export index to %s" %OutputPath)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	exportIndex(OutputPath)
				

def updateNewIndexFrom(CurrentLine):
	print("Split into single word at " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	RawWordsList = CurrentLine.split()
	WordPosition = 0
	for RawWord in RawWordsList:
		print("Normalize %s at position %s" %(RawWord, WordPosition))
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		nWord = Normalize(RawWord)
		print("Add %s to words' dictionary" %(nWord, WordPosition))
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		updateDictionary(nWord)
	return true
			