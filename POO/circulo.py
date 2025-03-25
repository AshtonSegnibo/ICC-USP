import math
class circulo:
    def __init__(self,raio):
        self.raio=raio

    def calcular_area(self):
        return math.pi*(self.raio)**2
    
    def calcular_perimetro(self):
        return 2*math.pi*self.raio
    
raio=float(input())
bola=circulo(raio)
print(f'Área: {bola.calcular_area()}\nPerímetro: {bola.calcular_perimetro()}')
