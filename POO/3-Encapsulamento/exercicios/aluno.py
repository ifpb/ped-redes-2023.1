class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.__matricula = matricula
        self.__notas = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def notas(self):
        return self.__notas
    
    def adiciona_nota(self, nota):
        assert type(nota) == int or type(nota) == float, "Nota precisa ser um número"
        assert nota >= 0 and nota <= 10, "Nota precisa ser um número entre 0 e 10"
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)
    
if __name__ == '__main__':
    a = Aluno("Petryck", "20221232324")
    a.adiciona_nota(4)
    a.adiciona_nota(8)
    a.adiciona_nota(9)
    print(f"Média = {a.media():.2f}")
