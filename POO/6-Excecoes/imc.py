class IMCException(Exception):
    def __init__(self, message):
        super().__init__(message)


def calcular_grau_imc(imc):
    if imc <= 18.5:
        return "Peso abaixo do normal"
    elif 18.5 < imc <= 24.9:
        return "Peso normal"
    elif 24.9 < imc <= 29.9:
        return "Sobrepeso"
    elif 29.9 < imc <= 34.9:
        return "Obesidade grau 1"
    elif 34.9 < imc <= 39.9:
        return "Obesidade grau 2"
    elif imc > 39.9:
        raise IMCException("Obesidade grau 3, procure um médico!")


def imc(peso, altura):
    assert type(peso) == int or type(peso) == float, "peso precisa ser um número"
    assert type(altura) == int or type(altura) == float, "altura precisa ser um número"
    assert peso > 0, "peso deve ser maior que zero"
    assert altura > 0, "altura deve ser maior que zero"
    return peso / (altura * altura)


if __name__ == '__main__':
    spa = []
    while True:
        print('--------------------')
        print('Calculadora IMC')
        print('--------------------')
        print('(c) calcular IMC')
        print('(s) Sair')
        print('---------------------')
        opcao = input('opcao:')
        opcao = opcao.lower()

        if opcao == 'c':  ### calcular IMC
            try:
                peso = int(input('Digite o peso:'))
                altura = float(input('Digite a altura:').replace(',', '.'))

                imc = imc(peso, altura)
                print(f'O seu IMC é de {imc:0.2f}')
                print(f'O grau do IMC é {calcular_grau_imc(imc)}')
            except IMCException as i:
                print(i)
            except AssertionError as e:
                print(e)
            except ValueError:
                print("Digite um valor numérico")
            except ZeroDivisionError:
                print('Não é possível dividir por zero')
        elif opcao == 's':
            break
