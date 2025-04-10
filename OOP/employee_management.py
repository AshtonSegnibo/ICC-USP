import math
n=int(input().strip())

class funcionario:
    def __init__(self,nome,salario,departamento):
        self.__nome=nome
        self.__salario=float(salario)
        self.__departamento=departamento

    def describe(self):
        return [self.__nome,self.__salario,self.__departamento]

    def get_nome(self):
        return self.__nome

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self,departamento):
        self.__departamento=departamento
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self,horas_trabalhadas):
        if horas_trabalhadas>50:
            horas_extras=horas_trabalhadas-50
            valor=horas_extras*(self.__salario/50)
            self.__salario += valor
        return self.__salario
    
def ajustar_salario(listas,nome,horas_trabalhadas):
    for f in listas:
        if f.get_nome()==nome:
            salario_ajustado=f.set_salario(horas_trabalhadas)
            return f.describe()
    return 'Funcionario nao encontrado'

def maior_salario(listas):
    maior=0
    for f in listas:
        if f.get_salario()>maior:
            maior=f.get_salario()
    for f in listas:
        if f.get_salario()==maior:
            return f.describe()
        
def alterar_departamento(listas,nome,novo_departamento):
    for f in listas:
        if f.get_nome()==nome:
            f.set_departamento(novo_departamento)
            return f.describe()

def media_salarial(listas):
    salarios=[]
    for f in listas:
        salarios.append(f.get_salario())
    media=sum(salarios)/n
    return media
    
        

listas=[]
for i in range(n):
    nome,salario,departamento=input().split()
    f=funcionario(nome,salario,departamento)
    listas.append(f)

def menu():
    opção=int(input())

    if opção==1:
        nome,horas_trabalhadas=input().split()
        horas_trabalhadas=float(horas_trabalhadas)
        resultado=ajustar_salario(listas,nome,horas_trabalhadas)
        print(f'{resultado[0]} {resultado[1]} {resultado[2]}')

    elif opção==2:
        resultado=maior_salario(listas)
        print(f'{resultado[0]} {resultado[1]} {resultado[2]}')
    
    elif opção==3:
        nome,novo_departamento=input().split()
        resultado=alterar_departamento(listas,nome,novo_departamento)
        print(f'{resultado[0]} {resultado[1]} {resultado[2]}')

    elif opção==4:
        resultado=media_salarial(listas)
        print(f'{resultado:.2f}')
    
menu()
