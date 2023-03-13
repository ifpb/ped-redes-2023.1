class Calculadora:
    # ----------- Construtor ------------ #
    def __init__(self, registrador: float = 0.0):
        self.nome = "Calculadora"
        self.__registrador = registrador
        self.__anterior = self.__registrador

    # ------------ Destrutor ------------ #
    def __del__(self):
        print(f'Objeto com endereço de memória {hex(id(self))} deletado.')

    # ------------- Getters ------------- #
    @property
    def registrador(self):
        return self.__registrador
    
    def criar_atributo_extra(self):
        self.extra = 123

    def faca_acao(self):
        if hasattr(self, 'extra'):
            print("ACAO EXTRA")
        else:
            print("ACAO NORMAL")

    # ---------- Magic Methods ---------- #
    def __str__(self):
        return f"Total: {self.__registrador}"

    # ------ Funções da Calculadora ----- #
    def adicionar(self, valor: float):
        self.__guardar_anterior()
        self.__registrador += valor

    def subtrair(self, valor: float):
        self.__guardar_anterior()
        self.__registrador -= valor

    def dividir(self, valor: float):
        self.__guardar_anterior()
        try:
          self.__registrador /= valor
        except ZeroDivisionError:
          self.__registrador = 0.0

    def multiplicar(self, valor: float):
        self.__guardar_anterior()
        self.__registrador *= valor

    def exibir(self):
        print(self.__registrador)

    def resetar(self):
        self.__guardar_anterior()
        self.__registrador = 0.0

    def desfazer(self):
        self.__registrador, self.__anterior = self.__anterior, self.__registrador

    # ------- Métodos Auxiliares -------- #
    def __guardar_anterior(self):
        self.__anterior = self.__registrador


if __name__ == '__main__':
    calculadora = Calculadora()
    operacao = None
    while True:
        print("+--------------+",
                f"|{calculadora.registrador: >13} |",
                "+--------------+",
                "(+) somar",
                "(-) subtrair",
                "(/) dividir",
                "(*) multiplicar",
                "(r) resetar",
                "(d) desfazer",
                "(exit) sair",
                "---------------",
                sep='\n')

        operacao = input("Operação: ")

        if operacao == '+':
            valor = float(input("Valor: "))
            calculadora.adicionar(valor)
            continue

        elif operacao == '-':
            valor = float(input("Valor: "))
            calculadora.subtrair(valor)
            continue

        elif operacao == '/':
            valor = float(input("Valor: "))
            calculadora.dividir(valor)
            continue

        elif operacao == '*':
            valor = float(input("Valor: "))
            calculadora.multiplicar(valor)
            continue

        elif operacao == 'r':
            calculadora.resetar()
            continue

        elif operacao == 'd':
            calculadora.desfazer()
            continue

        elif operacao == 'exit':
            break

        else:
            print('Operação inválida. Veja as opções disponíveis no menu.')

    print(calculadora.__dict__)
    print(Calculadora.__name__)
    print(Calculadora.__module__)
    print(hasattr(calculadora, 'registrador'))
    print(hasattr(calculadora, 'aaaaa'))