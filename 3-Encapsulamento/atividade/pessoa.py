"""
1. Cria uma Classe Pessoa, contendo os atributos encapsulados, com seus respectivos seletores (getters) e modificadores (setters),
e ainda o construtor padrão e pelo menos mais duas opções de construtores conforme sua percepção.

Atributos: String nome; String endereço; String telefone;
"""


class Pessoa:
    def __init__(self, nome, endereco="", telefone=""):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Endereço: {self.endereco}
        Telefone: {self.telefone}
        """


if __name__ == '__main__':
    p1 = Pessoa("Diego")
    p2 = Pessoa("Maria", "Rua Movimentada")
    p3 = Pessoa("João", "Rua da silva", "83 99923-2312")
    print(p1, p2, p3)