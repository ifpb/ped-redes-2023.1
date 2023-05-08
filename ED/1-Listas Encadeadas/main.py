from listacomposta import ListaComposta
from listaencadeada import ListaEncadeada
from listaencadeada_estendida import ListaEncadeadaEstendida
from listaencadeada_limitada import ListaLimitada
from listautils import ListUtils

if __name__ == '__main__':

    """ 
        Q1 
    """
    lista = ListaEncadeada()
    lista.inserir_no_inicio(8)
    lista.inserir_no_inicio(4)
    lista.inserir_no_inicio(7)
    lista.inserir_no_inicio(1)
    lista.inserir_no_inicio(5)
    lista.inserir_no_final(10)
    lista.remover_do_final()
    lista.inserir_no_inicio(50)
    lista.remover_do_inicio()
    print(lista)

    """ 
        Q2
    """
    l = ListaEncadeadaEstendida()
    l.inserir_no_final(2)
    l.inserir_no_final(22)
    l.inserir_no_final(44)
    l.inserir_no_final(13)
    l.inserir_no_final(1)
    l.inserir_no_final(44)
    print("Q2 - Elementos ")
    print(l)
    print("Q2 - Elementos Pares")
    print(l.pares())
    print("Q2 - elementos impares")
    print(l.impares())
    print(l.buscar_pos(2))

    print(l)
    print("remover elemento")
    l.remover_por_valor(13)
    print(l)

    print("remover ocorrencias")
    l.remover_ocorrencias(44)
    print(l)
    print("inserir em posição")
    l.inserir_pos(3, 999)
    print(l)
    print("remover de posição")
    l.remover_de_posicao(3)
    print(l)

    """ 
        Q3
    """
    print("#######")
    print("clonar")
    l2 = ListUtils.clonar(l)
    l.remover_do_final()
    print(l2)
    print("inverter")
    l3 = ListUtils.inverter(l)
    print(l3)
    print("join")
    ret = ListUtils.join(l2, ",")
    print(ret)
    print("split")
    l4 = ListUtils.split("2-0-3-8-2-0-3", "-")
    print(l4)
    print("intercalar")
    l5 = ListUtils.split("1-3-5-7-9-11-13-15-17-19", "-")
    l6 = ListUtils.split("0-2-4-6-8-10-12", "-")
    l7 = ListUtils.intercalar(l6, l5)
    print(l7)

    """ 
        Q4
    """
    print("#################")
    print("lista limitada")
    lim = ListaLimitada(4)
    lim.inserir_no_final(4)
    lim.inserir_no_final(5)
    lim.inserir_no_final(9)
    print(lim)
    try:
        lim = ListaLimitada(4)
        lim.inserir_no_final(4)
        lim.inserir_no_final(22)
        lim.inserir_no_final(11)
        lim.inserir_no_final(5)
        lim.inserir_no_final(9)
    except:
        print("Lista lotada!")

    """ 
        Q5
    """
    listaDeLista = ListaComposta()
    l1 = ListaEncadeadaEstendida()
    l1.inserir_no_inicio(22)
    l1.inserir_pos(0, 11)
    l1.inserir_no_final(33)
    l2 = ListaLimitada(5)
    l2.inserir_no_inicio(1)
    l2.inserir_no_inicio(2)
    l2.inserir_no_inicio(3)
    l2.inserir_no_inicio(4)
    l3 = ListaEncadeada()
    l3.inserir_no_final(100)
    l3.inserir_no_final(120)
    l3.inserir_no_final(140)
    l3.inserir_no_final(160)
    listaDeLista.inserir_no_final(l1)
    listaDeLista.inserir_no_final(l2)
    listaDeLista.inserir_no_final(l3)
    print("lista de lista: ")
    print(listaDeLista)
