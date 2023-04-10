from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, endereco, telefone):
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


class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, telefone, valor_credito, valor_divida) -> None:
        super().__init__(nome, endereco, telefone)
        self.valor_credito = valor_credito
        self.valor_divida = valor_divida

    @property
    def valor_credito(self):
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        assert type(valor_credito) == int or type(valor_credito) == float, "valor do cré]dito deve ser um número"
        self.__valor_credito = valor_credito

    @property
    def valor_divida(self):
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_divida):
        assert type(valor_divida) == int or type(valor_divida) == float, "valor da dívida deve ser um número"
        self.__valor_divida = valor_divida

    def obter_saldo(self):
        return self.valor_credito - self.valor_divida


class Empregado(Pessoa):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, comissao) -> None:
        super().__init__(nome, endereco, telefone)
        self.codigo_setor = codigo_setor
        self.salario_base = salario_base
        self.imposto = imposto
        self.comissao = comissao

    @property
    def codigo_setor(self):
        return self.__codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        assert type(codigo_setor) == int, "código do setor deve ser um inteiro"
        self.__codigo_setor = codigo_setor

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        assert type(salario_base) == int or type(salario_base) == float, "salário base deve ser um número"
        self.__salario_base = salario_base

    @property
    def imposto(self):
        return self.__imposto

    @imposto.setter
    def imposto(self, imposto):
        assert type(imposto) == float and 0 <= imposto <= 1, "imposto deve ser um float entre 0 e 1"
        self.__imposto = imposto

    @property
    def comissao(self):
        return self.__comissao

    @comissao.setter
    def comissao(self, comissao):
        assert type(comissao) == float  and 0 <= comissao <= 1, "comissao deve ser um float entre 0 e 1"
        self.__comissao = comissao

    @abstractmethod
    def calcular_salario(self):
        return self.salario_base - (self.salario_base * self.imposto)


class Operario(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, comissao, valor_producao) -> None:
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto, comissao)
        self.valor_producao = valor_producao

    @property
    def valor_producao(self):
        return self.__valor_producao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao

    def calcular_salario(self):
        return super().calcular_salario() + (self.comissao * self.valor_producao)


class Vendedor(Empregado):
    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, comissao, valor_vendas) -> None:
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto, comissao)
        self.valor_vendas = valor_vendas

    @property
    def valor_vendas(self):
        return self.__valor_vendas

    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        assert type(valor_vendas) == int or type(valor_vendas) == float, "valorVendas deve ser um número"
        self.__valor_vendas = valor_vendas

    def calcular_salario(self):
        return super().calcular_salario() + (self.comissao * self.valor_vendas)


if __name__ == '__main__':
    f = Fornecedor("Coca cola", "Los Angeles US", "12012131", 20000, 5000)
    print("Fornecedor =", f.nome)
    print("Saldo =", f.obter_saldo())

    o = Operario("Joao", "Rua boa", "998238283", 1, 900.00, 0.2, 0.2, 2000)
    v = Vendedor("Joao", "Rua boa", "998238283", 1, 1500.00, 0.2, 0.5, 3000.00)
    for p in [o, v]:
        print(f"Salário do {p.__class__.__name__} = {p.calcular_salario():.2f}")
