from SearchIndex import SearchIndex
from BuildIndex import BuildIndex
from SearchIndex import isSearchable

def getSearchResult(SearchString):
	if (!isValid(SearchString)):
		return "no result found, search string is not valid"
	if (!isSearchable()):
		BuildIndex("../data/data.txt", "/result/index.txt")
	SearchResult = SearchIndex(SearchString)
	return SearchResult
	
def isValid(string):
	#not implemented
	#Only implemented if the search string have to be meaningful
	return true