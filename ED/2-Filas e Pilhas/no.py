class No:
    def __init__(self, carga, prox=None):
        self.__carga = carga
        self.__prox = prox

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, prox):
        self.__prox = prox

    def __str__(self):
        return "%s -> %s" % (self.__carga, self.__prox)
