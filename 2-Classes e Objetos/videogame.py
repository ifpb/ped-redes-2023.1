from datetime import datetime

class Videogame:

    __ULTIMO_NUM_SERIE = 0

    def __init__(self, data_fabricacao=None, marca="", modelo=""):
        if data_fabricacao == None:
            self.data_fabricacao = datetime.today()
        else:
            self.data_fabricacao = datetime.strptime(data_fabricacao, '%d/%m/%Y')
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 50
        self.jogos_instalados = []
        self.anos_garantia = 1
        self.numero_serie = self.obter_num_serie()
        self.incrementar_num_serie()

    def obter_num_serie(self):
        return self.__class__.__ULTIMO_NUM_SERIE + 1
    
    def incrementar_num_serie(self):
        self.__class__.__ULTIMO_NUM_SERIE += 1

    def instalar_jogo(self, jogo):
        self.jogos_instalados.append(jogo)

    def __str__(self):
        return f"""
        Marca: {self.marca}, modelo: {self.modelo}, 
        Fabricação: {self.data_fabricacao.strftime('%d/%m/%Y')}, 
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