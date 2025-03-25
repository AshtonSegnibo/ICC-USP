class produto:
    def __init__(self,nome,preco_original,desconto):
        self.nome=nome
        self.preco_original=preco_original
        self.desconto=desconto
    def calcularprecocom_desconto(self):
        preçofinal=round(self.preco_original*(1-self.desconto/100),2)
        return preçofinal
    def exibirdetalhes(self):
        return f'Produto: {self.nome}, Preço Original: R$ {self.preco_original:.2f}, Preço com Desconto: R$ {self.calcularprecocom_desconto():.2f}'

nome=input().strip()
preço_original=float(input().strip())
desconto=float(input().strip())

if preço_original<0 or desconto<0:
    print('O preço original e o desconto devem ser números positivos.')
else:
    p1=produto(nome,preço_original,desconto)
    
    print(p1.exibirdetalhes())
