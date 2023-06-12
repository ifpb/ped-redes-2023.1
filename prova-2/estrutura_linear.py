class No:
    def __init__(self, carga: object = None,
                 ant: 'No' = None,
                 prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return '%s' % (self.carga)

class EstruturaLinear:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def imprimir_lista(self):
        if self.cabeca is None:
            return

        atual: 'No' = self.cabeca
        print(atual)

        while atual is not self.cauda:
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
        self.cabeca.ant = self.cauda
        self.cauda.prox = self.cabeca

    def inserir_lista(self, lista):
        for i in lista:
            self.inserir_no_final(i.carga)
        return self

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda
            novo.ant.prox = novo
            self.cauda = novo
            self.cauda.prox = self.cabeca
            self.cabeca.ant = self.cauda

    def remover_do_inicio(self):
        if self.cabeca is None:
            return

        elemento_a_remover = self.cabeca

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = self.cauda
            self.cauda.prox = self.cabeca

        return elemento_a_remover

    def remover_do_final(self):
        if self.cabeca is None:
            return

        elemento_a_remover = self.cauda

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = self.cabeca
            self.cabeca.ant = self.cauda

        return elemento_a_remover
