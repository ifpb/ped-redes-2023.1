class Filme:
    def __init__(self, id, titulo, preço):  # construtor
        self.__id = id
        self.__titulo = titulo
        self.__nota = None
        self.__preco = preço

    @property
    def id(self):
        return self.__id

    @property
    def titulo(self):
        return self.__titulo

    @property
    def nota(self):
        return self.__nota

    @property
    def preço(self):
        return self.__preco

    # criar um método "set"
    @id.setter
    def id(self, id):
        self.__id = id

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @preço.setter
    def preço(self, preco):
        self.reajustar_preco(preco)

    def reajustar_preco(self, preco):
        assert type(preco) == int or type(preco) == float, "preço deve ser int ou float"
        assert preco >= 0, "O preço deve ser maior ou igual a zero"
        if preco < 0:
            self.__preco = 0
        else:
            self.__preco = preco

    def avaliar(self, nota):
        # nota de 1...5
        assert type(nota) == float or type(nota) == int, "nota deve ser um float ou int"
        assert 0 <= nota <= 5, "nota deve ser um número entre 0 e 5"
        self.__nota = nota

    def __str__(self):
        return f'{self.__id} - {self.__titulo} - nota: {self.__nota}, preço = {self.__preco}'


class FilmeInexistente(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class IdJaUtilizado(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class FilmeJaCadastrado(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class PlataformaStreaming:
    def __init__(self, titulo):
        self.titulo = titulo
        self.catalogo = []

    def __checar_filme_existente(self, filme):
        for f in self.catalogo:
            if f.id == filme.id:
                raise IdJaUtilizado("Já existe um outro filme com o id " + str(filme.id))
            if f.titulo == filme.titulo:
                raise FilmeJaCadastrado("O filme "+filme.titulo+" já está cadastrado no catálogo com o id " + str(f.id))

    def cadastrar_filme(self, filme: Filme):
        self.__checar_filme_existente(filme)
        self.catalogo.append(filme)

    def pesquisar_filme(self, id):
        filme = None
        for f in self.catalogo:
            if f.id == id:
                filme = f
        if filme is None:
            raise FilmeInexistente("Filme com id " + str(id) + " não existe no catálogo!")
        return filme

    def listar_filmes(self):
        for f in self.catalogo:
            print(f)

    def avaliar_filme(self, id, nota):
        for f in self.catalogo:
            if f.id == id:
                f.avaliar(nota)
                return

    def reajustar_preco(self, id, novoPreço):
        filme = self.pesquisar_filme(id)
        filme.reajustar_preco(novoPreço)
