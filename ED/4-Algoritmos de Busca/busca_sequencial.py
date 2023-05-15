def busca_sequencial(lista, ip):
    for i in range(len(lista)):
        if lista[i].ip == ip:
            return lista[i].nome
        if lista[i].ip > ip:
            return -1
    return -1

def busca_sequencial_recursiva(lista, ip, i=0):
    if i == len(lista) or lista[i].ip > ip:
        return -1
    if lista[i].ip == ip:
        return lista[i].nome
    return busca_sequencial_recursiva(lista, ip, i+1)