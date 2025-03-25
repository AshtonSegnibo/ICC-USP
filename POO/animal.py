class animal:
    def __init__(self,nome):
        self.nome=nome

    def faz_som(self):
        return "O animal faz um som"
    
class cachorro(animal):
    def __init__(self,nome):
        super().__init__(nome)

    def faz_som(self):
        return 'Late'
        

class gato(animal):
    def __init__(self,nome):
        super().__init__(nome)

    def faz_som(self):
        return 'Mia'
    
class passaro(animal):
    def __init__ (self,nome):
        super().__init__(nome)

    def faz_som(self):
        return 'Canta'
    


def tipo_do_animal():
    nome_animal=input().strip().lower()
    if nome_animal=="cachorro":
        tipo=cachorro(nome_animal)
    elif nome_animal=="gato":
        tipo=gato(nome_animal)
    elif nome_animal=="pássaro":
        tipo=passaro(nome_animal)
    else:
        print('Animal não reconhecido.')
        return
    print(f'O {nome_animal}: {tipo.faz_som()}')
tipo_do_animal()

