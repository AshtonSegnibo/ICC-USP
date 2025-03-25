class Carro(object):
    def __init__ (self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
    
    def tempo(self):
        return 2024-self.ano
    
print()