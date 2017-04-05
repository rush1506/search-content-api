from pathlib import Path
from Normalize import Normalize

def isSearchable(DataPath):
	DataFile = Path(DataPath)
	if DataFile.is_file():
		return true
	else:
		return false

def SearchIndex(SearchString, WordIndex):
	WordList = getWordList(SearchString)
	#do something, think later, I'm tired
	for word in WordList:
