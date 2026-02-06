filename = r"C:\Users\ellio\Downloads\Clipping\[11-26-25] Northernlion - mike patton watching welcome to derry ｜ !prime ｜ Mister New PC - Chat.txt"

messagetimes = []
snum = []

with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        word =line[1:8]
        word =int(word.replace(':',''))
        word = 10*round(word/10)
        messagetimes.append(str(word))
        print(word)

uniques = list(set(messagetimes))
for i in range(len(uniques)):
    snum.append(str(messagetimes.count(uniques[i])))

print('done')

with open(r"C:\Users\ellio\Downloads\Clipping\messageTimes.txt", "w", encoding='utf-8') as file:
    for i in range(len(uniques)):
        file.write(uniques[i]+'\n')

with open(r"C:\Users\ellio\Downloads\Clipping\messageNumbers.txt", "w", encoding='utf-8') as file:
    for i in range(len(snum)):
        file.write(snum[i]+'\n')