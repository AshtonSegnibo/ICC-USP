class funcionario:
    def __init__(self,nome,salario,percentual_bonus):
        self.nome=nome
        self.salario=salario
        self.percentual_bonus=percentual_bonus
    def calcularbonus(self):
        bonus=self.salario*self.percentual_bonus/100
        return round(bonus,2)
    def calcularsarioscom_bonus(self):
        salariocombonus=self.salario+self.calcularbonus()
        return salariocombonus
    def exibirdetalhes(self):
        return f"Funcionário: {self.nome}, Salário Base: R$ {self.salario:.2f}, Bônus: R$ {self.calcularbonus():.2f}, Salário Total: R$ {self.calcularsarioscom_bonus():.2f}"
    
nom1=input().strip()
salario1=float(input().strip())
percentual1=float(input().strip())

funcionario1=funcionario(nom1,salario1,percentual1)
if salario1<0 or percentual1<0:
    print("O salário e o percentual de bônus devem ser números positivos.")
else:
    print(funcionario1.exibirdetalhes())