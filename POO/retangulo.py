class retangulo():
    def __init__(self,largura,altura):
        self.largura=largura
        self.altura=altura
    def calcular_area(self):
        area=self.largura*self.altura
        print(f'Área: {float(area)}')
    def calcular_per(self):
        perimetro=(self.largura+self.altura)*2
        print(f'Perímetro: {float(perimetro)}')
        
largura=float(input())
altura=float(input())
x=retangulo(largura,altura)
x.calcular_area()
x.calcular_per()

