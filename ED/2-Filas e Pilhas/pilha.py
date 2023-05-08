from no import No


class PilhaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Pilha:
    def __init__(self):
        self.__topo = None

    @property
    def topo(self):
        return self.__topo

    @topo.setter
    def topo(self, topo):
        self.__topo = topo

    def push(self, valor):
        novo = No(valor)
        if self.__topo is None:
            self.__topo = novo
            return
        novo.prox = self.__topo
        self.__topo = novo

    def pop(self):
        if self.__topo is None:
            raise PilhaVaziaException("Pilha vazia, não foi possível remover!")
        elemento = self.__topo
        self.__topo = self.__topo.prox
        return elemento

    def remover_ate_elemento(self, elemento):
        while self.pop().carga != elemento:
            pass
        if self.topo.carga == elemento:
            self.pop()

    def is_empty(self):
        return self.__topo is None

    def __str__(self):
        return "[%s]" % self.__topo