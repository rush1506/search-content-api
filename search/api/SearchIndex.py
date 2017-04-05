from pathlib import Path


def isSearchable(DataPath):
	DataFile = Path(DataPath)
	if DataFile.is_file():
		return true
	else:
		return false
	
