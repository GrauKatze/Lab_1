user = [0, 0]

corX = int(input())
corY = int(input())
gold = [corX, corY]

svet = 0
user_gold = list()
svet_gold = int()

i = 0
i_gold=0

command = str()
while command != "stop":
    if command == "направо":
        if svet == 4:
            svet = 0
        else:
            svet += 1
    elif command == "налево":
        if svet == 0:
            svet = 4
        else:
            svet -= 1
    elif command == "разворот":
        if svet == 3:
            svet = 1
        else:
            svet += 2
    elif command == "вперед":
        if svet == 0:
            user[1] += int(input())
        elif svet == 1:
            user[0] += int(input())
        elif svet == 2:
            user[1] -= int(input())
        elif svet == 3:
            user[0] -= int(input())

    if user == gold:
        if user_gold != gold:
            user_gold = user
            svet_gold = svet
            i_gold = i
        continue
    else:
        i+1
