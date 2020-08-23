__author__ = 'Douglas Carvalho'
__email__ = 'douglasc.dev@gmail.com'
__version__ = '0.0.1'

from flappy.controlador.controlador import Controlador


def flappy():
    ct = Controlador()
    ct.game_loop()


if __name__ == "__main__":
    flappy()
