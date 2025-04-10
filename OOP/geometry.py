import math
class FormaGeometrica:
    def __init__ (self,nome):
        self.nome=nome

class Quadrado(FormaGeometrica):
    def __init__(self,nome,lado):
        super().__init__(nome)
        self.lado=lado

    def calcular_area(self):
        area=self.lado**2
        return area
class retangulo(FormaGeometrica):
    def __init__(self,nome,largura,altura):
        super().__init__(nome)
        self.largura=largura
        self.altura=altura
    
    def calcular_area(self):
        area=self.largura*self.altura
        return area

class circulo(FormaGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio=raio

    def calcular_area(self):
        area=math.pi*(self.raio)**2
        return area
    
forma_desejada=input().lower().strip()

if forma_desejada=='quadrado':
    lado=float(input())
    quadrado=Quadrado(forma_desejada,lado)
    area=quadrado.calcular_area()
elif forma_desejada=='retângulo':
    largura=float(input())
    altura=float(input())
    ret=retangulo(forma_desejada,largura,altura)
    area=ret.calcular_area()
elif forma_desejada=='círculo':
    raio=float(input())
    circ=circulo(forma_desejada,raio)
    area=circ.calcular_area()
else:
    print('Forma geométrica não reconhecida.')
    exit()

print(f'A área do {forma_desejada} é: {area}')