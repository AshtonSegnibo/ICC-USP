class produto:
    def __init__(self,nome,preco_unitario,quantidade_estoque,quantidade_vendida,percentual_desconto):
        self.nome=nome
        self.preco_unitario=preco_unitario
        self.quantidade_estoque=quantidade_estoque
        self.quantidade_vendida=quantidade_vendida
        self.percentual_desconto=percentual_desconto

    def calcularvalordesconto(self):
        return self.preco_unitario*(self.percentual_desconto/100)
    
    def calcularreceitamensal(self):
        receita_mensal=(self.preco_unitario-self.calcularvalordesconto())*self.quantidade_vendida
        return receita_mensal
    
    def exibirdetalhes(self):
        return f"Produto: {self.nome}\n" f"Preço Unitário: R$ {self.preco_unitario:.2f} | Estoque: {self.quantidade_estoque} unidades | Vendas no Mês: {self.quantidade_vendida} | Receita Mensal: R$ {self.calcularreceitamensal():.2f}"

nome_produto=input()
preco_unitario=float(input())
qntd_estoque=int(input())
qntd_vendida=int(input())
perc=float(input())

if any in [preco_unitario,perc,qntd_estoque]==0:
    print("Os valores de preço unitário, percentual de desconto e quantidade em estoque devem ser positivos.")
elif qntd_vendida > qntd_estoque:
    print("A quantidade vendida não pode ser maior que o estoque disponível.")
else:
    pdt=produto(nome_produto,preco_unitario,qntd_estoque,qntd_vendida,perc)
    print(pdt.exibirdetalhes())


