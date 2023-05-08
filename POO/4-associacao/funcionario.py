"""
Funcionario;
- nome: str
- endereco: Endereco
- matricula : str
- estado_civil: EstadoCivil
- telefone: str
- funcoes: Funcao[]
- salario_base: float
"""
from enum import Enum


class EstadoCivil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viúvo"


class Funcao:
    def __init__(self, nome, bonus_salario):
        self.nome = nome
        self.bonus_salario = bonus_salario

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Bônus Salário: R$ {self.bonus_salario:.2f}
        """


class Endereco:
    def __init__(self, rua, cidade, numero, estado, pais):
        self.rua = rua
        self.cidade = cidade
        self.numero = numero
        self.estado = estado
        self.pais = pais

    def __str__(self):
        return f"""
        Rua: {self.rua}, Cidade: {self.cidade}, Número: {self.numero}, Estado: {self.estado}, País: {self.pais}
        """


class Funcionario:
    def __init__(self, nome, endereco, matricula, estado_civil, telefone, salario_base):
        self.nome = nome
        self.endereco = endereco
        self.matricula = matricula
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.salario_base = salario_base
        self.__funcoes = []

    def calcular_salario_total(self):
        salario_total = self.salario_base
        for funcao in self.funcoes:
            salario_total += funcao.bonus_salario
        return salario_total

    def adicionar_funcao(self, funcao):
        self.__funcoes.append(funcao)

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Endereço: {self.endereco}
        Matrícula: {self.matricula}
        Estado Civil: {self.estado_civil}
        Telefone: {self.telefone}
        Salario Base: {self.salario_base}
        """

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
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def funcoes(self):
        return self.__funcoes

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

if __name__ == '__main__':
    endereco = Endereco("Rua Primeiro de Maio", "João Pessoa", "321", "Paraíba", "Brasil")
    f = Funcionario("Mary Roberta", endereco, "231232132", EstadoCivil.CASADO, "83 923092323", 5000)
    funcao1 = Funcao("Professora", 1000)
    funcao2 = Funcao("Reitora", 2000)
    funcao3 = Funcao("Conselho Superior", 1500)
    f.adicionar_funcao(funcao1)
    f.adicionar_funcao(funcao2)
    f.adicionar_funcao(funcao3)
    print(f)
    print(f"Salário Total {f.calcular_salario_total():.2f}")
