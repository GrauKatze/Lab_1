from math import radians
from random import randint, randrange
num1 = int(input())
num2 = int(input())
num3 = int(input())
while num1 > 0 or num2 > 0 or num3 > 0:
    uncorrect = True
    if num1 > 0 and num2 > 0 and num3 > 0:
        vibor = randint(1, 3)
    elif num1 > 0 and num2 > 0 and num3 == 0:
        vibor = randint(1, 2)
    elif num1 > 0 and num2 == 0 and num3 > 0:
        vibor = randrange(1, 3, 2)
    elif num1 == 0 and num2 > 0 and num3 > 0:
        vibor = randint(2, 3)
    elif num1 > 0 and num2 == 0 and num3 == 0:
        vibor = 1
    elif num1 == 0 and num2 == 0 and num3 > 0:
        vibor = 3
    elif num1 == 0 and num2 > 0 and num3 == 0:
        vibor = 2

    if vibor == 1:
        pc_num = randint(1, num1)
        num1 -= pc_num
    elif vibor == 2:
        pc_num = randint(1, num2)
        num2 -= pc_num
    elif vibor == 3:
        pc_num = randint(1, num3)
        num3 -= pc_num

    if not num1 and not num2 and not num3:
        print("PC WIN")
        break

    print("Осталось " + str(num1) + "-" + str(num2) +
          "-"+str(num3), " взято: " + str(pc_num))
    while uncorrect:
        vibor = int(input(">>>"))
        if vibor == 1 and not num1 or vibor == 2 and not num2 or vibor == 3 and not num3:
            continue
        user_num = int(input(">>>"))
        if (vibor == 1 and user_num > num1) or (vibor == 2 and user_num > num2) or (vibor == 3 and user_num > num3):
            continue
        if vibor == 1:
            num1 -= user_num
        elif vibor == 2:
            num2 -= user_num
        elif vibor == 3:
            num3 -= user_num
        uncorrect = False
        print("Осталось " + str(num1) + "-" + str(num2) +
              "-"+str(num3), " взято: " + str(pc_num))
    if not num1 and not num2 and not num3:
        print("user WIN")
        break
