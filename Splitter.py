import os

fileNames = os.listdir()

def clean(stamp):
    stamp = stamp[0:len(stamp)-2]
    return int(stamp)

def stampToTime(num):
    hour = (num//3600)
    num = num -hour*3600

    minute = (num//60)
    num = num -minute*60

    return f'{hour}:{minute}:{num}'
     

tempList = []
for file in fileNames:
	if file[len(file)-2] == 'x':
		tempList.append(file)
fileNames = tempList
master = fileNames[len(fileNames)-1]
fileNames.pop(len(fileNames)-1)

data = []

for filename in fileNames:
    data = []

    with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data.append(line)
    tempList = []

    for i in data:
        tempList.append(clean(i))
        data.remove(i)
    
    data = tempList

    dataSet = list(set(data))
    dataSet = sorted(dataSet)

    dataOcc = []
    for d in dataSet:
        dataOcc.append(data.count(d))

    min = max(dataOcc)*0.35
    crossData = []
    for i in range(len(dataSet)):
        if dataOcc[i] > min:
            crossData.append(stampToTime(dataSet[i]))

    print(f'Crossing values in {filename}: {crossData}')
    