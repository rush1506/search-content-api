from SearchIndex import SearchIndex
from BuildIndex import BuildIndex
from SearchIndex import isSearchable

def getSearchResult(SearchString):
	if (!isValid(SearchString)):
		return "no result found, search string is not valid"
	if (!isSearchable("../../../data/data.txt")):
		WordIndex = BuildIndex("../../../data/data.txt", "../../index/index.txt")
	SearchResult = SearchIndex(SearchString, WordIndex)
	Display(SearchResult)
	return SearchResult
	
def isValid(string):
	#not implemented
	#Only implemented if the search string have to be meaningful
	return true