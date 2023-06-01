from typing import List
from lista_numeros_aleatorios import lista_numeros_aleatorios

def bubble_sort_alg(vetor):
    trocou: bool = True
    elementos: int = len(vetor) - 1
    while trocou:
        trocou = False
        for i in range(elementos):
            if vetor[i] > vetor[i + 1]:
                trocou = True
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]


if __name__ == '__main__':
    lista = lista_numeros_aleatorios(900)
    print("lista desordenada = ", lista)
    bubble_sort_alg(lista)
    print("lista ordenada = ", lista)
    import timeit

    print(timeit.timeit("lista=lista_numeros_aleatorios(900); bubble_sort_alg(lista)",
                        setup="from __main__ import bubble_sort_alg; from __main__ import lista_numeros_aleatorios",
                        number=1000))