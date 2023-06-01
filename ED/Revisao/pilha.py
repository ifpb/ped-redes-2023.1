import random

from lista_circular import ListaCircular


def lista_numeros_aleatorios(qtd=10):
    lista = random.sample(range(0, 9999), qtd)
    return lista


class Pilha(ListaCircular):
    def __init__(self):
        super().__init__()

    def push(self, novo):
        super().inserir_no_inicio(novo)

    def pop(self):
        return super().remover_do_inicio()

if __name__ == '__main__':
    elementos = lista_numeros_aleatorios(50)
    pilha = Pilha()
    for elemento in elementos:
        pilha.push(elemento)

    print("Pilha original: ")
    pilha.imprimir_lista()

    print("Iterações: ")
    iteracoes = int(input("Digite a quantidade de itens que deseja percorrer na pilha"))
    atual = pilha.cabeca
    for iteracao in range(iteracoes):
        print(atual)
        atual = atual.prox

