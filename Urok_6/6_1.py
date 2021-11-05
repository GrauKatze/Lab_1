import time
num = int(input())
if num > 0:
    while num > 0:
        print("Осталось секунд: " + str(num))
        num -= 1       
        time.sleep(1)        
print("Пуск")
