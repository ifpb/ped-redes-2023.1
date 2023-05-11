'''
Q1
'''


def contem_par(lista, c=0):
    if c >= len(lista):
        return False
    if lista[c] % 2 == 0:
        return True
    return contem_par(lista, c + 1)

def contem_par_v2(lista):
    if len(lista) == 0:
        return False
    if lista[0] % 2 == 0:
        return True
    return contem_par_v2(lista[1:])

'''
Q2
'''


def todos_impares(lista):
    if len(lista) == 0:
        return True
    if lista[0] % 2 == 0:
        return False
    return todos_impares(lista[1:])

'''
Q3
'''



def max(lista, maior=None, c=0):
    if len(lista) == 0:
        return -1
    if c >= len(lista):
        return maior
    if not maior:
        maior = lista[0]
    if lista[c] > maior:
        maior = lista[c]
    return max(lista, maior, c + 1)


def pos_max(lista, maior=None, maior_indice=0, c=0):
    if len(lista) == 0:
        return -1
    if c >= len(lista):
        return maior_indice
    if not maior:
        maior = lista[0]
    if lista[c] > maior:
        maior = lista[c]
        maior_indice = c
    return pos_max(lista, maior, maior_indice, c + 1)


'''
Q4
'''
def inverte_lista(lista):
    if len(lista) == 0:
        return lista
    else:
        return inverte_lista(lista[1:]) + [lista[0]]


'''
Q5
'''


def comparar_listas_iguais(lista1, lista2):
    # Se ambas as listas estiverem vazias, elas são iguais
    if not lista1 and not lista2:
        return True

    # Se apenas uma das listas estiver vazia, elas não são iguais
    if not lista1 or not lista2:
        return False

    # Se os primeiros elementos das listas forem diferentes, elas não são iguais
    if lista1[0] != lista2[0]:
        return False

    # Recursivamente compara as sublistas restantes
    return comparar_listas_iguais(lista1[1:], lista2[1:])


'''
Q6
'''
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

'''
Q7
'''
def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

'''
Q8
'''
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente-1)

'''
Q9
'''
def contagem_regressiva(n):
    if n == 0:
        print("Fogo!")
    else:
        print(n)
        contagem_regressiva(n-1)

'''
Q10
'''
def inverte_string(s):
    if len(s) == 0:
        return s
    else:
        return inverte_string(s[1:]) + s[0]


print("pos max")
print(max([1, 2, 3, 4, 100, 1, 2]))
print(pos_max([1, 2, 3, 4, 100, 1, 2]))

print("Contem par")
lista_pares = [1, 2, 3, 4, 5, 6, 10]
print(contem_par_v2(lista_pares))
print("lista pares")
print(lista_pares)
print("Todos ímpares")
lista = [1, 2, 3, 4, 5, 6, 10]
print(todos_impares(lista))
print("lista impares")
lista_impares = [1, 1, 3, 7, 9, 11, 13]
print(todos_impares(lista_impares.copy()))
print(lista_impares)
print("inverte lista")
lista = [1, 2, 3, 4, 5, 6]
print(inverte_lista(lista))
print("Comparar listas iguais")
print("Listas iguais = ", comparar_listas_iguais([1, 2, 3], [1, 2, 3]))
print("Fatorial")
print(fatorial(5))
print("Soma lista")
print(soma_lista([1, 2, 3, 4, 5]))
print("Potência")
print(potencia(4, 2))
print("Contagem regressiva")
print(contagem_regressiva(4))
print("Inverter string")
print(inverte_string("teste"))
