from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio * self.raio

    def perimetro(self):
        return 2 * 3.14 * self.raio


retangulo = Retangulo(4, 5)
# print("Área do retângulo:", r.area())
# print("Perímetro do retângulo:", r.perimetro())

circulo = Circulo(3)
# print("Área do círculo:", c.area())
# print("Perímetro do círculo:", c.perimetro())


formas = [retangulo, circulo]

for forma in formas:
    print("Área da forma:", forma.area())
    print("Perímetro da forma:", forma.perimetro())