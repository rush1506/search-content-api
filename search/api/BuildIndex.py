from codecs import open	
from Normalize import Normalize

def BuildIndex(DataPath):
	with open(DataPath, 'r', "utf-8") as DataFile:
		for line in DataFile:
			for word in line:
				word = Normalize(word)
				
			