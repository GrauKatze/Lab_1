otvet = list()
otvet.append(input("please input 'да' or 'нет'\n>>>"))
otvet.append(input("please input 'да' or 'нет' again\n>>>"))
if "да" == otvet[0] or "нет" == otvet[0]:
    if "да" == otvet[1] or "нет" == otvet[1]:
        print("ВЕРНО!")
    else:
        print("NO")
else:
    print("NOOOO")