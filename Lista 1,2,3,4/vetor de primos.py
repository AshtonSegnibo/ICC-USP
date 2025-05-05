def primo(n):
    lista=[]
    for i in range(1,n):
        if n%i==0:
            lista.append(i)
    if len(lista)==1:
        return 1
    else:
        return 0

def lista_primos():
    B=max(num1,num2)
    A=min(num1,num2)
    valores=[]
    for i in range(A,B+1):
       if primo(i) == 1:
           valores.append(i)
    return valores

num1 = int(input())
num2 = int(input())
print(lista_primos())
