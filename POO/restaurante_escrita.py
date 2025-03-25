class Restaurante:
    def __init__(self,mesa):
        print('Criando conta para mesa:',mesa)
        self.mesa=mesa
        self.itens=[]
        self.valores=[]

    def getMesa(self):
        return self.mesa
    
    def addItem(self,item,valor):
        self.itens.append(item)
        self.valores.append(valor)

    def getItens(self):
        return self.itens
    
    def getValores(self):
        return self.valores

contas={}
contas_encerradas=[]
    
def nova_conta(mesa):
    conta=Restaurante(mesa)
    contas[mesa]=conta
    return conta

def adicionar_item(mesa,item,valor):
    if mesa in contas:
        conta=contas[mesa]
        conta.addItem(item,valor)
    else:
        print('Mesa nao encontrada')

def exibir_itens(mesa,contas):
    if mesa in contas:
        for n,conta in contas.items():
            if n==mesa:
                print(f'Mesa {n} Pedidos: {conta.getItens()}')
                print(f'Mesa {n} Valores: {conta.getValores()}')
    else:
        print('Mesa nao encontrada')

def exibir_total(mesa,contas):
    for n,conta in contas.items():
        if n==mesa:
            valores=conta.getValores()
            total=sum(valores)
            print(f'Mesa {n} Total: {total}')

def encerrar_conta(mesa,contas):
    if mesa in contas:
        contas_encerradas.append(mesa)
        contas.pop(mesa)
    else:
        print('Mesa nao encontrada')   

def Exibe_contas_encerradas(): 
    print(contas_encerradas)

    
while True:
    print('1 - Criar Conta')
    print('2 - Adicionar Item')
    print('3 - Exibir Itens')
    print('4 - Exibir Total')
    print('5 - Encerrar Conta')
    print('6 - Exibir Contas Encerradas')
    print('9 - Sair')
    opcao=int(input())
    if opcao==9:
        break


    if opcao !=6:
        numero=int(input('Numero da mesa: '))
    else:
        pass

    if opcao==1:   
        nova_conta(numero)
    elif opcao==2:
        item=input('Qual o pedido: ')
        valor=float(input('Valor: '))
        adicionar_item(numero,item,valor)
    elif opcao==3:
        exibir_itens(numero,contas)
    elif opcao==4:
        exibir_total(numero,contas)
    elif opcao==5:
        encerrar_conta(numero,contas)
    elif opcao==6:
        Exibe_contas_encerradas()
    else:
        pass
