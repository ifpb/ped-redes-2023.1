from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = nome


if __name__ == '__main__':
    f = Funcionario("José")
    print(f.nome)

