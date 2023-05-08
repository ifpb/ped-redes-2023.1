import re


class SaldoInsuficiente(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class LimiteChequeEspecialExcedente(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class ContaBancaria:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        numero = numero.upper()
        assert re.match(r'^\d{1,5}-[\d|X]$', numero), "Numero da conta deve ter no maximo 7 digitos, " \
                                                      "com os 5 primeiros dígitos contendo apenas números, " \
                                                      "o 6º dígito sendo um hífen e " \
                                                      "o último dígito sendo um número ou a letra x"
        # assert len(numero) <= 7, "Numero da conta deve ter no maximo 7 digitos"
        # assert numero != "", "Numero da conta nao pode ser vazio"
        # assert numero[:5].isnumeric(), "5 primeiros dígitos da conta devem conter apenas números"
        # assert numero[5] == '-', "6º dígito da conta deve ser um hífen"
        # assert numero[6].isnumeric() or numero[6] == 'x', "último dígito da conta devem conter um número ou a letra x"
        self.__numero = numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        assert type(saldo) == int or type(saldo) == float, "Saldo da conta deve ser um número"
        assert saldo >= 0, "Saldo da conta nao pode ser negativo"
        self.__saldo = saldo

    def __str__(self):
        return f"Conta: {self.numero} Saldo: R$ {self.saldo:.2f}"


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self.__taxa_juros

    @taxa_juros.setter
    def taxa_juros(self, taxa_juros):
        assert type(taxa_juros) == int or type(taxa_juros) == float, "Taxa de juros deve ser um número"
        assert 0 <= taxa_juros <= 1, "Taxa de juros deve ser um número entre 0 e 1"
        self.__taxa_juros = taxa_juros

    def calcular_ganho_anual(self):
        return self.saldo * self.taxa_juros

    def __str__(self):
        return f"Conta: {self.numero} Saldo: R$ {self.saldo:.2f} Taxa de juros: {self.taxa_juros * 100:.2f}% " \
               f"Ganho anual: R$ {self.calcular_ganho_anual():.2f}"


class ContaCorrente(ContaBancaria):
    __MAX_CHEQUE_ESPECIAL = 1000.00

    def __init__(self, numero, saldo, limite):
        super().__init__(numero, saldo)
        self.limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        assert type(limite) == int or type(limite) == float, "Limite da conta deve ser um número"
        assert limite >= 0, "Limite da conta nao pode ser negativo"
        if limite > ContaCorrente.__MAX_CHEQUE_ESPECIAL:
            raise LimiteChequeEspecialExcedente(f"Limite da conta nao pode ser maior que R$ "
                                                f"{self.__class__.__MAX_CHEQUE_ESPECIAL:.2f}")
        self.__limite = limite

    def sacar(self, valor):
        assert valor >= 0, "Valor do saque deve ser maior que zero"
        if valor > self.saldo + self.limite:
            raise SaldoInsuficiente("Saldo insuficiente")
        if valor > self.saldo:
            saldo_anterior = self.saldo
            self.saldo = max(0, self.saldo - valor)
            self.limite -= valor - saldo_anterior
        else:
            self.saldo -= valor

    def depositar(self, valor):
        assert valor >= 0, "Valor do deposito deve ser maior que zero"
        self.saldo += valor

    def __str__(self):
        return f"Conta: {self.numero} Saldo: R$ {self.saldo:.2f} Limite: R$ {self.limite:.2f}"


if __name__ == '__main__':
    try:
        conta_corrente = ContaCorrente('12345-9', 1000, 500)
        conta_corrente.sacar(1000)
        print(conta_corrente)

        conta_poupanca = ContaPoupanca('12345-6', 1000, 0.05)
        print(conta_poupanca)

    except AssertionError as a:
        print(a)
    except SaldoInsuficiente as s:
        print(s)
    except LimiteChequeEspecialExcedente as l:
        print(l)
