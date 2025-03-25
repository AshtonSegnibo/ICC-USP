class livros:
    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
    def exibir_informações(self):
        return f"{self.titulo} por {self.autor}"
        # print(f'{self.titulo} por {self.autor}')
    def verificar_tamanho(self):
        if self.paginas>500:
            print('Livro Longo')
        else:
            print('Livro Curto')
        
titulo=input().strip()
autor=input().strip()
paginas=int(input().strip())
livro=livros(titulo,autor,paginas)
print(livro.exibir_informações())
livro.verificar_tamanho()