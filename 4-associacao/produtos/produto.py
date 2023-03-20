class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"({self.codigo}) {self.descricao} - R${self.valor:.2f}"
