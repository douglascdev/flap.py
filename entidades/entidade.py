from controlador.pg_utils import carregar_sprites
import pygame as pg


class Entidade(pg.sprite.Sprite):
    def __init__(self, pasta_sprites: str):
        pg.sprite.Sprite.__init__(self)
        self.sprites = carregar_sprites(pasta_sprites)
        self.index_imagem = 0
        self.imagem = self.sprites[self.index_imagem]
        self.ret = self.imagem.get_rect()
        # Usado pra manter copia da posição do image, já que ele pode ser alterado para outra referência
        self.x: int = 0
        self.y: int = 0

    def mover(self, x: int, y: int):
        self.x += x
        self.y += y
        self.ret.x = self.x
        self.ret.y = self.y

    def proximo_sprite(self):
        self.index_imagem = (self.index_imagem + 1) % len(self.sprites)
        self.imagem = self.sprites[self.index_imagem]
        self.ret = self.imagem.get_rect()
        self.ret.x = self.x
        self.ret.y = self.y

