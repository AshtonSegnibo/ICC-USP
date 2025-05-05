
def fibonacci_sequence(n):
    a,b=0,1
    lista=[]
    for i in range(n):
        lista.append(a)
        a,b=b,a+b
    return lista

def fibonacci(n):
    a=0
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
n=int(input())

print(fibonacci(n-1))