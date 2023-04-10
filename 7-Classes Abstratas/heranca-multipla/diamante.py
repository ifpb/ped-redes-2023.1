from abc import ABC, abstractmethod


class ClassXPTO(ABC):

    @abstractmethod
    def m10(self):
        pass


class ClassA(ABC):
    def m1(self):
        print("implementação da ClassA")
        print(f"{self.__class__.__name__} - m1")

    @abstractmethod
    def m2(self):
        pass


class ClassX:
    def m2(self):
        print("M2 da classe X")

    def m10(self):
        print("M10 da classe X")


class ClassB(ClassA):

    def m3(self):
        print("m3")


class ClassC(ClassA):
    def m2(self):
        print("M2 da classe C")

    def m4(self):
        print("m4")


class ClassBA(ClassA):
    def m2(self):
        print("M2 da classe BA")

    def m5(self):
        print("m5")


class ClassD(ClassB, ClassC, ClassBA):
    def m2(self):
        super().m2()


if __name__ == '__main__':
    # ca = ClassA()
    # ca.m1()

    # cb = ClassB()
    # cb.m2()

    # cc = ClassC()
    # cc.m2()

    # dd = ClassD()
    # dd.m2()

    # print(ClassD.__mro__)
    ClassA.register(ClassX)
    ClassXPTO.register(ClassX)

    cx = ClassX()
    cx.m2()
    cx.m10()
    print(isinstance(cx, ClassA))
    print(issubclass(ClassX, ClassA))
    print(isinstance(cx, ClassXPTO))
    print(issubclass(ClassX, ClassXPTO))