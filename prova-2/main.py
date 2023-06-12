from fila import *

fila = Fila()

arquivo1 = Arquivo("arquivo1", 100)
arquivo2 = Arquivo("arquivo2", 200)
arquivo3 = Arquivo("arquivo3", 300)
arquivo4 = Arquivo("arquivo4", 40)
arquivo5 = Arquivo("arquivo5", 50)

fila.inserir(arquivo1) 
fila.inserir(arquivo2)
fila.inserir(arquivo3)
fila.inserir(arquivo4)
fila.inserir(arquivo5)

fila.imprimir()
print(fila.remover())
fila = fila.ordenar()
print("ordenado =")
print(fila.imprimir())
print(f"Busca: {fila.buscar(arquivo3)}")