from telas.tela import Tela


class Jogo(Tela):
    def __init__(self):
        Tela.__init__(self)
        self.proxima = 'menu'
