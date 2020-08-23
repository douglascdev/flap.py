import sys
import logging
import pygame as pg
from flappy.configs.configs import Configs as Cfg
from flappy.controlador.pg_utils import carregar_sprite
from flappy.telas.jogo import Jogo
from flappy.telas.game_over import GameOver
from flappy.telas.tela import TelaBase
from flappy.telas.menu import Menu


class Controlador:
    def __init__(self):
        logging.info("Inicializando controlador")
        pg.display.init()
        pg.mixer.init()
        self.tela_pg = pg.display.set_mode(size=(Cfg.TELA_LARGURA, Cfg.TELA_ALTURA))
        breakpoint()
        pg.display.set_icon(carregar_sprite("outros/favicon"))
        pg.display.set_caption("flap.py by douglas-cpp")
        self.clock = pg.time.Clock()
        self.tela: TelaBase = Menu(self.tela_pg, proxima_tela=Jogo)

    @staticmethod
    def sair() -> None:
        logging.info("Encerrando controlador")
        pg.display.quit()
        pg.quit()
        sys.exit()

    def game_loop(self) -> None:
        while True:
            self.tela.desenhar()

            for evento in pg.event.get():
                self.tela.eventos_teclado(evento)

            if self.tela.fechar_jogo:
                self.sair()

            if self.tela.tela_finalizada:
                if self.tela.proxima is None:
                    self.sair()

                # TODO: Esse if é um hotfix que impede a criação de dependências circulares ao tentar colocar a próxima
                #  tela dentro do código do menu. Criar uma solução melhor.
                if self.tela.__class__ == GameOver:
                    # A classe da próxima tela fica na variável self.tela.proxima, então aqui instanciamos a próxima
                    # tela usando o construtor dela
                    self.tela = self.tela.proxima(self.tela_pg, proxima_tela=Jogo)
                else:
                    self.tela = self.tela.proxima(self.tela_pg)

            pg.display.update()
            self.clock.tick(Cfg.FPS)
