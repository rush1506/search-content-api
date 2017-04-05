from codecs import open	
from Normalize import Normalize
from time import strftime 
import datrie

def BuildIndex(DataPath, OutputPath):
	print("Enter %s" %DataPath)
	with open(DataPath, 'r', "utf-8") as DataFile:
		print("Open %s" %DataPath)
		for line in DataFile:
			print("Process %s" %line)
			updateNewIndexFrom(line)
	print("Export index to %s at" %OutputPath)
	strftime('%l:%M%p %z on %b %d, %Y')
	exportIndex(OutputPath)
				
			