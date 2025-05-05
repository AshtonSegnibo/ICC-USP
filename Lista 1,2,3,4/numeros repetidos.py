x=input()
y=list(x)
numeros=[]

for i in y:
    if i.isdigit() and i!=" ":
        numeros+=i

repetidos=[]
vistos=set()

for n in numeros:
    if n in vistos:
        repetidos.append(n)
    else:
        vistos.add(n)

if len(repetidos)!=0:
    print(False)
else:
    print(True)
