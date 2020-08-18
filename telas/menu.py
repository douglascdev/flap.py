from .tela import TelaBase
from .jogo import Jogo
from controlador.pg_utils import carregar_sprite


class Menu(TelaBase):
    def __init__(self):
        TelaBase.__init__(self, Jogo)
        self.get_ready = carregar_sprite("outros/get-ready")
        self.bg = carregar_sprite("bg/background-day")
        self.sprites.append(self.get_ready)
        self.sprites.append(self.bg)
