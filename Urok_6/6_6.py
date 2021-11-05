import math
i=1
num=int(input())
sum=0
while i < num:
    sum+=math.pow(i,-1)
    i+=1
print(str(math.pi*math.pi/sum))