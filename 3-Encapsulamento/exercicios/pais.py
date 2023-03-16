class Pais:
    def __init__(self, nome, capital, dimensao):
        self.nome = nome
        self.capital = capital
        self.dimensao = dimensao
        self.__paises_fronteira = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def capital(self):
        return self.__capital
    
    @capital.setter
    def capital(self, capital):
        self.__capital = capital

    @property
    def dimensao(self):
        return self.__dimensao
    
    @dimensao.setter
    def dimensao(self, dimensao):
        assert type(dimensao) == int or type(dimensao) == float, "Dimensão precisa ser inteiro ou float"
        self.__dimensao = dimensao

    @property
    def paises_fronteira(self):
        return self.__paises_fronteira

    def adiciona_pais_fronteira(self, pais):
        if pais not in self.paises_fronteira:
            self.paises_fronteira.append(pais)
    
    def __str__(self):
        return f"""
        Nome: {self.nome},
        Dimensão: {self.dimensao}
        Países que fazem fronteira: {self.paises_fronteira}
        """

if __name__ == '__main__':
    pais = Pais("Brasil", "Brasília", 3300000)
    pais.adiciona_pais_fronteira("Argentina")
    pais.adiciona_pais_fronteira("Argentina")
    pais.adiciona_pais_fronteira("Paraguai")
    pais.adiciona_pais_fronteira("Uruguai")
    pais.adiciona_pais_fronteira("Peru")
    pais.adiciona_pais_fronteira("Colombia")
    pais.adiciona_pais_fronteira("Bolivia")
    pais.adiciona_pais_fronteira("Venezuela")
    pais.adiciona_pais_fronteira("Guiana Francesa")
    pais.adiciona_pais_fronteira("Guiana")
    pais.adiciona_pais_fronteira("Suriname")
    print(pais)
