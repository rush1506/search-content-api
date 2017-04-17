from io import open
#def getResultFromFile(DataPath, Index):
#	LineQuery =[] 
#	print("get line from data file")
#	for LineSet in Index:
#		print("current line position: %s" %Index[LineSet][0][0])
#		Line = seekFromFile(DataPath, Index[LineSet][0][0])
#		print("current line: %s" %Line)
#		LineQuery.append(Line)
#	return LineQuery
	
def printResultFromFile(DataPath, Index):
	LineQuery =[] 
	print("get line from data file")
	for LineSet in Index:
		for PositionSet in LineSet:
			print("current line position: %s" %Index[LineSet][PositionSet][0])
			Line = seekFromFile(DataPath, Index[LineSet][PositionSet][0])
			print("current line: %s" %Line)
			LineQuery.append(Line)
	return LineQuery
	
def exportResultFromFile(DataPath, Index):
	createFile = open(OutputPath, 'w+')
	createFile.close()
	count = 0
	with openToWrite(OutputPath, mode='a+', encoding="utf-8") as ResultFile:	
		LineQuery =[] 
		print("get line from data file")
		for LineSet in Index:
			for PositionSet in LineSet:
				print("current line position: %s" %Index[LineSet][PositionSet][0])
				Line = seekFromFile(DataPath, Index[LineSet][PositionSet][0])
				print("current line: %s" %Line)
				ResultFile.write("Count: %s" %count)
				ResultFile.write(Line)
				ResultFile.write("\n")
				LineQuery.append(Line)
				count = count + 1
	return LineQuery
		
	
def seekFromFile(DataPath, LineNumber):
	with open(DataPath, mode="r", encoding="utf-8") as DataFile:
		LineCount = 0
		LineNumber = int(LineNumber) - 1
		for line in DataFile:
			if LineCount == LineNumber:
				return line
			LineCount = LineCount + 1
	
			
	