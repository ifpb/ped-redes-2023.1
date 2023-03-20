class Onibus:
    def __init__(self, lugares, marca, velocidade=0):
        self.lugares = lugares
        self.marca = marca
        self.velocidade = velocidade
        self.__direcao = 0

    @property
    def direcao(self):
        return self.__direcao

    @direcao.setter
    def direcao(self, dir):
        if self.velocidade == 0:
            print("Não é possível mudar de direção parado")
        else:
            self.__direcao = dir

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
        print("Garagem construída!")
        self.vagas = vagas

    def adicionar_veiculo(self):
        self.vagas -= 1
    
    def retirar_veiculo(self):
        self.vagas += 1

    def __del__(self):
        print("Garagem destruída!")