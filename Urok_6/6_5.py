num = int(input())
damag=list()

while num>0:
    damag.append(int(input()))
    damag.append(int(input()))
i=0
j=0
chisl=0
while i<len(damag):
    while j<len(damag):
        if j==i:
            continue
        else:
            chisl+=damag[i]*damag[j]
        j+2
    j=0
    i+=2
znam=1
i=1
while i<len(damag):
    znam*=damag[i]
    i+2
while chisl != 0 and znam!= 0:
    if chisl > znam:
       chisl=chisl% znam
    else:
       znam=znam% chisl
 
nod = chisl + znam

print(str(chisl//nod)+"/"+str(znam//nod))

