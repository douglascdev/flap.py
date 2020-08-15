class Entidade(object):
    def __init__(self, x: int = 0, y: int = 0, sprites: list = None):
        if sprites is None:
            sprites = []
