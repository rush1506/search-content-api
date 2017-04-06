from pathlib import Path
from Normalize import Normalize
from collections import defaultdict
from time import localtime, strftime
from collections import Counter

def isSearchable(DataPath):
	DataFile = Path(DataPath)
	if DataFile.is_file():
		return true
	else:
		return false

def SearchIndex(SearchString, WordIndex):
	print("Get word list from search string %s" %SearchString)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	WordList = getWordList(SearchString)
	WordsCount = getWordListCount(SearchString)
	SearchStringIndex = defaultdict(list)
	print("Get index from database")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SearchStringIndex = getIndexFromDatabase(WordIndex, WordList)
	#print("Trim index")
	#print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	#SearchStringIndex = trimSearchIndex(SearchStringIndex)
	print("Sort index")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	ResultIndex = sortIndex(SearchStringIndex, WordsCount)
	return ResultIndex
	
def getWordList(SearchString):
	print("Split \"%s\" into word list" %SearchString)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	wordsList = SearchString.split()
	return wordsList

def getWordListCount(SearchString):
	print("Get word count from string %s" %SearchString)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	wordsList = SearchString.split()
	wordCount = Counter(wordsList)
	print("Word count: %s" %wordCount)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return wordCount

def trimSearchIndex(SearchStringIndex):
	#not implemented
	return true

def sortIndex(SearchStringIndex, WordsCount):
	SortedIndex = defaultdict(list)
	print("Begin finding document that contains search words")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = sortMatchPosition(SortedIndex, WordsCount)
	print("Sort index based on single count in document")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = prioritizeBasedOnCount(SortedIndex)
	rint("Sort index based on heuristic distance, not implemented yet")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = prioritizeBasedDistance(SortedIndex)
	return SortedIndex
	
def prioritizeBasedDistance(Index):
	#not implemented
	return Index

def sortMatchPosition(Index, WordsCount):
	SortedIndex = defaultdict(list)
	k = 0
	for i in range(1, WordsCount):
		for ChosenPosition in Index[i]:
			print("Chosen position: ")
			print(ChosenPosition)
			for j in range(2, WordsCount + 1):	
				for Position in Index[j]:
					print("Position: ")
					print(Position)
					if ChosenPosition == Position:
						SortedIndex[k].append(Position)
						print("Pop position in %s" %j)
						Index[j].pop(Position)
		print("Add chosen position to sorted index")
		SortedIndex[k].append(ChosenPosition)
		print("Pop chosen position in %s" %i)
		WordsCount[i].pop(ChosenPosition)
		k = k + 1
	return SortedIndex
	
def prioritizeBasedOnCount(Index):
	for ChosenPosition in range(0, len(Index) - 1):
		for Position in range(1, len(Index)):
			print("Compare chosen position len: %s and position len %s" %(len(Index[ChosenPosition]), len(Index[Position])))
			PositionLen = len(Index[Position])
			ChosenPositionLen = len(Index[ChosenPosition])
			if ChosenPositionLen < PositionLen:
				tmp = Index[Position]
				Index[Position] = Index[ChosenPosition]
				Index[ChosenPosition] = tmp
	return Index
				
		
	
		
def getIndexFromDatabase(WordIndex, WordList):
	SearchIndex = defaultdict(list)
	for word in WordList:
		word = Normalize(word)
		print("get search word's inversed index from word index")
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		i = 0
		for PositionList in WordIndex[word]:
			if 0 == i:
				print("skip word count")
			else:
				SearchIndex[i].append(WordIndex[word][i])
			i = i + 1
		print("Curent index for %s" %word)
		print(SearchIndex[word])
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return SearchIndex