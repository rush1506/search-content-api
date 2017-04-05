def NormalizeWord(word):
	for Character in ['[', ']', '(', ')']:
		word = word.replace(Character, "")
	word = putToLowCase(word)
	return word
	
def putToLowCase(word):
	return word.lower()