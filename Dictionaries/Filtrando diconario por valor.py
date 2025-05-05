
n=int(input().strip())

dicionario={} 

letras=[]
numeros=[]

info=[]

for i in range(n*2):
    info.append(input().strip())

for i in range(len(info)):
    if i%2==0:
        letras.append(info[i])
    else:
        numeros.append(info[i])
numeros=list(map(int,numeros))


for i in range(n):
    dicionario[letras[i]]=numeros[i]

limite=int(input())
dicionario_novo={nome: num for nome, num in dicionario.items() if num > limite}

print(dicionario_novo)  

