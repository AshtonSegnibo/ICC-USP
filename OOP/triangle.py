class triangulo():
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def verificar_validez(self):
        if self.lado1+self.lado2>self.lado3 and self.lado1+self.lado3>self.lado2 and self.lado2+self.lado3>self.lado1:
            print('Triângulo válido')
            return True
        else:
            print('Triângulo inválido')
            return False

    def calcular_perímetro(self):
        perimetro=self.lado1+self.lado2+self.lado3
        print(f'Perímetro: {perimetro}')
        return perimetro
    
    def calculo_area(self):
        if self.verificar_validez():  
            s=self.calcular_perímetro()/2
            area=(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3))**0.5
            print(f'Área: {area}')
        else:
            pass
        
lado1=float(input())
lado2=float(input())
lado3=float(input())
x=triangulo(lado1,lado2,lado3)
x.verificar_validez()
x.calcular_perímetro()
x.calculo_area()


