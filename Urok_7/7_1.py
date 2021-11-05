num=int(input())
spisok=list()
i=0
while i < num:
    spisok.append(input())
    i+=1
for i in spisok:
    if "кот" in spisok[i]:
        print("МЯУ")
    else:
        print("NOO")