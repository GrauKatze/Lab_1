num = int(input("enter num "))
pas1 = (num//100)+(num//10 % 10)
pas2 = num//10 % 10+num % 10
if pas1 > pas2:
    print(str(pas1)+str(pas2))
else:
    print(str(pas2)+str(pas1))
