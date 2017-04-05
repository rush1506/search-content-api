from time import localtime, strftime

def NormalizeWord(word):
	print("Normalize %s" %word)
	for Character in ['[', ']', '(', ')']:
		word = word.replace(Character, "")
	print("New word after eliminate special character: %s" %word)
	word = putToLowCase(word)
	print("final new word: %s" %word)
	print("Timestamp: " + strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	return word
	
def putToLowCase(word):
	return word.lower()