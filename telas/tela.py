from typing import Dict

import pygame as pg
import logging


class TelaBase(object):
    def __init__(self, proxima = None):
        self.fechar_jogo: bool = False
        self.tela_finalizada: bool = False
        self.proxima = proxima
        self.sprites: [pg.Surface] = []
        self.atalhos_teclado: Dict[pg.event] = {
            pg.K_ESCAPE: self.sair,
        }

    def sair(self):
        self.fechar_jogo = True

    def eventos_teclado(self, evento: pg.event) -> None:
        if evento.type == pg.QUIT:
            self.sair()
            return

        if evento.type not in (pg.KEYDOWN, pg.KEYUP):
            return

        funcao_atalho = self.atalhos_teclado.get(evento.key, None)
        logging.info(f"Tecla apertada: {str(evento.key)}")
        if funcao_atalho is not None:
            funcao_atalho()
