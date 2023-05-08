from listaencadeada import ListaEncadeada
from listautils import ListUtils


class ListaComposta(ListaEncadeada):
    def __str__(self):
        res = ""
        atual = self.cabeca
        while atual is not None:
            res += ListUtils.join(atual.carga, " -> ")
            atual = atual.prox
            res += " -> " if atual is not None else ""
        return res