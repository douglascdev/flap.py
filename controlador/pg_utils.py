import pygame as pg
import logging
from configs.configs import Configs
from typing import List


def carregar_sprites(pasta_sprites: str) -> List[pg.Surface]:
    """
    Carrega sprites da pasta especificada em memória e retorna a lista
    :param pasta_sprites: nome da pasta que está no diretório de sprites
    :return: lista de sprites carregados no formato pygame.Surface
    """
    pasta = Configs.pasta_sprites / pasta_sprites
    logging.info(f"Carregando os sprites da pasta '{str(pasta)}'")
    return [pg.image.load(str(sprite)).convert_alpha() for sprite in pasta.glob('*.png')]


def carregar_sprite(sprite: str) -> pg.Surface:
    """
    Carrega sprite especificado
    :param sprite: nome/caminho do png na pasta de sprites
    :return: sprite carregado como pg.Surface
    """
    return pg.image.load(str(Configs.pasta_sprites / sprite) + ".png").convert_alpha()
