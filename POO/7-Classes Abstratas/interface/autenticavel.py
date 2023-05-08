from abc import ABC, abstractmethod


class Autenticavel(ABC):

    @abstractmethod
    def autentica(self, login, senha):
        pass

    @abstractmethod
    def esta_autenticado(self):
        pass

class Presidente:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.autenticado = False

    def autentica(self, login, senha):
        if login == self.login and senha == self.senha:
            print('Acesso permitido')
            self.autenticado = True
        else:
            print('Acesso negado')

    def esta_autenticado(self):
        return self.autenticado

    def __str__(self):
        return f'Nome: {self.nome}'

class Gerente:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.autenticado = False

    def autentica(self, login, senha):
        if login == self.login and senha == self.senha:
            print('Acesso permitido')
            self.autenticado = True
        else:
            print('Acesso negado')

    def esta_autenticado(self):
        return self.autenticado

    def __str__(self):
        return f'Nome: {self.nome}'


class Diretor:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.autenticado = False

    def autentica(self, login, senha):
        if login == self.login and senha == self.senha:
            print('Acesso permitido')
            self.autenticado = True
        else:
            print('Acesso negado')

    def esta_autenticado(self):
        return self.autenticado

    def __str__(self):
        return f'Nome: {self.nome}'


if __name__ == '__main__':
    gerente = Gerente('João', 'joao', '123')
    diretor = Diretor('Maria', 'maria', '321')
    presidente = Presidente('José', 'jose', '456')

    gerente.autentica('joao', '123')
    diretor.autentica('maria', '321')
    presidente.autentica('jose', '456')

    print(gerente)
    print(diretor)
    print(presidente)

    Autenticavel.register(Gerente)
    Autenticavel.register(Diretor)
    Autenticavel.register(Presidente)

    funcionarios = [gerente, diretor, presidente]
    for funcionario in funcionarios:
        print("Está autenticado", funcionario.esta_autenticado()) # POLIMORFISMO

    print(isinstance(gerente, Autenticavel))
    print(isinstance(diretor, Autenticavel))
    print(issubclass(Gerente, Autenticavel))
    print(issubclass(Diretor, Autenticavel))