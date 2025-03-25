class carro:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
    def ano_atual(self):
        idade=2024-self.ano
        # return f'{self.marca} {self.modelo}, {idade} anos de uso'
        return idade

marca=input().strip()
modelo=input().strip()
ano=int(input().strip())
car=carro(marca,modelo,ano)
print(f'{marca} {modelo}, {car.ano_atual()} anos de uso')