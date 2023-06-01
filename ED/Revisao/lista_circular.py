from no import No
class ListaCircular:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        print(atual)

        while atual is not self.cauda:  # Note que agora precisamos varrer a lista até encontrar a cauda, já que não há mais nenhum apontador para None
            print(atual.prox)
            atual = atual.prox

    def inserir_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo
            novo.prox.ant = novo
            self.cabeca.ant = self.cauda  ## adiciona referência para a cauda como anterior da cabeça
            self.cauda.prox = self.cabeca  ## atualiza referência do próximo da cauda para apontar para a nova cabeça

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda
            novo.ant.prox = novo
            self.cauda = novo
            self.cauda.prox = self.cabeca  ## adiciona referência para a cabeça como próximo da cauda
            self.cabeca.ant = self.cauda  ## atualiza referência do anterior da cabeça para apontar para a nova cauda

    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        removido = self.cabeca

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = self.cauda  # O anterior da nova cabeça agora passa a apontar para a cauda
            self.cauda.prox = self.cabeca  # O próximo da cauda passa a ser a nova cabeça

        return removido

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = self.cabeca  # o próximo da nova cauda agora passa a pontar para a cabeça
            self.cabeca.ant = self.cauda  # o anterior da cabeça passa a ser a nova cauda


