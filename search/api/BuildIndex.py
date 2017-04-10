from codecs import open as openCodec
from Normalize import Normalize
from time import localtime, strftime
from collections import defaultdict
from io import open as openToWrite

WordIndex = defaultdict(list)

def BuildIndex(DataPath, OutputPath):
	print("Enter %s" %DataPath)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	with openCodec(DataPath, 'r', "utf-8") as DataFile:
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
		print("Add %s to words' dictionary in position %s" %(nWord, WordPosition))
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		updateDictionary(nWord, LinePosition, WordPosition)
		WordPosition = WordPosition + 1
	return 1
	
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
	return 1
	
def exportIndex(OutputPath):
	print("Create and open datafile for writing %s" %OutputPath)
	createFile = open(OutputPath, 'w+')
	createFile.close()
	with openToWrite(OutputPath, mode='a+', encoding="utf-8") as outDataFile:		
		global WordIndex
		for KeyWord in WordIndex:
			print("Print keyword's array length to file, curren len: %s" %len(WordIndex[KeyWord]))
			print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
			tempLength = len(WordIndex[KeyWord])
			outDataFile.write(str(tempLength))
			outDataFile.write("\n")
			print("Print keyword %s to file" %KeyWord)
			print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
			outDataFile.write(KeyWord)
			outDataFile.write("\n")
			print("Print word count: %s to file" %WordIndex[KeyWord][0])
			print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
			outDataFile.write(str(WordIndex[KeyWord][0]))
			outDataFile.write("\n")
			for i in range(1, len(WordIndex[KeyWord])):
				print("Line: %s" %WordIndex[KeyWord][i][0])
				print("Position: %s" %WordIndex[KeyWord][i][1])
				print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
				outDataFile.write(str(WordIndex[KeyWord][i][0]))
				outDataFile.write(str(WordIndex[KeyWord][i][1]))
				outDataFile.write("\n")
	return 1
	
def ImportIndex(DataPath):
	with openCodec(DataPath, 'r', "utf-8") as DataFile:
		global WordIndex
		Flag = 1
		Word = ""
		Line = 0
		Position = 0
		KeyLength = 0
		CountLine = 0
		flagLine = 0
		for line in DataFile:
			if line == "":
				print("Reach EOF after reading, exit")
				return 1
			if flag == 1:
				Word = ""
				Line = 0
				Position = 0
				CountLine = 0
				KeyLength = line
				KeyLength = KeyLength - 1
				flag = 2
			if flag == 2:
				Word = line
				flag = 3
			if flag == 3:
				NewIndexEntry = [(Word, 1)]
				for word, NewEntry in NewIndexEntry: 
					WordIndex[word].append(NewEntry)
				flag = 4
			if flag == 4:
				if CountLine == KeyLength:
					flag = 1
				else:
					if flagLine == 0:
						Line = line
						flagLine = 1
					else: 
						Position = line
						CountLine = CountLine + 1
						flagLine = 0
						NewPositionEntry = (Line, Position)
						NewIndexEntry = [(Word, NewPositionEntry)]
						for word, NewEntry in NewIndexEntry: 
							WordIndex[word].append(NewEntry)
	return WordIndex
					
				
				
				
	#not implemented