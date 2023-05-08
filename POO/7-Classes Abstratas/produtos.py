from abc import ABC, abstractmethod


class Produto(ABC):
    @abstractmethod
    def preco(self):
        pass

    @abstractmethod
    def descricao(self):
        pass


class Tenis(Produto):
    def __init__(self, tamanho, cor, marca, preco):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
        self.preco_unitario = preco

    def preco(self):
        return self.preco_unitario

    def descricao(self):
        return f"{self.tamanho}, {self.cor}, {self.marca}"


class Camisa(Produto):
    def __init__(self, tamanho, cor, marca, preco):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
        self.preco_unitario = preco

    def preco(self):
        return self.preco_unitario

    def descricao(self):
        return f"{self.tamanho}, {self.cor}, {self.marca}"


class Calca(Produto):
    def __init__(self, tamanho, cor, marca, preco):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca
        self.preco_unitario = preco

    def preco(self):
        return self.preco_unitario

    def descricao(self):
        return f"{self.tamanho}, {self.cor}, {self.marca}"


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def preco_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco()
        return total


# Testar as classes
carrinho = CarrinhoDeCompras()

camisa1 = Camisa("P", "Azul", "Nike", 89.99)
camisa2 = Camisa("M", "Preto", "Adidas", 79.99)
calca1 = Calca("42", "Azul", "Levis", 119.99)

tenis = Tenis("43", "Branca", "Nike", 120.00)

carrinho.adicionar_produto(camisa1)
carrinho.adicionar_produto(camisa2)
carrinho.adicionar_produto(calca1)
carrinho.adicionar_produto(tenis)

print("Produtos no carrinho:")
for produto in carrinho.produtos:
    print(produto.descricao(), produto.preco())

print("Preço total: R$", carrinho.preco_total())
