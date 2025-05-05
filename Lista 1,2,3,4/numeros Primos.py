#numeros Primos
num=int(input())
sequencia=list(range(2,num+1))

primos=[]
numero=[]

for i in range(2,num):
    for j in range (2,num):
        if sequencia[i-2]%j==0:
            primos.append(i)
for k in range(1,num):
    if num%k==0:
        numero.append(k)
if len(numero)==1:
        primos.append(num)

for i in primos:
    if primos.count(i)==1:
        print(i)