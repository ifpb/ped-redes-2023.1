from ordenacao import servidores_dns
from busca_binaria import *
from busca_sequencial import *

if __name__ == '__main__':
    print("Entrada: ")
    for servidor in servidores_dns:
        print(servidor)

    ip = input("Digite o IP do servidor que deseja buscar")
    resultado = busca_sequencial(servidores_dns, ip)
    print(resultado)
    resultado = busca_sequencial_recursiva(servidores_dns, ip)
    print(resultado)
    resultado = busca_binaria(servidores_dns, ip)
    print(resultado)
    resultado = busca_binaria_recursiva(servidores_dns, ip)
    print(resultado)
