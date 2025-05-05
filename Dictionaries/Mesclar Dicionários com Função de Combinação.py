y=int(input().strip()) #2

def dicionario(n):
    dic1={}
    lista=[]
    for i in range(n*2):
        lista.append(input().strip())

    for i in range(len(lista)): #4
        if i%2==0:
            dic1[lista[i]]=lista[i+1]
    return dic1

def combinacao(d1,d2):
    for letras, valor in d1.items():
        if letras in d2:
            d1[letras]=int(valor)+int(d2[letras])
        else:
            d1[letras]=int(valor)
    for letras, valor in d2.items():
        if not letras in d1:
            d1[letras]=int(valor)
    return d1

dicionario_1=dicionario(y)
z=int(input())
dicionario_2=dicionario(z)
print(combinacao(dicionario_1,dicionario_2))


