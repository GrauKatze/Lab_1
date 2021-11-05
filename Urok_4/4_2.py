from typing import List


num_list = list()
znach = int()
num = 0
i = 0
while True:
    num = int(input())
    if num > (-300):
        num_list.append(num)
    else:
        break
for j in num_list:
    znach += j
    i += 1
print(znach/i)
