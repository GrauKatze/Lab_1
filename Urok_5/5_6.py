num1 = int(input())
num2 = int(input())
num3 = int(input())
while num1 != 0 or num2 != 0 or num3 != 0:
    num = int(input())
    if num == 1:
        num1 -= int(input())
    elif num == 2:
        num2 -= int(input())
    elif num == 3:
        num3 -= int(input())
    print(num1, num2, num3)
