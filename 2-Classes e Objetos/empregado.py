

class Empregado:

    NUM_EMPREGADOS_CRIADOS = 0
    SALARIO_PADRAO = 1500.00
    DECIMO_TERCEIRO_ATIVO = False

    def __init__(self, nome, salario=-1):
        if salario < 0:
            salario = Empregado.SALARIO_PADRAO
        self.nome = nome
        self.salario = salario
        Empregado.NUM_EMPREGADOS_CRIADOS += 1
        self.NUM_EMPREGADOS_CRIADOS = 999

    def calcula_imposto_renda(self):
        pass

    def calcula_desconto_vale_transporte(self):
        return self.salario * 0.06
    
    def vai_ter_decimo_terceiro(self):
        return "SIM! TEREMOS 13º" if Empregado.DECIMO_TERCEIRO_ATIVO else "Que pena! Não teremos 13º!"
    
    def habilitar_decimo_terceiro(self):
        Empregado.DECIMO_TERCEIRO_ATIVO = True

    def desabilitar_decimo_terceiro(self):
        Empregado.DECIMO_TERCEIRO_ATIVO = False

    def __str__(self):
        return f"Nome: {self.nome}, Salário: R$ {self.salario:.2f}, Desconto Vale: R$ {self.calcula_desconto_vale_transporte():.2f}"

i = 1
print("Digite sair para encerrar e execução")
opcao = ""
empregados = []
while(opcao != "sair"):
    nome = input(f"Digite o nome do empregado {i}")
    salario = float(input(f"Digite o salario do empregado {i}"))
    e = Empregado(nome, salario)
    i += 1
    empregados.append(e)
    opcao = input("Digite a opção desejada (sair, continuar)")

for emp in empregados:
    print(emp)


# e1 = Empregado("José da Silva")
# e2 = Empregado("Maria da Silva", 2000)
# print(e1.vai_ter_decimo_terceiro())
# print(e2.vai_ter_decimo_terceiro())
# e1.habilitar_decimo_terceiro()
# print(e1.vai_ter_decimo_terceiro())
# print(e2.vai_ter_decimo_terceiro())
# print(Empregado.DECIMO_TERCEIRO_ATIVO)

# print("Salário de e1: ",e1.salario)
# print("NUM EMPREGADOS CRIADOS =", e1.NUM_EMPREGADOS_CRIADOS)
# print(e1.vai_ter_decimo_terceiro())

# print(e2.vai_ter_decimo_terceiro())
# Empregado.DECIMO_TERCEIRO_ATIVO = True
# print(e2.vai_ter_decimo_terceiro())
# print("Salário de e2: ",e2.salario)
# print("Número de empregados criados: ", Empregado.NUM_EMPREGADOS_CRIADOS)
# print("NUM EMPREGADOS CRIADOS =", e1.NUM_EMPREGADOS_CRIADOS)
