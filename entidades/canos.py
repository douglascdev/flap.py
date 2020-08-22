import logging
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
        self.x = 15
        self.y = Configs.tela_altura / 2

        self.ACELERACAO_GRAVIDADE = 0.05
        self.ACELERACAO_PULO = -self.ACELERACAO_GRAVIDADE * 5
        self.REDUCAO_ACELERACAO_PULO = self.ACELERACAO_GRAVIDADE / 200

        self.aceleracao = self.ACELERACAO_GRAVIDADE

    def pular(self):
        if not self.pulando:
            logging.info("Pulando!")
            self.pulando = True
            self.aceleracao = self.ACELERACAO_PULO

    def altura(self):
        self.y += self.aceleracao
        if self.pulando:
            # Desfaz a aceleração negativa gerada pelo pulo
            self.aceleracao += self.REDUCAO_ACELERACAO_PULO
            if self.aceleracao >= self.ACELERACAO_GRAVIDADE:
                self.pulando = False
                self.aceleracao = self.ACELERACAO_GRAVIDADE
        # if True:
        # self.y += 10
        # self.pulando = False

    def blitar(self):
        self.altura()
        super(Flappy, self).blitar()


if __name__ == '__main__':
    """
    Verificar sprites carregados. A função que carrega os sprites não funciona sem inicializar o display
    """

    import pygame as pg

    pg.init()
    pg.display.init()
    screen = pg.display.set_mode([800, 600])
    assert len(Flappy(screen).sprites) == 3
