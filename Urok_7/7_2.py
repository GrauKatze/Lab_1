spisok=list()
while True:
    word = input()
    if word == "СТОП":
        continue
    spisok.append(input())
for i in spisok:
    if "кот" in spisok[i]:
        print(i)
    else:
        print(-1)