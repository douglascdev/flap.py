import pygame as pg
import logging
from flappy.configs.configs import Configs
from typing import List, Tuple


def carregar_sprites(pasta_sprites: str) -> List[pg.Surface]:
    """
    Carrega sprites da pasta especificada em memória e retorna a lista
    :param pasta_sprites: nome da pasta que está no diretório de sprites
    :return: lista de sprites carregados no formato pygame.Surface
    """
    pasta = Configs.PASTA_SPRITES / pasta_sprites
    logging.info(f"Carregando os sprites da pasta '{str(pasta)}'")
    return [pg.image.load(str(sprite)).convert_alpha() for sprite in sorted(pasta.glob('*.png'))]


def carregar_sprite(sprite: str) -> pg.Surface:
    """
    Carrega sprite especificado
    :param sprite: nome/caminho do png na pasta de sprites
    :return: sprite carregado como pg.Surface
    """
    pasta_str = str(Configs.PASTA_SPRITES / sprite)
    logging.info(f"Carregando sprite '{pasta_str}.png'")
    return pg.image.load(str(Configs.PASTA_SPRITES / sprite) + ".png").convert_alpha()


def posicao_central(largura: int, altura: int) -> Tuple:
    """
    Calcula a posição em que o objeto deve ser renderizado para ficar centralizado na tela do jogo
    :param altura:
    :param largura:
    :return: coordenadas x e y em que o objeto deve ser renderizado para ficar centralizado
    """
    posicao = (Configs.TELA_LARGURA - largura) / 2, (Configs.TELA_ALTURA - altura) / 2
    logging.info(f"Posição central: {posicao}")
    return posicao


def posicao_central_horizontal(largura: int) -> int:
    """
    Calcula a posição em que o objeto deve ser renderizado para ficar centralizado na horizontal
    :param largura:
    :return: coordenadas x e y em que o objeto deve ser renderizado para ficar centralizado
    """
    posicao = (Configs.TELA_LARGURA - largura) / 2
    logging.info(f"Posição central: {posicao}")
    return posicao


def posicao_baixo(altura: int) -> int:
    """
    Calcula a posição em que o objeto deve ser renderizado para ficar embaixo na tela do jogo
    :param altura:
    :return: coordenada y em que o objeto deve ser renderizado pra ficar embaixo
    """
    posicao = Configs.TELA_ALTURA - altura
    logging.info(f"Posição baixo: {posicao}")
    return posicao


def som(nome: str):
    s = pg.mixer.Sound(str(Configs.PASTA_AUDIO / f"{nome}.wav"))
    s.play()
