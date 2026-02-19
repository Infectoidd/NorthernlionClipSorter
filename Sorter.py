import os

def breakDown(stamp):
	stamp = stamp[1:8]
	stamp = stamp.replace(':','')
	print(stamp)
	stamp = int(stamp[0])*3600 + int(stamp[1:3])*60 + int(stamp[3:5])
	return str(stamp)

def readAndSort(filename, searchValue):
	listNums = []
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

tempList = []
for file in fileNames:
	if file[len(file)-2] == 'x':
		tempList.append(file)
fileNames = tempList

master = input('Enter the master file name: ')

fileNames.remove(master)

for file in fileNames:
	with open(file, 'w', encoding='utf-8'):
		pass

for file in fileNames:
	search = str(file)
	search = search[0:int(len(file)-4)]
	tempList = readAndSort(master, search)
	with open(file, 'w', encoding='utf-8') as file:
		for time in tempList:
			file.write(f'{time}\n')	
		print(file)
