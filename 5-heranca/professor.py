from abc import ABC


class Servidor(ABC):
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario
        self.descontos = 0
        self.__calcular_descontos()

    def __calcular_descontos(self):
        if self.salario > 10000:
            self.descontos = self.salario * 0.27 
        elif self.salario > 5000:
            self.descontos = self.salario * 0.15
        elif self.salario > 3000:
            self.descontos = self.salario * 0.07

    def imprimir_salario(self):
        print(f"Salário: R$ {self.salario:.2f}")

class Professor(Servidor):
    def __init__(self, nome, email, salario, disciplinas, ch):
        super().__init__(nome, email, salario)
        self.disciplinas = disciplinas
        self.ch = ch

class TecnicoAdministrativo(Servidor):
    def __init__(self, nome, email, salario, turno_trabalho):
        super().__init__(nome, email, salario)
        self.turno_trabalho = turno_trabalho

prof = Professor("Marcio", "marcio@ifpb.edu.br", 15000, ["Fund. de Redes"], 8)
print(f"Nome: {prof.nome}")
print(f"Email: {prof.email}")
prof.imprimir_salario()
print(f"Descontos: R${prof.descontos:.2f}")
print(f"Disciplinas: {prof.disciplinas}")
print(f"Carga-horária: {prof.ch} h/a")

ta = TecnicoAdministrativo("José da Silva", "jose@ifpb.edu.br", 10000, "manhã")
print(f"Nome: {ta.nome}")
print(f"Email: {ta.email}")
ta.imprimir_salario()
print(f"Descontos: R${ta.descontos:.2f}")
print(f"Turno de trabalho: {ta.turno_trabalho}")

servidor = Servidor("nome", "email@email.com", 10000)