from collections import defaultdict


def foo():
	WordIndex = defaultdict(list)
	word = "test"
	NewPositionEntry = ('line', 'pos')
	NewIndexEntry = [(word, 1), (word, NewPositionEntry)]
	for word, NewEntry in NewIndexEntry:
		WordIndex[word].append(NewEntry)
		
	WordIndex[word].append(NewPositionEntry)
		
	return WordIndex