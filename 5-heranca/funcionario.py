from enum import Enum


class SalarioMenorQueOMinimo(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Funcionario:

    SALARIO_MINIMO = 1212.00

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def adiciona_aumento(self, valor):
        self.salario += valor

    def ganho_anual(self):
        return self.salario * 12

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        assert type(salario) == float or type(salario) == int, "O valor do salário deve ser float ou int"
        if salario < Funcionario.SALARIO_MINIMO:
            raise SalarioMenorQueOMinimo("Salário não pode ser menor do que o mínimo "+str(Funcionario.SALARIO_MINIMO))
        self.__salario = salario

    def exibe_dados(self):
        return f"""
        Nome: {self.nome}
        Salário: R$ {self.salario:.2f}
        Ganho Anual: R$ {self.ganho_anual():.2f}"""


class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def exibe_dados(self):
        return super().exibe_dados() + f"""
        Matrícula: {self.matricula}
        """

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        assert len(matricula) <= 16, "Matrícula deve ter menos que 16 caracteres"
        self.__matricula = matricula


class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, salario, matricula, bonus_salarial):
        super().__init__(nome, salario, matricula)
        self.bonus_salarial = bonus_salarial
        self.salario += bonus_salarial

    @property
    def bonus_salarial(self):
        return self.__bonus_salarial
    
    @bonus_salarial.setter
    def bonus_salarial(self, bonus_salarial):
        assert type(bonus_salarial) == int or type(bonus_salarial) == float, "Bônus salarial deve ser do tipo int ou float"
        assert bonus_salarial >= 0, "Bônus deve ser maior ou igual a zero"
        self.__bonus_salarial = bonus_salarial


class Turno(Enum):
    DIA = 'Dia'
    NOITE = 'Noite'


class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
        self.salario += self.adicional_noturno if self.turno == Turno.NOITE else 0

    @property
    def adicional_noturno(self):
        return self.__adicional_noturno

    @adicional_noturno.setter
    def adicional_noturno(self, adicional_noturno):
        assert type(adicional_noturno) == int or type(adicional_noturno) == float, "adicional noturno deve ser int ou float"
        assert adicional_noturno >= 0, "adicional noturno deve ser um número positivo"
        self.__adicional_noturno = adicional_noturno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        assert type(turno) == Turno, "O turno deve ser um valor do enum Turno"
        self.__turno = turno


if __name__ == '__main__':
    try:
        assistente = Assistente("José", 1250, "312321")
        print(assistente.exibe_dados())

        assistente_tecnico = AssistenteTecnico("Técnico", 1500, "32424", Turno.NOITE, 150.00)
        print(assistente_tecnico.exibe_dados())

        assistente_administrativo = AssistenteAdministrativo("Administrativo", 1500, "23232", 50.0)
        print(assistente_administrativo.exibe_dados())
    except SalarioMenorQueOMinimo as e:
        print(e)
    except AssertionError as e:
        print(e)