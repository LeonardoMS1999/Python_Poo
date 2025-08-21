#gosto de yugioh
#criar objeto monstro com atribudos das cartas

class Monstro():
    def __init__(self,nome,atributo,nivel,atk,defesa,tipo,descricao,nomeatk):
        self.nome = nome
        self.atributo = atributo
        self.nivel = nivel
        self.atk = atk
        self.defesa = defesa
        self.tipo = tipo
        self.descricao = descricao
        self.nomeatk = nomeatk    

    def invocar(self):
        if self.nivel > 4:
            print(f'Invocação Normal Com Tributo')
            print(f'Monster: {self.nome} / ATK: {self.atk} / DEF: {self.defesa}')
        else:
            print(f'Invocação Normal Sem Tributo')

    def atacar(self):
        print(f'ATAQUE {self.nomeatk} !')
    
    def defender(self):
        print(f'{self.nome} em modo de defesa')

magonegro = Monstro("Mago Negro","TREVAS",7,2500,2100,"Mago/Normal","O mago definitivo em termos de ataque e defesa.","Magia Negra")
magonegro.invocar()
magonegro.atacar()
magonegro.defender()
     

