from typing import List
from lista_numeros_aleatorios import lista_numeros_aleatorios

def selection_sort_alg(vetor: List):
    for i in range(len(vetor)):
        pos_menor = i
        menor = vetor[i]
        for j in range(i+1, len(vetor)):
            if vetor[j] < menor:
                menor = vetor[j]
                pos_menor = j
        vetor[pos_menor] = vetor[i]
        vetor[i] = menor

if __name__ == '__main__':
    lista = lista_numeros_aleatorios(900)
    selection_sort_alg(lista)
    import timeit
    print(lista)
    print(timeit.timeit("lista=lista_numeros_aleatorios(900); selection_sort_alg(lista)", setup="from __main__ import selection_sort_alg; from __main__ import lista_numeros_aleatorios", number=1000))
