class Ingresso:
    def __init__(self, valor):
        self._valor = valor

    def calcular_valor(self):
        return self._valor


class IngressoCaro:
    def __init__(self):
        self._valor = 9999


class IngressoVIP(Ingresso, IngressoCaro):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self._valor += adicional


if __name__ == '__main__':
    ing = Ingresso(30)
    ingVip = IngressoVIP(30, 5)
    print(ing.calcular_valor(), ingVip.calcular_valor())
