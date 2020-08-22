import pygame as pg
import logging
from random import randint
from configs.configs import Configs
from controlador.pg_utils import carregar_sprites
from entidades.flappy import Flappy
from entidades.terreno import Terreno
from entidades.canos import Canos
from telas.game_over import GameOver
from telas.tela import TelaBase


class Jogo(TelaBase):
    def __init__(self, tela_pg):
        TelaBase.__init__(self, tela_pg, proxima=GameOver)
        # TODO: contar arquivos da pasta ao inves de carregar tudo
        fundos = carregar_sprites("bg")
        # Gera um fundo aleatório entre os que estão na pasta.
        indice_fundo_aleatorio = randint(0, len(fundos) - 1)
        self.bg = fundos[indice_fundo_aleatorio]

        self.flappy = Flappy(tela_pg)
        self.terreno = Terreno(tela_pg)
        self.canos1 = Canos(tela_pg)
        self.canos2 = Canos(tela_pg)
        self.canos2.rect.x += (Configs.TELA_LARGURA + self.canos2.imagem.get_width()) / 2

        # self.sprites.append(self.bg)
        # self.sprites.append(self.terreno)

        self.atalhos_teclado[pg.K_SPACE] = self.flappy.pular

    def desenhar(self):
        self.tela_pg.blit(self.bg, self.bg.get_rect())
        # TODO: desenhar score
        self.canos1.desenhar()
        self.canos2.desenhar()
        self.terreno.desenhar()
        self.flappy.desenhar()

        # TODO: animação de morte, tela de game over
        objetos_colisao = [self.canos1, self.canos2, self.terreno]
        for objeto in objetos_colisao:
            if objeto.colisao(self.flappy):
                logging.info(f"Flappy colidiu com '{objeto.__class__}'")
                self.canos1.movimentar = False
                self.canos2.movimentar = False
                self.flappy.movimentar = False
                self.atalhos_teclado = {}
                pg.time.wait(1000)
                self.proxima = GameOver
                self.finalizar()
                break
