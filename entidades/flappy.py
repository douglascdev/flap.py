import logging
import pygame as pg
from random import choice
from entidades.entidade import Entidade
from configs.configs import Configs


class Flappy(Entidade):
    def __init__(self, tela_pg):
        cores_flappy = ('amarelo', 'azul', 'vermelho')
        # Escolhe cor aleatória entre as opções da lista e concatena com o caminho da pasta
        pasta_cor = 'flappy/' + choice(cores_flappy)
        super(Flappy, self).__init__(pasta_cor, tela_pg)
        self.pulando = False
        self.rect.x = 15
        self.rect.y = Configs.TELA_ALTURA / 2

        self.aceleracao_vertical = Configs.ACELERACAO_GRAVIDADE

    def pular(self):
        if not self.pulando:
            logging.info("Pulando!")
            self.pulando = True
            self.aceleracao_vertical = Configs.ACELERACAO_PULO

    def altura(self):
        self.mover(0, self.aceleracao_vertical)
        if self.pulando:
            # Desfaz a aceleração negativa gerada pelo pulo
            self.aceleracao_vertical += Configs.REDUCAO_ACELERACAO_PULO
            if self.aceleracao_vertical >= Configs.ACELERACAO_GRAVIDADE:
                self.pulando = False
                self.aceleracao_vertical = Configs.ACELERACAO_GRAVIDADE
        # if True:
        # self.y += 10
        # self.pulando = False

    def desenhar(self):
        self.altura()
        super(Flappy, self).desenhar()


if __name__ == '__main__':
    """
    Verificar sprites carregados. A função que carrega os sprites não funciona sem inicializar o display
    """

    import pygame as pg

    pg.init()
    pg.display.init()
    screen = pg.display.set_mode([800, 600])
    assert len(Flappy(screen).sprites) == 3
