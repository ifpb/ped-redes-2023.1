import timeit

from lista_numeros_aleatorios import lista_numeros_aleatorios


def quicksort(vetor):
    if len(vetor) <= 1: return vetor
    pivo = vetor[0]
    iguais = [x for x in vetor if x == pivo]
    menores = [x for x in vetor if x < pivo]
    maiores = [x for x in vetor if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


def main():
    vetor = lista_numeros_aleatorios(9999)
    print(vetor)
    vetor = quicksort(vetor)
    print("ordenado = ", vetor)


if __name__ == '__main__':
    main()
    print(timeit.timeit("lista=lista_numeros_aleatorios(900); quicksort(lista)",
                        setup="from __main__ import quicksort; from __main__ import lista_numeros_aleatorios",
                        number=1000))
