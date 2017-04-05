from pathlib import Path
from Normalize import Normalize
from collections import defaultdict
from time import localtime, strftime

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
	SearchStringIndex = defaultdict(list)
	print("Get index from database")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	SearchStringIndex = getIndexFromDatabase(WordIndex, WordList)
	#print("Trim index")
	#print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	#SearchStringIndex = trimSearchIndex(SearchStringIndex)
	print("Sort index")
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	ResultIndex = sortIndex(SearchStringIndex)
	return ResultIndex

def trimSearchIndex(SearchStringIndex):
	#not implemented
	return true

def sortIndex(SearchStringIndex):
	SortedIndex = defaultdict(list)
	#Sort Index: rank Word position in index using distance heuristic
	#Continue coding here
	return SortedIndex
	
		
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
				SearchIndex[word].append(WordIndex[word][i])
			i = i + 1
		print("Curent index for %s" %word)
		print(SearchIndex[word])
		print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return SearchIndex