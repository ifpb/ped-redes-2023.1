from listaencadeada import ListaEncadeada, No


class ListaEncadeadaEstendida(ListaEncadeada):
    def pares(self):
        elementos_pares = ListaEncadeada()
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 == 0:
                elementos_pares.inserir_no_final(atual.carga)
            atual = atual.prox
        return elementos_pares

    def impares(self):
        elementos_impares = ListaEncadeada()
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 != 0:
                elementos_impares.inserir_no_final(atual.carga)
            atual = atual.prox
        return elementos_impares

    def buscar_pos(self, valor):
        atual = self.cabeca
        c = 0
        while atual is not None:
            if atual.carga == valor:
                # Encontramos o elemento
                return c
            atual = atual.prox
            c += 1
        return -1

    def inserir_pos(self, pos, valor):
        if pos == 0 or self.cabeca is None:
            self.inserir_no_inicio(valor)
            return
        c = 0
        atual = self.cabeca
        while atual is not None and c < pos - 1:
            atual = atual.prox
            c += 1

        novo = No(valor)
        novo.prox = atual.prox
        atual.prox = novo

    def remover_de_posicao(self, pos):
        if pos == 0 or self.cabeca == self.cauda:
            self.remover_do_inicio()
            return
        c = 0
        atual = self.cabeca
        while atual is not None and c < pos - 1:
            atual = atual.prox
            c += 1

        if atual is not None and atual.prox is not None:
            atual.prox = atual.prox.prox

    def remover_ocorrencias(self, valor):
        while self.remover_por_valor(valor):
            pass

    def remover_por_valor(self, valor):
        if self.cabeca is not None and self.cabeca.carga == valor:
            self.remover_do_inicio()
            return True
        atual = self.cabeca
        while atual.prox is not None:
            if atual.prox.carga == valor:
                atual.prox = atual.prox.prox
                return True
            atual = atual.prox
        return False
