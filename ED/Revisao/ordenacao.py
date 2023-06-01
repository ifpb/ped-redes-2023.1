from servidores_dns import servidores_dns


def quicksort(vetor):
    if len(vetor) <= 1: return vetor
    pivo = vetor[0].ip
    iguais = [x for x in vetor if x.ip == pivo]
    menores = [x for x in vetor if x.ip < pivo]
    maiores = [x for x in vetor if x.ip > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


print("Nao-ordenada: ")
for servidor in servidores_dns:
    print(servidor)
servidores_dns = quicksort(servidores_dns)
print("Ordenada: ")
for servidor in servidores_dns:
    print(servidor)
