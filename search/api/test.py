from collections import defaultdict


def foo():
	WordIndex = defaultdict(list)
	word = "test"
	NewPositionEntry = ('line', 'pos')
	NewIndexEntry = [(word, 1), (word, NewPositionEntry)]
	for word, NewEntry in NewIndexEntry:
		WordIndex[word].append(NewEntry)
		
	NewPositionEntry = ('line', 'posds')
	WordIndex[word].append(NewPositionEntry)
	
	print(len(WordIndex[word]))
		
	#if (WordIndex[word][1] == WordIndex[word][2]):
	#	print("test ok")
	return WordIndex
	
foo()