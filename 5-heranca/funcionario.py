from enum import Enum


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def adiciona_aumento(self, valor):
        self.salario += valor

    def ganho_anual(self):
        return self.salario * 12

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
        self.__matricula = matricula


class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, salario, matricula, bonus_salarial):
        super().__init__(nome, salario, matricula)
        self.bonus_salarial = bonus_salarial
        self.salario += bonus_salarial


class Turno(Enum):
    DIA = 'Dia'
    NOITE = 'Noite'


class AssistenteTecnico(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
        self.salario += self.adicional_noturno if self.turno == Turno.NOITE else 0


if __name__ == '__main__':
    assistente = Assistente("José", 1500, "312321")
    print(assistente.exibe_dados())

    assistente_tecnico = AssistenteTecnico("Técnico", 1500, "32424", Turno.NOITE, 150.00)
    print(assistente_tecnico.exibe_dados())

    assistente_administrativo = AssistenteAdministrativo("Administrativo", 1500, "23232", 50.00)
    print(assistente_administrativo.exibe_dados())