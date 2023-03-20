"""
Crie uma classe Elevador para armazenar as informações de um elevador de prédio.
A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo),
    capacidade do elevador e quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
    Inicializar: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
    Entrar: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    Sair: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    Subir: para subir um andar (não deve subir se já estiver no último andar);
    Descer: para descer um andar (não deve descer se já estiver no térreo);
Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).
"""


class Elevador:

    # Contempla o método Inicializar pedido
    def __init__(self, total_andares, capacidade):
        self.total_andares = total_andares
        self.capacidade = capacidade
        self.andar_atual = 0
        self.pessoas_presentes = 0

    def entrar(self):
        # assert self.pessoas_presentes < self.capacidade, "Não há mais espaço no elevador"
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
        else:
            print("Não há mais espaço no elevador")

    def sair(self):
        if self.pessoas_presentes >= 1:
            self.pessoas_presentes -= 1
        else:
            print("Não é possível sair mais ninguém. O elevador já está vazio")

    def subir(self):
        # assert self.andar_atual < self.total_andares, "Não há mais andar para subir"
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print("Não há mais andar para subir")

    def descer(self):
        # assert self.andar_atual > 0, "Não há mais andar para descer"
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print("Não há mais andar para descer")

    @property
    def total_andares(self):
        return self.__total_andares

    @total_andares.setter
    def total_andares(self, total_andares):
        self.__total_andares = total_andares

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def andar_atual(self):
        return self.__andar_atual

    @andar_atual.setter
    def andar_atual(self, andar_atual):
        self.__andar_atual = andar_atual

    @property
    def pessoas_presentes(self):
        return self.__pessoas_presentes

    @pessoas_presentes.setter
    def pessoas_presentes(self, pessoas_presentes):
        self.__pessoas_presentes = pessoas_presentes

    def __str__(self):
        return f"""
        Total Andares: {self.total_andares}
        Andar Atual: {self.andar_atual}
        Capacidade Máxima: {self.capacidade}
        Pessoas Presentes: {self.pessoas_presentes}
        """


if __name__ == '__main__':
    andares = 10
    max_pessoas = 8
    elevador = Elevador(andares, max_pessoas)
    print(elevador)
    elevador.entrar()
    print(elevador)
    elevador.entrar()
    print(elevador)
    elevador.entrar()
    print(elevador)
    elevador.entrar()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.subir()
    print(elevador)
    elevador.sair()
    print(elevador)
    elevador.sair()
    print(elevador)
    elevador.sair()
    print(elevador)
    elevador.descer()
    print(elevador)
    elevador.descer()
    print(elevador)
    elevador.descer()
    print(elevador)
    elevador.descer()
    print(elevador)
