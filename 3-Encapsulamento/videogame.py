from datetime import datetime

class Videogame:

    __ULTIMO_NUM_SERIE = 0

    def __init__(self, data_fabricacao=None, marca="", modelo=""):
        if data_fabricacao == None:
            self.__data_fabricacao = datetime.today()
        else:
            self.__data_fabricacao = datetime.strptime(data_fabricacao, '%d/%m/%Y')
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidade_hd = 50
        self.__jogos_instalados = []
        self.__anos_garantia = 1
        self.__numero_serie = self.obter_num_serie()
        self.__incrementar_num_serie()

    @property
    def data_fabricacao(self):
        return self.__data_fabricacao.strftime('%d/%m/%Y')
    
    @data_fabricacao.setter
    def data_fabricacao(self, data):
        self.__data_fabricacao = datetime.strptime(data, '%d/%m/%Y')
    
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def capacidade_hd(self):
        return self.__capacidade_hd
    
    @capacidade_hd.setter
    def capacidade_hd(self, capacidade):
        assert type(capacidade).__name__ == 'int', "Capacidade precisa ser um número inteiro positivo"
        assert capacidade >= 0, "Capacidade precisa ser um número inteiro positivo"
        self.__capacidade_hd = capacidade
    
    @property
    def anos_garantia(self):
        return self.__anos_garantia
    
    @anos_garantia.setter
    def anos_garantia(self, anos):
        assert type(anos).__name__ == 'int', "Anos de garantia precisa ser um número inteiro positivo"
        assert anos <= 10 and anos >= 0, "Máximo de anos de garantia excedido"
        self.__anos_garantia = anos
    
    @property
    def numero_serie(self):
        return self.__numero_serie
    
    @property
    def jogos_instalados(self):
        return self.__jogos_instalados

    @staticmethod
    def validar_max_anos_garantia(anos):
        if anos > 10:
            print("Máximo de anos de garantia excedido")
        else:
            print("Garantia ok")

    @classmethod
    def obter_num_serie(cls):
        return cls.__ULTIMO_NUM_SERIE + 1
    
    @classmethod
    def __incrementar_num_serie(cls):
        cls.__ULTIMO_NUM_SERIE += 1

    def instalar_jogo(self, jogo):
        self.jogos_instalados.append(jogo)

    def __str__(self):
        return f"""
        Marca: {self.marca}, modelo: {self.modelo}, 
        Fabricação: {self.data_fabricacao}, 
        Capacidade: {self.capacidade_hd}, 
        Número de série: {self.numero_serie}, 
        Jogos Instalados: {self.jogos_instalados},
        Anos de garantia: {self.anos_garantia}
        """
    
v1 = Videogame('12/02/2020')
v1.modelo = "Switch"
v1.marca = "Nintendo"
v1.capacidade_hd = 64
v1.anos_garantia = 2
v1.instalar_jogo("Mario Kart")
v1.instalar_jogo("Super Mario World")
print(v1)

v2 = Videogame('12/04/2019', "XBOX", "360")
v2.capacidade_hd = 256
v2.anos_garantia = 3
v2.instalar_jogo("E-Sports 2023")
v2.instalar_jogo("Sonic")
print(v2)

v3 = Videogame()
v3.modelo = "5"
v3.marca = "Playstation"
v3.capacidade_hd = 512
v3.anos_garantia = 2
v3.instalar_jogo("Counter Strike")
v3.instalar_jogo("Final Fantasy XX")
print(v3)

print("Ultimo numero de serie: ", Videogame.obter_num_serie())
Videogame.validar_max_anos_garantia(9)