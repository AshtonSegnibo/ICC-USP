import math
class Ponto(object):
    def __init__(self, x1, y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def distancia(self):
       distancia=math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
       return distancia
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
p=Ponto(x1,y1,x2,y2)
print(f'Distância: {p.distancia()}')