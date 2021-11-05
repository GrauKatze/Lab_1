spisok=list()
i =0
while True:
    word = input()
    if word == "СТОП":
        print(-1)
        continue
    spisok.append(input())
    if "кот" in spisok[i]:
        print(i)
        break
    i+=1