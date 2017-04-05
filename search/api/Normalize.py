def NormalizeWord(word):
	for Character in ['[', ']', '(', ')']:
		word = word.replace(Character, "")
	return word