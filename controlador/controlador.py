import sys
import logging
from controlador.pg_utils import carregar_sprite
import pygame as pg
import telas
from configs.configs import Configs as Cfg
from telas import Jogo
from telas.game_over import GameOver


class Controlador:
    def __init__(self):
        logging.info("Inicializando controlador")
        pg.init()
        pg.display.init()
        self.tela_pg = pg.display.set_mode(size=(Cfg.TELA_LARGURA, Cfg.TELA_ALTURA))
        pg.display.set_icon(carregar_sprite("outros/favicon"))
        self.clock = pg.time.Clock()
        self.tela: telas.TelaBase = telas.menu.Menu(self.tela_pg, proxima_tela=Jogo)

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
