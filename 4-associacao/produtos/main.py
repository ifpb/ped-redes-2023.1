from pedido import Pedido, ItemPedido
from produto import Produto

coxinha = Produto("001", 5.00, "Coxinha")
coca = Produto("002", 4.00, "Coca-cola")
pastel = Produto("003", 5.50, "Pastel")
bolo = Produto("004", 6.50, "Bolo")

pedido = Pedido()
pedido.adicionar_item(ItemPedido(coxinha, 2))
pedido.adicionar_item(ItemPedido(coca, 4))
pedido.adicionar_item(ItemPedido(pastel, 3))
pedido.adicionar_item(ItemPedido(bolo, 2))
print(pedido)
print(f"Total do Pedido = R${pedido.obter_total():.2f}")
