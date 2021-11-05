num = int(input())
sr_iq=0
max_iq=0
num_people=0
while num>0:
    iq=int(input())
    max_iq+=iq
    num_people+=1
    sr_iq=max_iq//num_people
    if iq==sr_iq:
        print(0)
    elif iq>sr_iq:
        print(">")
    elif iq<sr_iq:
        print("<")
    num-=1
