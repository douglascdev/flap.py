from telas.tela import TelaBase


class Jogo(TelaBase):
    def __init__(self):
        TelaBase.__init__(self)
        self.proxima = 'menu'
