def busca_binaria_recursiva(lista, arquivo):
    if lista is None or len(lista) == 0:
        return -1
    meio = len(lista) // 2
    if lista[meio].carga.tamanho == arquivo.tamanho:
        return lista[meio].carga.tamanho
    elif lista[meio].carga.tamanho < arquivo.tamanho:
        return busca_binaria_recursiva(lista[meio+1:], arquivo)
    else:
        return busca_binaria_recursiva(lista[:meio], arquivo)

def busca_sequencial_recursiva(lista, arquivo, i=0):
    if i == len(lista) or lista[i].carga.tamanho > arquivo.tamanho:
        return -1
    if lista[i].carga.tamanho == arquivo.tamanho:
        return lista[i].carga.tamanho
    return busca_sequencial_recursiva(lista, arquivo, i+1)

