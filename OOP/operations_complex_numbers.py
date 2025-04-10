import math

class complexo:
    def __init__ (self,xreal,ximag,yreal,yimag):
        self.xreal=xreal
        self.ximag=ximag
        self.yreal=yreal
        self.yimag=yimag
    
    def soma(self):
        zreal=self.xreal + self.yreal
        zimag=self.ximag + self.yimag
        return f'{zreal:.2f}+{zimag:.2f}i'

    def subtracao(self):
        zreal=self.xreal - self.yreal
        zimag=self.ximag - self.yimag
        return f'{zreal:.2f}+{zimag:.2f}i'
    
    def divisao(self):
        r=self.yreal**2+self.yimag**2
        zreal=(self.xreal*self.yreal+self.ximag*self.yimag)/r
        zimag=(self.ximag*self.yreal-self.xreal*self.yimag)/r
        return f'{zreal:.2f}+{zimag:.2f}i'
    
    def multiplicacao(self):
        zreal=self.xreal*self.yreal - self.ximag*self.yimag
        zimag=self.ximag*self.yreal+self.xreal*self.yimag
        return f'{round(zreal,2)}+{round(zimag,2)}i'
    
    def absoluto(self):
        ab=math.sqrt(self.xreal**2+self.ximag**2)
        aby=math.sqrt(self.yreal**2+self.yimag**2)
        return f'{round(ab,2)}\nabs:{round(aby,2):.2f}'
    
    def igual(self):
        if self.xreal==self.yreal and self.ximag==self.yimag:
            return True
        else:
            return False
        
operacoes=input().split()
operacoes=list(operacoes)

xreal,ximag =map(float,input().split(","))
yreal,yimag=map(float,input().split(","))

numero_complexo=complexo(xreal,ximag,yreal,yimag)

for i in operacoes:
    if i=="+":
        print(f'+:{numero_complexo.soma()}')
    elif i=="-":
        print(f'-:{numero_complexo.subtracao()}')
    elif i=="/":
        print(f'/:{numero_complexo.divisao()}')
    elif i=="abs":
        print(f'abs:{numero_complexo.absoluto()}')
    elif i=="==":
        print(f'==:{numero_complexo.igual()}')
    elif i=="*":
        print(f'*:{numero_complexo.multiplicacao()}')

            
        
