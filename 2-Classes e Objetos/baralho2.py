import collections
from random import choice

Carta = collections.namedtuple('Carta', ['valor', 'naipe'])

class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('JQKA')
    naipes = 'espadas paus copas ouro'.split()

    def __init__(self):
        self._cartas = [Carta(valor, naipe) for valor in self.valores for naipe in self.naipes]

    def __len__(self):
        return len(self._cartas)

    def __getitem__(self, pos):
        return self._cartas[pos]

if __name__ == '__main__':
    baralho = Baralho()
    print(choice(baralho))
    for c in baralho:
        print(c)

    print(Carta('Q', 'copas') in baralho)

