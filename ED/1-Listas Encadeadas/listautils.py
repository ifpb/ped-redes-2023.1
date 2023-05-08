from listaencadeada import ListaEncadeada


class ListUtils:

    @staticmethod
    def clonar(lista):
        clone = ListaEncadeada()
        atual = lista.cabeca
        while atual is not None:
            clone.inserir_no_final(atual.carga)
            atual = atual.prox
        return clone

    @staticmethod
    def inverter(lista):
        invertida = ListaEncadeada()
        atual = lista.cabeca
        while atual is not None:
            invertida.inserir_no_inicio(atual.carga)
            atual = atual.prox
        return invertida

    @staticmethod
    def join(lista, sep):
        atual = lista.cabeca
        retorno = ""
        while atual is not None:
            retorno += str(atual.carga) + (sep if atual.prox is not None else "")
            atual = atual.prox
        return retorno

    @staticmethod
    def split(palavra, sep):
        lista = ListaEncadeada()
        novo = ""
        i = 0
        for c in list(palavra):
            novo += c if c is not sep else ""
            if c == sep or i == len(list(palavra)) - 1:
                lista.inserir_no_final(novo)
                novo = ""
            i += 1
        return lista

    @staticmethod
    def intercalar(lista1, lista2):
        atual = lista1.cabeca
        atual2 = lista2.cabeca
        lista3 = ListaEncadeada()
        while atual is not None or atual2 is not None:
            if atual is not None:
                lista3.inserir_no_final(atual.carga)

            if atual2 is not None:
                lista3.inserir_no_final(atual2.carga)

            if atual is not None:
                atual = atual.prox

            if atual2 is not None:
                atual2 = atual2.prox
        return lista3
