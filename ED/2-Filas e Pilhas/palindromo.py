from pilha import Pilha, PilhaVaziaException


def checa_palindromo(palavra):
    palavra = palavra.replace(" ", "")
    pilha1 = Pilha()
    for c in list(palavra):
        pilha1.push(c)

    pilha2 = Pilha()
    atual = pilha1.topo
    while atual is not None:
        pilha2.push(atual.carga)
        atual = atual.prox

    print(pilha1)
    print(pilha2)

    atual = pilha1.topo
    atual2 = pilha2.topo
    while atual is not None or atual2 is not None:
        if atual.carga != atual2.carga:
            return False
        atual = atual.prox
        atual2 = atual2.prox

    return True


if checa_palindromo("amor a roma"):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
