num1 = float(input("enter num 1"))
num2 = float(input("enter num 2"))
delo = input("Enter deistvie")
if delo == "/":
    if num2 !=0:
        print(num1/num2)
    else:
        print(888888)
elif delo == "+":
    print(num1+num2)
elif delo == "*":
    print(num1*num2)
elif delo == "-":
    print(num1-num2)
else:
    print(888888)