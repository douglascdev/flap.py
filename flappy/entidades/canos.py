import pygame as pg
from random import choice, randint

from flappy.entidades.entidade import Entidade
from flappy.configs.configs import Configs


class Canos(Entidade):
    """
    Representa dois canos na tela
    """
    def __init__(self, tela_pg):
        """
        TODO: carregar sprites em atributo estático das classe entidade? Ou pelo menos não carregar ao criar os canos
        """
        super(Canos, self).__init__("cano", tela_pg)
        self.imagem_invertida = None
        self.rect_invertida = self.rect.copy()
        self.pos_abertura = 0
        self.contador_mov = 0
        self.resetar_atributos()

    # Ao chegar ao fim da tela para a esquerda, chamar esse método para resetar os atributos de posição, abertura, etc
    def resetar_atributos(self):
        # Escolha aleatória entre cores de cano disponíveis
        self.imagem = choice(self.sprites)
        # Cano superior, que é o cano normal rotacionado
        # TODO: não fazer isso no resetar atributos
        self.imagem_invertida = pg.transform.rotate(self.imagem, 180)
        # Gerar aleatoriamente a posição em que a abertura entre os canos ficará
        self.pos_abertura = randint(Configs.ABERTURA_MIN, Configs.ABERTURA_MAX)
        self.rect.x = Configs.TELA_LARGURA
        self.rect.y = self.pos_abertura

    def chegou_ao_final(self):
        return self.rect.x + self.imagem.get_width() <= 0

    def desenhar(self):
        if self.chegou_ao_final():
            self.resetar_atributos()
        else:
            if self.movimentar:
                if self.contador_mov == Configs.FPS_POR_MOV_TELA:
                    self.mover(-Configs.PIXELS_MOV, 0)
                    self.contador_mov = 0
                else:
                    self.contador_mov += 1

        self.rect_invertida = self.rect.copy()
        self.rect_invertida.y = self.pos_abertura - Configs.TAM_ABERTURA - self.rect.h
        self.tela_pg.blit(self.imagem_invertida, self.rect_invertida)
        self.tela_pg.blit(self.imagem, self.rect)

    def colisao(self, outro: pg.rect.Rect) -> bool:
        return self.rect.colliderect(outro) or self.rect_invertida.colliderect(outro)
