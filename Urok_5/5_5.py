from random import randint

num = int(input())
while num > 0:
    uncorrect = True
    if num < 4:
        pc_num = num
    else:
        pc_num = randint(1, 3)
    num -= pc_num
    if num == 0:
        print("User WIN")
        break
    print("Осталось " + str(num), "взято: " + str(pc_num))
    while uncorrect:
        user_num = int(input(">>>"))
        if user_num == 1 or user_num == 2 or user_num == 3:
            uncorrect = False
    print("Осталось " + str(num), "взято: " + str(user_num))
    num -= user_num
    if num == 0:
        print("PC WIN")
        break
