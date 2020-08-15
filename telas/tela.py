import pygame as pg
import enum
from .jogo import Jogo
from .menu import Menu


class TelaBase(object):
    def __init__(self):
        self.finalizada: bool = False
        self.sair: bool = False
        self.proxima: TelaBase = None
        self.anterior: TelaBase = None

    def evento(self, event: pg.event):
        if event.type == pg.KEYDOWN:
            print(f'Apertou uma tecla na tela {self.__class__}')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.finalizada = True

    def atualizar(self, screen, dt):
        self.draw(screen)

    def desenhar(self, screen):
        screen.fill((0, 0, 255))


class Telas(enum.Enum):
    menu = Menu()
    jogo = Jogo()
