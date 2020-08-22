from random import choice
from entidades.entidade import Entidade


class Flappy(Entidade):
    def __init__(self, tela_pg):
        cores_flappy = ('amarelo', 'azul', 'vermelho')
        # Escolhe cor aleatória entre as opções da lista e concatena com o caminho da pasta
        pasta_cor = 'flappy/' + choice(cores_flappy)
        super(Flappy, self).__init__(pasta_cor, tela_pg)


if __name__ == '__main__':
    """
    Verificar sprites carregados. A função que carrega os sprites não funciona sem inicializar o display
    """

    import pygame as pg

    pg.init()
    pg.display.init()
    screen = pg.display.set_mode([800, 600])
    assert len(Flappy(screen).sprites) == 3
