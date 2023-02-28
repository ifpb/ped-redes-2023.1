class Onibus:
    def __init__(self, lugares, marca, velocidade=0):
        self.lugares = lugares
        self.marca = marca
        self.velocidade = velocidade
        self.direcao = 0

    def mudar_direcao(self, dir):
        if self.velocidade == 0:
            print("Não é possível mudar de direção parado")
        else:
            self.direcao = dir

    def acelerar (self, valor) :
        self.velocidade += valor

    def desacelerar(self, valor):
        self.velocidade -= valor
    
    def frear (self):
        self.velocidade = 0
    
    def buzinar (self):
        print ('Bi Biiiiiii')


class Garagem:
    def __init__(self, vagas):
        self.vagas = vagas

    def adicionar_veiculo(self):
        self.vagas -= 1
    
    def retirar_veiculo(self):
        self.vagas += 1