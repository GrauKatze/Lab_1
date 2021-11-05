from math import radians
from random import randint
num1 = int(input())
num2 = int(input())
while num1 > 0 or num2 > 0:
    uncorrect = True
    if num1 > 0 and num2 > 0:
        vibor = randint(1, 2)
    elif num1 > 0 and num2 == 0:
        vibor = 1
    elif num1 == 0 and num2 > 0:
        vibor = 2
    if vibor == 1:
        pc_num = randint(1, num1)
        num1 -= pc_num
    else:
        pc_num = randint(1, num2)
        num2 -= pc_num
    if not num1 and not num2:
        print("PC WIN")
        break
    print("Осталось " + str(num1) + str(num2), "взято: " + str(pc_num))
    while uncorrect:
        vibor = int(input(">>>"))
        if ((num1 > 0 and num2 > 0) and (vibor != 1 or vibor != 2)) or ((num1 > 0 and num2 == 0) and vibor != 1) or ((num1 == 0 and num2 > 0) and vibor != 2):
            continue
        user_num = int(input(">>>"))
        if (vibor == 1 and user_num > num1) or (vibor == 2 and user_num > num2):
            continue
        if vibor == 1:
            num1 -= user_num
        elif vibor == 2:
            num2 -= user_num
        uncorrect = False
    print("Осталось " + str(num1) +"-"+ str(num2), "взято: " + str(user_num))
    if not num1 and not num2:
        print("user WIN")
        break
