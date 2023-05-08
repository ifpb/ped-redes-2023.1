from listaencadeada import ListaEncadeada


class ListaLotadaException(Exception):
    pass


class ListaLimitada(ListaEncadeada):
    def __init__(self, capacidade=10):
        self.capacidade = capacidade
        self.elementos = 0
        super().__init__()

    def inserir_no_inicio(self, valor: object):
        if self.elementos < self.capacidade:
            super().inserir_no_inicio(valor)
            self.elementos += 1
        else:
            raise ListaLotadaException()

    def inserir_no_final(self, valor):
        if self.elementos < self.capacidade:
            super().inserir_no_final(valor)
            self.elementos += 1
        else:
            raise ListaLotadaException()

    def remover_do_inicio(self):
        super().remover_do_inicio()
        self.elementos -= 1

    def remover_do_final(self):
        super().remover_do_final()
        self.elementos -= 1
