from SearchIndex import SearchIndex
from BuildIndex import BuildIndex
from BuildIndex import ImportIndex
from SearchIndex import isSearchable
from collections import defaultdict
from DisplayResult import getResultFromFile

def getSearchResult(DataPath, IndexPath, SearchString):
	#if (0 == isValid(SearchString)):
	#	return "no result found, search string is not valid"
	if (isSearchable(IndexPath) == 0):
		print("There are no index file, building one")
		WordIndex = BuildIndex(DataPath, IndexPath)
	else:
		print("Found index file, getting index")
		WordIndex = ImportIndex(IndexPath)
	SearchResult = SearchIndex(SearchString, WordIndex)
	LineQuery = getResultFromFile(DataPath, SearchResult)
	Display(LineQuery)
	return SearchResult
	
def isValid(string):
	#not implemented
	#Only implemented if the search string have to be meaningful
	return 1
		
def Display(SearchResult):
	print("Result in display for visualization: ")
	print(SearchResult)
	
#instruction on how to use:
#getSearchResult("../../../data/data.txt", "../../index/index.txt", u"caasm")