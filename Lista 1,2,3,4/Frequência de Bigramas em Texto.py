a=input()
x=a.lower()
"python é ótimo e python é versátil"
y=x.split()
"['python', 'é', 'ótimo', 'e', 'python', 'é', 'versátil']"
lista=[]
unicos=[]
contagem=[]
for i in range(len(y)-1):
    bigrama=(y[i],y[i+1])
    lista.append(bigrama)

for bigrama in lista:
    if bigrama in unicos:
        indice=unicos.index(bigrama)
        contagem[indice]+=1
    else:
        unicos.append(bigrama)
        contagem.append(1)

for j in range(len(unicos)):
    z=' '.join(unicos[j])
    w=contagem[j]
    print(z+":",w)
  
if abs(0.1+0.2-0.3)<0.00001: 
    print("true") 
    
else: 
    print("false")
    print(0.1+0.2)