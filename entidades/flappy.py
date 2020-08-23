import logging
import pygame as pg
from random import choice

from controlador.pg_utils import som
from entidades.entidade import Entidade
from configs.configs import Configs


class Flappy(Entidade):
    def __init__(self, tela_pg):
        cores_flappy = ('amarelo', 'azul', 'vermelho')
        # Escolhe cor aleatória entre as opções da lista e concatena com o caminho da pasta
        pasta_cor = 'flappy/' + choice(cores_flappy)
        super(Flappy, self).__init__(pasta_cor, tela_pg)
        self.pulando = False
        self.rect.x = Configs.TELA_LARGURA / 10
        self.rect.y = Configs.TELA_ALTURA / 2 - Configs.POSICAO_INICAL

        self.aceleracao_vertical = Configs.ACELERACAO_GRAVIDADE

    def pular(self):
        # if not self.pulando:
        logging.info("Pulando!")
        som("wing")
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

    def desenhar(self):
        self.altura()
        super(Flappy, self).desenhar()
