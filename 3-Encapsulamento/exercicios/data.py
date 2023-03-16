class Data:
    def __init__(self, dia=1, mes=1, ano=2023):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        assert type(dia) == int, "Dia precisa ser um número inteiro"
        assert dia > 0 and dia <= 31, "Dia precisa ser maior do que zero e menor ou igual a 31"
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        assert type(mes) == int, "Mês precisa ser um número inteiro"
        assert mes > 0 and mes <= 12, "Mês precisa ser um número entre 1 e 12"
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        assert type(ano) == int, "Ano precisa ser um número inteiro"
        assert ano > 0 and ano < 3000, "Ano precisa ser um número entre 1 e 3000"
        self.__ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    

if __name__ == '__main__':
    d = Data(10)
    d = Data(10, 2)
    d = Data(10, 2, 2023)

    print("Data = ", d)