import random
def lista_numeros_aleatorios(qtd=10):
    lista = random.sample(range(0,9999), qtd)
    return lista