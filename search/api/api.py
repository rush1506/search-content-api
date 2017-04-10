from SearchIndex import SearchIndex
from BuildIndex import BuildIndex
from BuildIndex import ImportIndex
from SearchIndex import isSearchable
from collections import defaultdict

def getSearchResult(SearchString):
	#if (0 == isValid(SearchString)):
	#	return "no result found, search string is not valid"
	if (isSearchable("../../index/index.txt") == 0):
		print("There are no index file, building one")
		WordIndex = BuildIndex("../../../data/data.txt", "../../index/index.txt")
	else:
		print("Found index file, getting index")
		WordIndex = ImportIndex("../../index/index.txt")
	SearchResult = SearchIndex(SearchString, WordIndex)
	Display(SearchResult)
	return SearchResult
	
def isValid(string):
	#not implemented
	#Only implemented if the search string have to be meaningful
	return 1
		
def Display(SearchResult):
	print("Hello kitty bitches: ")
	print(SearchResult)
	

getSearchResult(u"hành tinh")