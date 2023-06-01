def busca_binaria(lista, ip):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio].ip == ip:
            return lista[meio].nome
        elif lista[meio].ip < ip:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

def busca_binaria_recursiva(lista, ip, resultados=[]):
    if len(lista) == 0:
        return -1
    meio = len(lista) // 2
    if lista[meio].ip == ip:
        return lista[meio].nome
    elif lista[meio].ip < ip:
        return busca_binaria_recursiva(lista[meio+1:], ip)
    else:
        return busca_binaria_recursiva(lista[:meio], ip)