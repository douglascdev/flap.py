import logging
import pygame as pg
from configs import Configs
from controlador.pg_utils import carregar_sprites


class Entidade(pg.sprite.Sprite):
    def __init__(self, pasta_sprites: str, tela_pg):
        pg.sprite.Sprite.__init__(self)
        self.tela_pg = tela_pg
        self.sprites = carregar_sprites(pasta_sprites)
        self.index_imagem = 0
        self.imagem = self.sprites[self.index_imagem]
        self.clock = pg.time.Clock()
        self.rect = self.imagem.get_rect().copy()
        self.contador_animacao = 0
        self.movimentar = True

    def mover(self, x: int, y: int):
        self.rect.move_ip(x, y)

    def proximo_sprite(self):
        self.index_imagem = (self.index_imagem + 1) % len(self.sprites)
        logging.info(f"Carregando próximo sprite. Entidade: '{self.__class__}'. Index: '{self.index_imagem}'")
        self.imagem = self.sprites[self.index_imagem]

    def desenhar(self):
        self.tela_pg.blit(self.imagem, self.rect)
        if self.movimentar:
            if self.contador_animacao == Configs.FPS_POR_ANIMACAO:
                self.proximo_sprite()
                self.contador_animacao = 0
            else:
                self.contador_animacao += 1

    def colisao(self, outro: pg.rect.Rect) -> bool:
        return self.rect.colliderect(outro)
