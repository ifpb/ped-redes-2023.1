lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

indice_meio = len(lista) / 2
lista[indice_meio]



lista[5]
def imprimir_primeiro_elemento(lista):
    print(lista[0]) ## O(1)

def percorrer_lista(lista): ## O(n)
    c = 0
    for item in lista:
        print(item)
        c += 1
    print("Total de iterações:", c)


def imprimir_pares_de_elementos(lista): ## O(n^2)
    c = 0
    for i in lista:
        for j in lista:
            print(f"{i}-{j}")
            c += 1
    print("Tamanho da lista: ", len(lista))
    print("Total de iterações:", c)



# imprimir_primeiro_elemento(lista)
# percorrer_lista(lista)
imprimir_pares_de_elementos(lista)
