import pygame as pg
import sys
from configs.configs import Configs


if __name__ == '__main__':
    configs = Configs()
    screen = pg.display.set_mode((configs.tela_largura, configs.tela_altura))
    pg.quit()
    sys.exit()
