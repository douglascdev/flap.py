from controlador.controlador import Controlador
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    ct = Controlador()
    ct.game_loop()

