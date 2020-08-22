import pygame as pg
from configs import Configs
from entidades.entidade import Entidade


class Score(Entidade):
    def __init__(self, tela_pg):
        super(Score, self).__init__("numeros", tela_pg)
        self.score = 0
        self.contador_score = 0
        pg.font.init()
        self.rect.x, self.rect.y = Configs.TELA_LARGURA / 2, Configs.TELA_ALTURA / 10
        self.fonte = pg.font.Font("assets/fontes/press-start-2/PressStart2P-vaV7.ttf", 20)

    def desenhar(self):
        str_score = str(self.score)
        self.imagem = self.fonte.render(str_score, False, (255, 255, 255))
        rect = self.imagem.get_rect(center=(Configs.TELA_LARGURA / 2, 50))
        self.tela_pg.blit(self.imagem, rect)

    def incrementar_score(self):
        if self.contador_score == Configs.FPS_POR_MOV_TELA:
            self.score += 1
            self.contador_score = 0
        else:
            self.contador_score += 1

    def mover(self, x: int, y: int):
        pass

    def proximo_sprite(self):
        pass

    def colisao(self, outro: pg.rect.Rect) -> bool:
        return False
