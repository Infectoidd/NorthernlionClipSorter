
import matplotlib.pyplot as plot
from random import randint

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

    data = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(int(line[0:(len(line)-2)]))

    dataSet = list(set(data))
    dataSet = sorted(dataSet)

    print(dataSet)

    dataOcc = []
    for d in dataSet:
        dataOcc.append(data.count(d))

    newDataSet = []
    newDataOcc= []
    iterate = 0

    while iterate < 17690:
        iterate += 10
        if iterate in dataSet:
            print(dataOcc[0])
            newDataSet.append(iterate)
            newDataOcc.append(dataOcc[0])

            dataSet.pop(0)
            dataOcc.pop(0)

        else:
            newDataSet.append(iterate)
            newDataOcc.append(0)

    plot.plot(newDataSet, newDataOcc)
    plot.xlabel(filename)
    plot.show()