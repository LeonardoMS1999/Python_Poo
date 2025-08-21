class Carro():
    def __init__(self,marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.velocidade = int(velocidade)

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade == 0:
            print(f'A velocidade está zerada !, tente outro metodo... ')
        else:
            self.velocidade == 10
    
    def exibir_info(self):
        print()
        print(f'Veículo da Marca : {self.marca} ')
        print(f'Modelo :{self.modelo} ')
        print(f'Fabricado em : {self.ano} ')
        print(f'Está a {self.velocidade} Kilometros / Hora')
        

novoCarro1 = Carro("VW", "Fusca", 1990,0)
novoCarro2 = Carro("GM", "Marajó", 1986,0)

novoCarro1.acelerar()
novoCarro1.acelerar()
novoCarro1.frear()
novoCarro1.exibir_info()
novoCarro2.exibir_info()


