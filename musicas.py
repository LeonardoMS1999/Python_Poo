#guardar e listar minhas musicas preferidas

lista_musicas = []

class Musica():
    def __init__(self,nome, cantor):
        self.nome = nome
        self.cantor = cantor

    
def cadastrar():
    aNome = input("Digite o nome da música: ")
    aCantor = input("Digite o nome do cantor: ")
    nova_musica = Musica(aNome,aCantor)
    lista_musicas.append(nova_musica)

def aprensentar():
    for x in lista_musicas:
        print()
        print(f'Music : {x.nome} - Cantor/Banda: {x.cantor}')

def menu():
    print('=' * 40)
    print('1- Cadastrar Musicas')
    print('2- Listar Musicas')
    entrada = int(input("Digite a Opção: "))
    if entrada == 1:
        cadastrar()
    elif entrada == 2:
        aprensentar()
    else :
        print("entrada invalida!")

while True:
    menu()
