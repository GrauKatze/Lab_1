num = int(input("enter num"))
if (num//100 == (num//10) % 10) or (num//100 == num % 10) or ((num//10) % 10 == num % 10):
    print("Две одинаковые цифры")
elif num//100 == (num//10) % 10 and num//100 == num % 10:
    print("Все цифры одинаковые")
else:
    print("OK")