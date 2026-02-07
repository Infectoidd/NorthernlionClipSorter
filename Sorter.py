import os

def breakDown(stamp):
	stamp = stamp[1:8]
	stamp = stamp.replace(':','')
	stamp = int(stamp[0])*3600 + int(stamp[1:2])*60 + int(stamp[3:4])
	return str(stamp)

def readAndSort(filename, searchValue):
	listNums = []
	for file in fileNames:
		try:
			with open(filename, 'r', encoding='utf-8') as file:
				for line in file:
					if searchValue in line:
						word = line.strip()
						num = breakDown(word)
						listNums.append(num)
		except Exception as e:
			print(f"error: {e}") 
	return listNums

fileNames = os.listdir()

print(fileNames)
for file in fileNames:
	if not file[len(file)-1] == 'x':
		fileNames.pop(fileNames[file])
print(fileNames)
# print(readAndSort(filesList[0], '+2'))
