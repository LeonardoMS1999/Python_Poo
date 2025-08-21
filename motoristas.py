#menu com duas opcoes, cadastrar e listar
#cada instancia do objeto cadastrado ficara guardado em uma lista
#o cadastro funciona, agora printar na tela todos motoristas ainda nao
# 

lista_motoristas = []

class Motorista():
    def __init__(self, nome, cpf, cnh):
        self.nome = nome
        self.cpf = cpf
        self.cnh = cnh

    def apresentar(self):
        print(f'... {self.nome} ... {self.cpf} ... {self.cnh} ...')

        
def menu():
    print("Voce deseja cadastrar um motorista ? ")
    opcao = int(input("1-Cadastrar ... 2-Listar todos Motoristas"))

    if opcao == 1:
        aNome = input("Digite o nome do motorista :")
        aCpf = int(input("Digite o CPF do motoritsta :"))
        aCnh = int(input("Digite o N de registo CNH :"))
        novoMotorista = Motorista(aNome, aCpf, aCnh)
        lista_motoristas.append(novoMotorista)
    
    elif opcao == 2:
        for x in lista_motoristas:
            apresentar()    
    else:
        pass

while True:
    menu()
