timestamps = []
badstamps = []

filename = r"C:\Users\ellio\Downloads\Clipping\[11-26-25] Northernlion - mike patton watching welcome to derry ｜ !prime ｜ Mister New PC - Chat.txt"

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if '-2' in line:
                word = line.strip()
                num = word[1:8]
                num = num.replace(":","")
                num = f'{num[:4]}.{num[4]}'
                num = float(num)
                num = str(round(num))
                num = f'{num}0'
                timestamps.append(num)
                print(num)
except Exception as e:
    print(f"error: {e}")

unique = list(set(timestamps))
uniquecount = []
length = len(unique)
for i in range(length):
    uniquecount.append(str(timestamps.count(unique[i])))
print(timestamps)
print(uniquecount)

filename2 = r"C:\Users\ellio\Downloads\Clipping\amount.txt"

with open(filename2, "w", encoding='utf-8') as file:
    for i in range(len(uniquecount)):
        file.write(uniquecount[i]+'\n')

with open(r"C:\Users\ellio\Downloads\Clipping\plus2.txt", "w", encoding='utf-8') as file:
    for i in range(len(unique)):
        file.write(unique[i]+'\n')