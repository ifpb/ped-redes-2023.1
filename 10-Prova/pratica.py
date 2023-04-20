from abc import abstractmethod


class PortaIndisponivel(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class DispositivoDeRede:
    def __init__(self, nome, endereco_ip):
        self.nome = nome
        self.endereco_ip = endereco_ip
        self.portas = []

    def __str__(self):
        return f'{self.nome} - {self.endereco_ip}'

    '''
    Q1
    '''

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, portas):
        assert all(isinstance(p, int) for p in portas), 'Portas devem ser inteiros'
        self.__portas = portas


    '''
    Q2
    '''

    def conectar(self, dispositivo, porta):
        assert isinstance(dispositivo, DispositivoDeRede), 'Dispositivo deve ser uma instância de DispositivoDeRede'
        assert isinstance(porta, int), 'Porta deve ser um inteiro'
        if porta not in self.portas or porta not in dispositivo.portas:
            raise PortaIndisponivel('Porta indisponível')
        self.portas.remove(porta)
        dispositivo.portas.append(porta)
        print("Dispositivo conectado com sucesso!")

    '''
    Q3
    '''

    @abstractmethod
    def configurar(self):
        pass


class Firewall(DispositivoDeRede):
    def __init__(self, nome, endereco_ip):
        super().__init__(nome, endereco_ip)

    def configurar(self):
        print(f"Firewall {self.nome} configurado com sucesso!")


class Switch(DispositivoDeRede):
    def __init__(self, nome, endereco_ip, vlan):
        super().__init__(nome, endereco_ip)
        self.vlan = vlan

    def configurar(self):
        print(f"Switch {self.nome} configurado com sucesso!")


class Roteador(DispositivoDeRede):
    def __init__(self, nome, endereco_ip, protocolo):
        super().__init__(nome, endereco_ip)
        self.protocolo = protocolo

    def configurar(self):
        print(f"Roteador {self.nome} configurado com sucesso!")


'''
Main
'''

if __name__ == '__main__':
    dispositivo = DispositivoDeRede('R1', '10.0.0.2')
    dispositivo.portas = [1, 2, 3, 4]
    print(dispositivo)

    dispositivo2 = DispositivoDeRede('R2', '10.0.0.3')
    dispositivo2.portas = [3, 4, 5, 6]
    try:
        dispositivo.conectar(dispositivo2, 3)
        # dispositivo.conectar(dispositivo2, 6)

        roteador = Roteador('R3', '10.0.0.4', "TCP/IP")
        switch = Switch('S1', '10.0.0.5', "100")
        firewall = Firewall('F1', '10.0.0.6')

        for dispositivo in [roteador, switch, firewall]:
            dispositivo.configurar()

    except PortaIndisponivel as e:
        print(e)
