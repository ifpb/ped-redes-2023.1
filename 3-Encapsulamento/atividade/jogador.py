"""
2. Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento,
    nacionalidade, altura e peso.
Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador.
Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo falta
    para o jogador se aposentar.
Para isso, considere que os jogadores da posição de defesa se aposentam em média aos 40 anos, os jogadores de
    meio-campo aos 38 e os atacantes aos 35.
"""
from datetime import datetime
from enum import Enum


class Posicao(Enum):
    DEFESA = "Defesa"
    MEIO_CAMPO = "Meio-campo"
    ATAQUE = "Ataque"


class Jogador:
    def __init__(self, nome: str, posicao: Posicao, nascimento: str, nacionalidade: str, altura: float, peso: float):
        self.nome = nome
        self.posicao = posicao
        self.nascimento = nascimento
        self.nacionalidade = nacionalidade
        self.altura = altura
        self.peso = peso

    def calcular_idade(self):
        idade_timedelta = datetime.today() - self.__nascimento
        return int(idade_timedelta.days / 365)

    def tempo_falta_aposentadoria(self):
        anos_faltam = self.__idade_aposentadoria() - self.calcular_idade()
        return anos_faltam if anos_faltam > 0 else 0

    def __idade_aposentadoria(self):
        idade_aposentar = {
            Posicao.DEFESA: 40,
            Posicao.MEIO_CAMPO: 38,
            Posicao.ATAQUE: 35,
        }
        return idade_aposentar.get(self.posicao, 0)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def posicao(self):
        return self.__posicao

    @posicao.setter
    def posicao(self, posicao):
        assert type(posicao) == Posicao, "Posição deve ser do tipo Enum Posicao"
        self.__posicao = posicao

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    @property
    def nascimento(self):
        return self.__nascimento.strftime("%d/%m/%Y")

    @nascimento.setter
    def nascimento(self, nascimento: str):
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        assert type(altura) == float or type(altura) == int, "Altura precisa ser um número"
        self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        assert type(peso) == float or type(peso) == int, "Peso precisa ser um número"
        self.__peso = peso

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Posição: {self.posicao}
        Nacionalidade: {self.nacionalidade}
        Data de Nascimento: {self.nascimento}
        Altura: {self.altura}
        Peso: {self.peso}
        Idade: {self.calcular_idade()}
        Tempo falta para aposentar: {self.tempo_falta_aposentadoria()} anos
        """


if __name__ == '__main__':
    j1 = Jogador("Neymar", Posicao.ATAQUE, '05/02/1992', "Brasileiro", 1.75, 68.0)
    j2 = Jogador("Messi", Posicao.MEIO_CAMPO, '24/06/1987', "Argentino", 1.69, 70.0)
    j3 = Jogador("Romário", Posicao.ATAQUE, '29/01/1966', "Brasileiro", 1.67, 75)
    j4 = Jogador("Cássio", Posicao.DEFESA, '06/06/1987', 'Brasileiro', 1.96, 95)
    j5 = Jogador("Arrascaeta", Posicao.MEIO_CAMPO, '01/06/1994', 'Uruguaio', 1.72, 73)
    print(j1, j2, j3, j4, j5)
