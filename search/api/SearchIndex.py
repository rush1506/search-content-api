from pathlib import Path
from Normalize import Normalize
from collections import defaultdict
from time import localtime, strftime
from collections import Counter

def isSearchable(DataPath):
	DataFile = Path(DataPath)
	if DataFile.is_file():
		return 1
	else:
		return 0

def SearchIndex(SearchString, WordIndex):
	print("Get word list from search string %s" %SearchString)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	WordList = getWordList(SearchString)
	print("Search word list: ")
	print(WordList)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	WordsCount = getWordListCount(SearchString)
	SearchStringIndex = defaultdict(list)
	print("Get index from database")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SearchStringIndex = getIndexFromDatabase(WordIndex, WordList)
	print("Search string's index: ")
	print(SearchStringIndex)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	#print("Trim index")
	#print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	#SearchStringIndex = trimSearchIndex(SearchStringIndex)
	print("Sort index")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	ResultIndex = sortIndex(SearchStringIndex, WordList)
	print("Return result from search: ")
	print(ResultIndex)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
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
	wordCount = len(wordsList)
	print("Word count: %s" %wordCount)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return wordCount

def trimSearchIndex(SearchStringIndex):
	#not implemented
	return 1

def sortIndex(SearchStringIndex, WordList):
	if len(WordList) == 1:
		print("Since there is only one word, we dont have to sort anything")
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		return SearchStringIndex
	SortedIndex = defaultdict(list)
	print("Begin finding document that contains search words")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = sortMatchPosition(SearchStringIndex, WordList)
	print("Sort index based on single count in document")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = prioritizeBasedOnCount(SortedIndex, WordList)
	print("Sort index based on heuristic distance, not implemented yet")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SortedIndex = prioritizeBasedDistance(SortedIndex, WordList)
	return SortedIndex
	
def prioritizeBasedDistance(Index, WordList):
	#not implemented
	return Index

def sortMatchPosition(Index, WordList):
	SortedIndex = defaultdict(list)
	count = -1
	for WordPositioni in range(0, len(Index) - 1):
		print("Word Position i: %s" %WordPositioni)
		print("Word i: %s" %WordList[WordPositioni])
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		i = 0
		for imember in Index[WordList[WordPositioni]]:
			print("imember: %s in word list position: %s" %(imember, WordPositioni))
			print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))	
			count = count + 1
			for WordPositionj in range(1, len(Index)):
				print("Word Position j: %s" %WordPositionj)
				print("Word j: %s" %WordList[WordPositionj])
				print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
				j = 0
				PopList = ()
				for jmember in Index[WordList[WordPositionj]]:
					print ("jmember: %s in word list position: %s" %(jmember, WordPositionj))
					print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
					if imember[0] == jmember[0]:
						print("in the same line")
						print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
						SortedIndex[count].append(imember)
						PopList
						Index[WordList[WordPositionj]].pop(j)
					j = j + 1
			Index[WordList[WordPositioni]].pop(i)
		i = i + 1
	print("Sorted Index: ")
	print(SortedIndex)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	input()
	return SortedIndex
	
def prioritizeBasedOnCount(Index, WordList):
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
			if i == 0:
				print("skip word count")
			else:
				SearchIndex[word].append(WordIndex[word][i])
			i = i + 1
		print("Curent index for %s" %word)
		print(SearchIndex[word])
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return SearchIndex