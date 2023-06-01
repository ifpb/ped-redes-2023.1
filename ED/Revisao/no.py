class No:
    def __init__(self, carga: object = None,
                 ant: 'No' = None,
                 prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return str(self.carga)