class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def __str__(self):
        return f"Produto: {self.produto}, Quantidade: {self.quantidade}"


class Pedido:
    def __init__(self):
        self.__valor_total = 0
        self.__itens_pedido = []

    def adicionar_item(self, item: ItemPedido):
        self.__itens_pedido.append(item)

    def __str__(self):
        # Necessário usar compreensão de listas para converter cada item em string para exibir o __str__ apropriadamente
        return f"""
        Itens: {[str(item) for item in self.__itens_pedido]}
        """

    def obter_total(self):
        # soma = 0
        # for item in self.__itens_pedido:
        #     soma += item.produto.valor * item.quantidade
        # return soma
        return sum([item.produto.valor * item.quantidade for item in self.__itens_pedido])

