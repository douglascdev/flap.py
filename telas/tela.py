from typing import Dict

import pygame as pg
import logging


class TelaBase(object):
    def __init__(self, tela_pg, proxima = None):
        logging.info(f"Instanciada a tela {self.__class__}")
        self.fechar_jogo: bool = False
        self.tela_finalizada: bool = False
        self.proxima = proxima
        self.tela_pg = tela_pg
        # Adicionar lista de sprites da mais ao fundo para mais a frente
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

        if evento.type != pg.KEYDOWN:
            return

        funcao_atalho = self.atalhos_teclado.get(evento.key, None)
        logging.info(f"Tecla apertada: '{evento.dict.get('unicode')}'")

        if funcao_atalho is not None:
            funcao_atalho()

    def desenhar(self):
        for sprite in self.sprites:
            self.tela_pg.blit(sprite, sprite.get_rect())

    def finalizar(self):
        logging.info(f"Finalizando a tela {self.__class__}")
        self.tela_finalizada = True
