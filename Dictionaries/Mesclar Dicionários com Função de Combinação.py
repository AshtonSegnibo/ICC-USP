y=int(input().strip()) #2

# 2 (quantos pares chave-valor deseja inserir no primeiro dicionário)
# a (chave) 0
# 10 (valor) 1
# b (chave) 2
# 5 (valor) 3
# 2 (quantos pares chave-valor deseja inserir no segundo dicionário)
# b (chave)
# 15 (valor)
# c (chave)
# 20 (valor)

# 2
# a
# 10
# b
# 5
# 2
# b
# 15
# c
# 20
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


