import math
num  = int(input())
spisok=list()
i=0
while i <num:
    spisok.append(int(input()))
    i+=1
num=0
for i in spisok:
    num+=math.pow(-1,i+1)*i
print(num)