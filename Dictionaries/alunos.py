dic1=input().strip()
dic1=eval(dic1)

for chaves, valor in dic1.items():
    soma=0
    for i in range(len(valor)): 
        soma+=valor[i]
    soma=round(soma/len(valor),2)
    dic1[chaves]=float(soma)

print(dic1)