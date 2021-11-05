i = 10
num_max = 1000
num_min = 0
while i > 0:
    num = (num_min+num_max)//2
    print(num)
    if input() == ">":
        num_max = num
    elif input() == "<":
        num_min = num
    elif input() =="=":
        break
    i -= 1
    print(i)
