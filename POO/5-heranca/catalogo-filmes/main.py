from filmes import *


def imprimir_opcoes(catalogo):
    print('--------------------')
    print(catalogo.titulo)
    print('--------------------')
    print('(r) Reajustar preço')
    print('(a) Avaliar filme')
    print('(l) Listar catálogo')
    print('(c) Cadastrar filme')
    print('(p) Pesquisar filme')
    print('(s) Sair')
    print('---------------------')


def reajustar_preco(catalogo):
    id_filme = int(input('Digite o id do Filme que deseja alterar o preço:'))
    try:
        filme = catalogo.pesquisar_filme(id_filme)
        print('Titulo:', filme.titulo)
        print('Preco anterior:', filme.preço)
        novoPreco = float(input('Novo preço:'))
        catalogo.reajustar_preco(id_filme, novoPreco)
    except FilmeInexistente as e:
        print(e)
    except AssertionError as e:
        print(e)


def avaliar_filme(catalogo):
    id_filme = int(input('Digite o id do Filme que deseja avaliar:'))
    try:
        filme = catalogo.pesquisar_filme(id_filme)
        print('Titulo:', filme.titulo)
        nota = float(input('Nota:'))
        catalogo.avaliar_filme(id_filme, nota)
    except (FilmeInexistente, AssertionError) as e:
        print(e)


def cadastrar_filme(catalogo):
    id_filme = int(input('id do Filme:'))
    titulo = input('Titulo:')
    preço = float(input('Preço da locação:'))

    try:
        catalogo.cadastrar_filme(Filme(id_filme, titulo, preço))
    except (IdJaUtilizado, FilmeJaCadastrado) as e:
        print(e)

    print('\n')
    catalogo.listar_filmes()


def pesquisar_filme(catalogo):
    id_filme = int(input('Digite o id do Filme que deseja consultar:'))
    try:
        filme = catalogo.pesquisar_filme(id_filme)
        print('Titulo:', filme.titulo)
        print('Preço:', filme.preço)
        print('Nota:', filme.nota)
    except Exception as e:
        print(e)


########################################
# instanciando a Plataforma de Streaming com o nome desejado
netflix = PlataformaStreaming('Netflix')
netflix.cadastrar_filme(Filme(1, 'Stuart Little', 5.0))
netflix.cadastrar_filme(Filme(2, 'Luca', 15.0))

while True:
    imprimir_opcoes(netflix)

    opcao = input('opcao:').lower()

    if opcao == 'r':
        reajustar_preco(netflix)

    elif opcao == 'a':
        avaliar_filme(netflix)

    elif opcao == 'l':
        netflix.listar_filmes()

    elif opcao == 'c':
        cadastrar_filme(netflix)

    elif opcao == 'p':
        pesquisar_filme(netflix)

    elif opcao == 's':
        break
