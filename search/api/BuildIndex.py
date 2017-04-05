from codecs import open	
from Normalize import Normalize
from time import localtime, strftime
import datrie

def BuildIndex(DataPath, OutputPath):
	print("Enter %s" %DataPath)
	print("Timestamp: "strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	with open(DataPath, 'r', "utf-8") as DataFile:
		print("Open %s" %DataPath)
		print("Timestamp: "strftime("%a, %d %b %Y %H:%M:%S", localtime()))
		for line in DataFile:
			print("Process %s" %line)
			print("Timestamp: "strftime("%a, %d %b %Y %H:%M:%S", localtime()))
			updateNewIndexFrom(line)
	print("Export index to %s" %OutputPath)
	print("Timestamp: "strftime("%a, %d %b %Y %H:%M:%S", localtime()))
	exportIndex(OutputPath)
				
			