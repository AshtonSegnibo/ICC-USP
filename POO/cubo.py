class cubo:
    def __init__(self,aresta):
        self.aresta=aresta
    def calcular_volume(self):
        volume=self.aresta**3
        return volume
    def calcular_areasuperficie(self):
        area=(self.aresta**2)*6
        return area
    
aresta=float(input())

if aresta <=0:
    print("A aresta deve ser um número positivo.")
else:
    ex=cubo(aresta)
    print(f'Volume: {round(float(ex.calcular_volume()),1)}\n'
          f'Área da Superfície: {float(ex.calcular_areasuperficie())}')

