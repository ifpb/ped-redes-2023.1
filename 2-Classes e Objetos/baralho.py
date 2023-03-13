import random

class Carta:

    def __init__(self, valor, naipe):
        self.__naipe = naipe
        self.__valor = valor

    @property
    def naipe(self):
        return self.__naipe

    @property
    def valor(self):
        return self.__valor

    @staticmethod
    def calcular_valor(carta):
        if carta.valor == 'A':
            return 0
        elif carta.valor == 'J':
            return 11
        elif carta.valor == 'Q':
            return 12
        elif carta.valor == 'K':
            return 13
        else:
            return int(carta.valor)

    def __str__(self):
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        self.__cartas = self.__obter_cartas()
        self.embaralhar()

    @property
    def cartas(self):
        return self.__cartas

    def __obter_cartas(self):
        return [Carta('A', 'copas'), Carta('2', 'copas'), Carta('3', 'copas'), Carta('4', 'copas'), Carta('5', 'copas'), Carta('6', 'copas'), Carta('7', 'copas'), Carta('8', 'copas'), Carta('9', 'copas'), Carta('10', 'copas'), Carta('J', 'copas'), Carta('Q', 'copas'), Carta('K', 'copas'),
           Carta('A', 'espadas'), Carta('2', 'espadas'), Carta('3', 'espadas'), Carta('4', 'espadas'), Carta('5', 'espadas'), Carta('6', 'espadas'), Carta('7', 'espadas'), Carta('8', 'espadas'), Carta('9', 'espadas'), Carta('10', 'espadas'), Carta('J', 'espadas'), Carta('Q', 'espadas'), Carta('K', 'espadas'),
           Carta('A', 'paus'), Carta('2', 'paus'), Carta('3', 'paus'), Carta('4', 'paus'), Carta('5', 'paus'), Carta('6', 'paus'), Carta('7', 'paus'), Carta('8', 'paus'), Carta('9', 'paus'), Carta('10', 'paus'), Carta('J', 'paus'), Carta('Q', 'paus'), Carta('K', 'paus'),
           Carta('A', 'ouros'), Carta('2', 'ouros'), Carta('3', 'ouros'), Carta('4', 'ouros'), Carta('5', 'ouros'), Carta('6', 'ouros'), Carta('7', 'ouros'), Carta('8', 'ouros'), Carta('9', 'ouros'), Carta('10', 'ouros'), Carta('J', 'ouros'), Carta('Q', 'ouros'), Carta('K', 'ouros')]

    def embaralhar(self):
        random.shuffle(self.__cartas)

    def imprimir_cartas(self):
        # for c in self.__cartas:
        #     print(str(c))
        ## Versão com compreensão de listas - List Comprehension:
        print([str(c) for c in self.__cartas])

    def retirar_carta_topo(self):
        if not self.vazio():
            return self.__cartas.pop()

    def vazio(self):
        return self.total_cartas() == 0
    
    def total_cartas(self):
        return len(self.__cartas)

class Jogador:

    __PROX_ID = 1

    def __init__(self):
        self.__cartas = []
        self.__pontuacao_total = 0
        self.__id = self.__class__.__PROX_ID
        self.__class__.__PROX_ID += 1

    @property
    def cartas(self):
        return self.__cartas
    
    @property
    def pontuacao_total(self):
        return self.__pontuacao_total
    
    @property
    def id(self):
        return self.__id

    def receber_carta(self, carta):
        if carta is None:
            return
        self.__pontuacao_total += Carta.calcular_valor(carta)
        self.cartas.append(carta)

    def imprimir_cartas(self):
        print([str(c) for c in self.cartas])

    def __str__(self):
        return f"Jogador {self.id}"

class Partida:
    def __init__(self, num_jogadores=2):
        assert num_jogadores >= 1 and num_jogadores <= 4,  "Número de jogadores deve ser de 1 a 4"
        self.__jogadores = []
        self.__baralho = Baralho()
        self.__num_jogadores = num_jogadores
        self.__criar_jogadores()
        self.__distribuir_cartas()

    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def baralho(self):
        return self.__baralho
    
    @property
    def num_jogadores(self):
        return self.__num_jogadores

    def __criar_jogadores(self):
        for i in range(self.num_jogadores):
            j = Jogador()
            self.jogadores.append(j)

    def __distribuir_cartas(self):
        while not self.baralho.vazio():
            for j in self.jogadores:
                j.receber_carta(self.baralho.retirar_carta_topo())

    def imprimir_distribuicao_cartas(self):
        print("Distribuição de cartas para jogadores: ")
        for j in self.jogadores:
            print(f"Jogador {j.id}: ")
            j.imprimir_cartas()
            print()

    def imprimir_ranking_pontuacao(self):
        self.ordenar_jogadores_por_pontuacao()
        for p, j in enumerate(self.jogadores, 1):
            print(f"{str(p)} - Jogador {str(j.id)} ({j.pontuacao_total} pontos)")

    def ordenar_jogadores_por_pontuacao(self):
        self.jogadores.sort(reverse=True, key=lambda j: j.pontuacao_total)

    def declarar_vencedor(self):
        self.ordenar_jogadores_por_pontuacao()
        vencedores = [self.jogadores[0]]
        ## Procura por empate
        for j in self.jogadores[1:]:
            if j.pontuacao_total == vencedores[0].pontuacao_total:
                vencedores.append(j)

        if len(vencedores) == 1:
            print(f"Jogador {vencedores[0].id} foi o vencedor!")
        else:
            print(f"Temos um empate entre os jogadores: {[j.id for j in vencedores]}")

if __name__ == '__main__':
    ## Parte 1: ###
    baralho = Baralho()
    baralho.imprimir_cartas()
    print("Total de cartas = ", baralho.total_cartas())

    ## Parte 2: ###
    try:
        partida = Partida(int(input("Digite o número de jogadores: "))))
        partida.imprimir_distribuicao_cartas()
        partida.imprimir_ranking_pontuacao()
        partida.declarar_vencedor()
    except AssertionError as error:
        print(error)
    
   
    

