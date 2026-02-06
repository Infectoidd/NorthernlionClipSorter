filesList = [r"C:\Users\ellio\Downloads\Northernlion Chat Sort\[2-5-26].txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\-2.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\+2.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Cereal.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Cinema.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Classic.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Clueless.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Copium.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\ICANT.txt",
r"C:\Users\ellio\Downloads\Northernlion Chat Sort\Life.txt"]

def breakDown(stamp):
	stamp = stamp[1:8]
	stamp = stamp.replace(':','')
	stamp = int(stamp[0])*3600 + int(stamp[1:2])*60 + int(stamp[3:4])
	return str(stamp)

def readAndSort(filename, searchValue):
	listNums = []
	for file in filesList:
		try:
			with open(filename, 'r', encoding='utf-8') as file:
				for line in file:
					if searchValue in line:
						word = line.strip()
						num = breakDown(word)
		except Exception as e:
			print(f"error: {e}") 