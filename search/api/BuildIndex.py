from codecs import open	
from Normalize import Normalize
from time import localtime, strftime
from collections import defaultdict

WordIndex = defaultdict(list)

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
			#stemming line, not yet implemented
			LinePosition = LinePosition + 1
			updateNewIndexFrom(line, LinePosition)
	print("Export index to %s" %OutputPath)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	exportIndex(OutputPath)
	global WordIndex
	return WordIndex
				

def updateNewIndexFrom(CurrentLine, LinePosition):
	print("Split into single word at " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	RawWordsList = CurrentLine.split()
	WordPosition = 0
	for RawWord in RawWordsList:
		print("Normalize %s at position %s" %(RawWord, WordPosition))
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		nWord = Normalize(RawWord)
		print("Add %s to words' dictionary" %(nWord, WordPosition))
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		updateDictionary(nWord, LinePosition, WordPosition)
		WordPosition = WordPosition + 1
	return true
	
def updateDictionary(word, LinePosition, WordPosition):
	global WordIndex
	if word in WordIndex:
		updateDictionaryValues(word, LinePosition, WordPosition)
	else:
		createDictionaryValues(word, LinePosition, WordPosition)
		
			
def createDictionaryValues(word, LinePosition, WordPosition):
	global WordIndex
	print("%s is a new word, add new word to dictionary" %word)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	NewPositionEntry = (LinePosition, WordPosition)
	print("Create new entry for: ")
	print(NewPositionEntry)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	NewIndexEntry = [(word, 1), (word, NewPositionEntry)]
	for word, NewEntry in NewIndexEntry: 
		WordIndex[word].append(NewEntry)

def updateDictionaryValues(word, LinePosition, WordPosition):
	global WordIndex
	print("%s is already an index member, update %s value" %(word, word))
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	NewPositionEntry = (LinePosition, WordPosition)
	WordCount = WordIndex[word][0]
	print("Old word count: %s" %WordCount)
	WordCount = WordCount + 1
	WordIndex[word][0] = WordCount
	print("Update new word count: %s" %WordCount)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	WordIndex[word].append(NewPositionEntry)
	print("Append to word index: ")
	print(NewPositionEntry)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return true
	
def exportIndex:
	return true
	#not implemented