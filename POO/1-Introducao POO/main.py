from onibus import Onibus, Garagem
onibus1 = Onibus(40, "Mercedez")
onibus1.acelerar(50)
onibus1.acelerar(20)
onibus1.desacelerar(10)
print(f"Marca = {onibus1.marca}")
print(f"Lugares = {onibus1.lugares}")
print(f"Velocidade = {str(onibus1.velocidade)}km/h")
onibus1.frear()
print(f"Velocidade = {str(onibus1.velocidade)}km/h")
onibus1.buzinar()
print(f"Direção do onibus {onibus1.direcao}")
onibus1.mudar_direcao(2)
print(f"Direção do onibus {onibus1.direcao}")

g = Garagem(50)
g.adicionar_veiculo()

onibus2 = Onibus(30, "X")
micro_onibus = Onibus(15, "XYZ")
onibus2.estacionar()


