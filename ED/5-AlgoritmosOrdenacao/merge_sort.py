import timeit
from lista_numeros_aleatorios import lista_numeros_aleatorios


def merge(esquerda, direita, vetor):
    i, j, k = 0, 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            vetor[k] = esquerda[i]
            i, k = i + 1, k + 1
        else:
            vetor[k] = direita[j]
            j, k = j + 1, k + 1

    while i < len(esquerda):
        vetor[k] = esquerda[i]
        i, k = i + 1, k + 1

    while j < len(direita):
        vetor[k] = direita[j]
        j, k = j + 1, k + 1


def mergesort(vetor):
    if len(vetor) < 2: return vetor
    meio = len(vetor) // 2
    ## Divisão
    esquerda = vetor[:meio]
    direita = vetor[meio:]
    mergesort(esquerda)
    mergesort(direita)
    ## Combinação
    merge(esquerda, direita, vetor)


def main():
    vetor = lista_numeros_aleatorios(9999)
    print(vetor)
    mergesort(vetor)
    print("ordenado = ", vetor)


if __name__ == '__main__':
    main()
    print(timeit.timeit("lista=lista_numeros_aleatorios(900); mergesort(lista)",
                        setup="from __main__ import mergesort; from __main__ import lista_numeros_aleatorios",
                        number=1000))