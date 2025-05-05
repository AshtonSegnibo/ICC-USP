num=list(map(int,input().split())) #1 2 3 7 6
def substrings(num):
    n=len(num)
    lista=[]
    for i in range(n):
        for j in range(i+2,n+1):
            for k in range(1,n):
                a=num[i:j:k]
                if len(a)>1 and a not in lista:
                    lista+=[num[i:j:k]]
    for z in lista:
        if sum(z) == num[-1]:
           return(True)
    return False
print(substrings(num))
