intervalo=int(input())

if intervalo<6:
     print("Erro: valor de N deve ser maior ou igual a 6")
else:
    numeros_perfeitos=[]

    for i in range(6,intervalo+1):
        soma_divisores=0
        for j in range(1,i):
                if i%j==0:
                    soma_divisores+=j
                else:
                    pass
        if soma_divisores==i:
         numeros_perfeitos.append(i)
                    
    if numeros_perfeitos:
        print(*numeros_perfeitos)
    else:
        print("Erro: valor de N deve ser maior ou igual a 6")
