from estrutura_linear import *
from algoritmos_busca import *

class Arquivo:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    def __str__(self):
        return f"Nome = {self.nome}, Tamanho = {self.tamanho}"

class Fila(EstruturaLinear):
    def __init__(self):
        super().__init__()

    def inserir(self, arquivo):
        self.inserir_no_final(arquivo)

    def remover(self):
        return self.remover_do_inicio()
    
    def imprimir(self):
        self.imprimir_lista()

    def __iter__(self):
        atual = self.cabeca
        if atual is not None:
            yield atual
            atual = atual.prox
        else:
            return None
        while atual is not self.cabeca and atual is not None:
            yield atual
            atual = atual.prox

    def __setitem__(self, indice, valor):
        atual: 'No' = self.cabeca
        for i in range(indice):
            if atual is None:
                return
            atual = atual.prox
            atual.carga = valor

    def __getitem__(self, indice):
        if isinstance(indice, slice):
            start, stop, step = indice.indices(len(self))
            return [self[i] for i in range(start, stop, step)]
        else:
            atual: 'No' = self.cabeca
            if indice == 0:
                return atual
            else:
                atual = atual.prox
            for i in range(indice): 
                if atual is None:
                    return None
                if atual is not self.cabeca:
                    atual = atual.prox
                else:
                    atual = None
            return atual

    def __len__(self):
        contador = 0
        for atual in self:
            contador += 1
        return contador

    def ordenar(self):
        return self.quicksort(self)
    
    def buscar(self, arquivo):
        return busca_binaria_recursiva(self, arquivo)
    
    def quicksort(self, vetor):
        if len(vetor) <= 1: return vetor
        pivo = vetor[0].carga.tamanho
        iguais = [x for x in vetor if x.carga.tamanho == pivo]
        menores = [x for x in vetor if x.carga.tamanho < pivo]
        maiores = [x for x in vetor if x.carga.tamanho > pivo]
        resultado = Fila()
        return resultado.inserir_lista(self.quicksort(menores)).inserir_lista(iguais).inserir_lista(self.quicksort(maiores))

