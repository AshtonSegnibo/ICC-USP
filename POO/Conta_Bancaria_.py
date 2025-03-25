class conta_bancaria(object):
    def __init__(self,nome,saldo):
        self.nome=nome
        self.saldo=saldo
    def deposito(self,valor):
        self.deposito=self.saldo+valor
        return self.deposito
    
    def saque(self,valor):
        self.saque=self.saldo-valor
        return self.saque
    def saldo_final(self,final):
        self.final=saldo+deposito-saque
        return self.final
    
nome=input()
saldo=int(input()) 
deposito=int(input())
saque=int(input())
p=conta_bancaria(nome,saldo)
print(f'Saldo final: {float(p.saldo_final(saldo+deposito-saque))}')