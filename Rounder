import os

fileNames = os.listdir()

tempList = []
for file in fileNames:
	if file[len(file)-2] == 'x':
		tempList.append(file)
fileNames = tempList
master = fileNames[len(fileNames)-1]
fileNames.pop(len(fileNames)-1)

for filename in fileNames:
    newFile = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                newFile.append(line[0:(len(line)-2)]+'00')
    except Exception as e:
        print(f"error: {e}") 
        
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in newFile:
                file.write(f'{line}\n')
    except Exception as e:
        print(f'error: {e}')