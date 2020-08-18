from entidades.entidade import Entidade


class Flappy(Entidade):
    def __init__(self):
        super(Flappy, self).__init__('flappy/amarelo')


if __name__ == '__main__':
    """
    Verificar sprites carregados. A função que carrega os sprites não funciona sem inicializar o display
    """

    import pygame as pg

    pg.init()
    pg.display.init()
    screen = pg.display.set_mode([800, 600])
    print(Flappy().sprites)
