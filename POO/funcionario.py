class funcionario:
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario
    
    def calcular_bonus(self):
         return round(self.salario*1.1,1)
    
class gerente(funcionario):
    def __init__(self,nome,salario,departamento):
            super().__init__(nome,salario)
            self.departamento=departamento
    def calcular_bonus(self):
         return self.salario*1.2

nome_fun=input().strip()
salario_fun=float(input().strip())
nome_ger=input().strip()
salario_gen=float(input().strip())
departamento_ger=input().strip()

funcionario1=funcionario(nome_fun,salario_fun)
gerente1=gerente(nome_ger,salario_gen,departamento_ger)
print(f'{nome_fun}: Salário com bônus = {funcionario1.calcular_bonus()}\n{nome_ger}: Salário com bônus = {gerente1.calcular_bonus()}')