pas = input()
if len(pas)>8:
    if "123" in pas:
        print("простой")
        exit()
    if input() == pas:
        print("OK")
    else:
        print("Различаются")
else:
    print("Простой!")
