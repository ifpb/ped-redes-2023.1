from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def calcula_area(self):
        """calcula área de uma forma geométrica
        Returns:
            float|int: resultado do cálculo da área
        """
        pass


class FormaComBaseEAltura(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base):
        assert type(base) == int or type(base) == float, "Base deve ser um número"
        self.__base = base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        assert type(altura) == int or type(altura) == float, "Altura deve ser um número"
        self.__altura = altura

    def calcula_area(self):
        return self.base * self.altura


class Retangulo(FormaComBaseEAltura):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)


class Triangulo(FormaComBaseEAltura):
    def __init__(self, base, altura) -> None:
        super().__init__(base, altura)

    def calcula_area(self):
        return (self.base * self.altura) / 2


class Trapezio(FormaComBaseEAltura):
    def __init__(self, base, altura, base_maior) -> None:
        super().__init__(base, altura)
        self.base_maior = base_maior

    @property
    def base_maior(self):
        return self.__base_maior

    @base_maior.setter
    def base_maior(self, base_maior):
        assert type(base_maior) == int or type(base_maior) == float, "Base maior deve ser um número"
        assert base_maior > self.base, "A base maior precisa ser maior do que a base menor"
        self.__base_maior = base_maior

    def calcula_area(self):
        return ((self.base_maior + self.base) * self.altura) / 2


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        assert type(raio) == int or type(raio) == float, "Raio deve ser um número"
        self.__raio = raio

    def calcula_area(self):
        return math.pi * math.pow(self.raio, 2)


class Hexagono(FormaGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcula_area(self):
        return 6 * self.lado ** 2 / (4 * math.tan(math.pi / 6))


class Cilindro(FormaGeometrica):
    def __init__(self, raio, altura):
        super().__init__()
        self.raio = raio
        self.altura = altura

    def calcula_area(self):
        return 2 * math.pi * self.raio * (self.raio + self.altura)


try:
    c = Circulo(10)
    ti = Triangulo(30, 50)
    r = Retangulo(10, 20)
    ta = Trapezio(10, 20, 30)
    h = Hexagono(10)
    cil = Cilindro(10, 20)

    for f in [c, ti, r, ta, h, cil]:
        print(f"Aréa do {f.__class__.__name__} = {f.calcula_area()}")

except AssertionError as e:
    print(e)
