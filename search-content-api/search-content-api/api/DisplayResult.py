from io import open
def getResultFromFile(DataPath, Index):
	LineQuery =[] 
	print("get line from data file")
	for LineSet in Index:
		print("current line position: %s" %Index[LineSet][0][0])
		Line = seekFromFile(DataPath, Index[LineSet][0][0])
		print("current line: %s" %Line)
		LineQuery.append(Line)
	return LineQuery
		
	
def seekFromFile(DataPath, LineNumber):
	with open(DataPath, mode="r", encoding="utf-8") as DataFile:
		LineCount = 0
		LineNumber = int(LineNumber) - 1
		for line in DataFile:
			if LineCount == LineNumber:
				return line
			LineCount = LineCount + 1
	
			
	