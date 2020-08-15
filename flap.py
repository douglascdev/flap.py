import pygame as pg
import sys
from configs.configs import Configs


if __name__ == '__main__':
    configs = Configs()
    largura, altura = configs.tela_largura, configs.tela_altura
    screen = pg.display.set_mode(largura, altura)
    pg.quit()
    sys.exit()
