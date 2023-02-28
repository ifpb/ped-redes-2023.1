from lampada import Lampada

print("Lampada 1: ")
l1 = Lampada(True, "Amarela")
print(f"Cor: {l1.cor}")
print(f"Ligada? {l1.esta_ligada()}")
print(f"Desligada? {l1.esta_desligada()}")

print("Lampada 1 =", l1)

print()
print("Lampada 2: ")
l2 = Lampada(False)
print(f"Cor: {l2.cor}")
print(f"Ligada? {l2.esta_ligada()}")
print(f"Desligada? {l2.esta_desligada()}")
l2.mudar_cor("Amarela")
l2.ligado = True
print(f"Cor: {l2.cor}")
print(f"Ligada? {l2.esta_ligada()}")
print(f"Desligada? {l2.esta_desligada()}")
print("Lampada 2 =", l2)