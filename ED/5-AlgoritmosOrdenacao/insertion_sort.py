from lista_numeros_aleatorios import lista_numeros_aleatorios


def insertion_sort_seq(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


def busca_binaria_recursiva(vetor, chave, primeiro=0, ultimo=None):
    if ultimo is None:
        ultimo = len(vetor) - 1

    if primeiro == ultimo:
        if vetor[primeiro] > chave:
            return primeiro
        else:
            return primeiro + 1
    if primeiro > ultimo:
        return primeiro

    meio = (primeiro + ultimo) // 2

    if chave < vetor[meio]:
        return busca_binaria_recursiva(vetor, chave, primeiro, meio)
    elif chave > vetor[meio]:
        return busca_binaria_recursiva(vetor, chave, meio + 1, ultimo)
    else:
        return meio

def insertion_sort_bin(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        loc = busca_binaria_recursiva(lista, chave)

        # Move os elementos maiores que a chave para uma posição
        # a mais do que a atual para abrir espaço
        while j >= loc:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

if __name__ == '__main__':
    lista = lista_numeros_aleatorios(900)
    insertion_sort_seq(lista)
    print(lista)
    import timeit

    print(timeit.timeit("lista=lista_numeros_aleatorios(900); insertion_sort_seq(lista)",
                        setup="from __main__ import insertion_sort_seq; from __main__ import lista_numeros_aleatorios",
                        number=1000))

    lista = lista_numeros_aleatorios(900)
    insertion_sort_bin(lista)
    print(lista)
    import timeit

    print(timeit.timeit("lista=lista_numeros_aleatorios(900); insertion_sort_bin(lista)",
                        setup="from __main__ import insertion_sort_bin; from __main__ import lista_numeros_aleatorios",
                        number=1000))


