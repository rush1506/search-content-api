from collections import defaultdict
from io import open

def foo():
	WordIndex = defaultdict(list)
	word = "test"
	NewPositionEntry = ('line', 'pos')
	NewIndexEntry = [(word, 1), (word, NewPositionEntry)]
	for word, NewEntry in NewIndexEntry:
		WordIndex[word].append(NewEntry)
		
	NewPositionEntry = ('line', 'posds')
	WordIndex[word].append(NewPositionEntry)
	
	for word in WordIndex:
		#print(WordIndex[word])
		#print(len(WordIndex[word]))
		for item in range(1, len(WordIndex[word])):
			print(WordIndex[word][item][0])
			print(WordIndex[word][item][1])
	#if (WordIndex[word][1] == WordIndex[word][2]):
	#	print("test ok")
	return WordIndex
	
foo()
#str="một"
#print(str)
#with open("datatest.txt", mode='a', encoding="utf-8") as file:
#	file.write(str)
#	file.write("\n")
#	file.write(u"Hai")