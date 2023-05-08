class Lampada:
    def __init__(self, ligado, cor="Branca"):
        self.ligado = ligado
        self.cor = cor

    def esta_ligada(self):
        return self.ligado
    
    def esta_desligada(self):
        return not self.ligado
    
    def mudar_cor(self, cor):
        self.cor = cor

    def __str__(self):
        return f"Está ligada = {self.esta_ligada()}, cor = {self.cor}"