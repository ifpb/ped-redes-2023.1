class CartaoMensagem:
    def __init__(self, destinatario, remetente):
        self.destinatario = destinatario
        self.remetente = remetente

    def retornar_mensagem(self):
        pass


class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return f"Feliz dia dos namorados, {self.destinatario}! - Ass. {self.remetente}"


class MensagemNatal(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return f"Feliz natal, {self.destinatario}! - Ass. {self.remetente}"


class MensagemAniversario(CartaoMensagem):
    def __init__(self, destinatario, remetente):
        super().__init__(destinatario, remetente)

    def retornar_mensagem(self):
        return f"Feliz aniversário, {self.destinatario}! - Ass. {self.remetente}"


if __name__ == '__main__':
    mensagens = [ MensagemDiaDosNamorados(
        input("Destinatário para mensagem de dia dos namorados "),
        input("Remetente para mensagem de dia dos namorados "),
    ),
     MensagemAniversario(
         input("Destinatário para mensagem de aniversário"),
         input("Remetente para mensagem de aniversário")
     ),
     MensagemNatal(
         input("Destinatário para mensagem de natal"),
         input("Remetente para mensagem de natal")
     )]

    for mensagem in mensagens:
        print(mensagem.retornar_mensagem())