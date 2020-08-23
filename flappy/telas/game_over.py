import pygame as pg
from flappy.controlador.pg_utils import carregar_sprite, posicao_central
from .menu import Menu
from .tela import TelaBase


class GameOver(TelaBase):
    def __init__(self, tela_pg, proxima_tela = Menu):
        TelaBase.__init__(self, tela_pg, proxima_tela)
        self.bg = carregar_sprite("bg/background-day")
        self.get_ready_sprite = carregar_sprite("outros/gameover")
        self.get_ready_rect = self.get_ready_sprite.get_rect()
        self.get_ready_central = posicao_central(self.get_ready_rect.w, self.get_ready_rect.h)

        # self.sprites.append(self.bg)
        # self.sprites.append(self.get_ready_sprite)

        self.atalhos_teclado[pg.K_SPACE] = self.finalizar

    def desenhar(self):
        # Altera posição do Get Ready para o centro da tela
        self.get_ready_rect.x, self.get_ready_rect.y = self.get_ready_central
        # Deveria ser feito iterando self.sprites, mas as posições x e y centralizadas são descartadas com o get_rect
        self.tela_pg.blit(self.bg, (0, 0))
        self.tela_pg.blit(self.get_ready_sprite, self.get_ready_rect)
