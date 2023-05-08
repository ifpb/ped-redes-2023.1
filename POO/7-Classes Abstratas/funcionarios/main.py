from tabulate import tabulate

from funcionarios import Gerente, Diretor, Presidente, GrauInstrucao

try:
    gerente = Gerente("Steve Jobs", 1500, GrauInstrucao.ESPECIALISTA)
    diretor = Diretor("Bill Gates", 3500, GrauInstrucao.MESTRE)
    presidente = Presidente("Linus Torvalds", 2000, GrauInstrucao.DOUTOR)
    funcionarios = [gerente, diretor, presidente]
    for f in funcionarios:
        print(f)

    print(tabulate(
        [[f.nome, f.grau_instrucao.nome, f'R$ {f.salario_base:.2f}', f'R$ {f.bonificacao:.2f}', f'R$ {f.contracheque():.2f}'] for f in funcionarios],
        headers=['Nome', 'Grau de Instrução', 'Salário base', 'Bonificação', 'Salário total']))


except Exception as fe:
    print(fe)
