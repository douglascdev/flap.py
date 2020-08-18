import sys
import pygame as pg
import logging
import telas
from configs.configs import Configs as Cfg


class Controlador:
    def __init__(self):
        logging.info("Inicializando controlador")
        pg.init()
        pg.display.init()
        self.tela_pg = pg.display.set_mode(size=(Cfg.tela_largura, Cfg.tela_altura))
        self.tela: telas.TelaBase = telas.menu.Menu()

    @staticmethod
    def sair() -> None:
        logging.info("Encerrando controlador")
        pg.display.quit()
        pg.quit()
        sys.exit()

    def game_loop(self) -> None:
        while True:
            for sprite in self.tela.sprites:
                self.tela_pg.blit(sprite, (0, 0))

            pg.display.update()

            for evento in pg.event.get():
                self.tela.eventos_teclado(evento)

            if self.tela.fechar_jogo:
                self.sair()
