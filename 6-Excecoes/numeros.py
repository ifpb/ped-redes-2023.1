try:
    num = int(input('Digite um numero: '))
    y = 1 / num
    print('Valor de y =', y)
except ZeroDivisionError:
    print('Divisão por zero não permitida')
except ValueError:
    print('Digite um inteiro válido')
except KeyboardInterrupt:
    print('Fim do programa - execução interrompida')
except:
    print('Erro inesperado!')
