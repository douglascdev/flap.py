from importlib import resources
from flappy import assets


class Configs:
    with resources.path(assets, "") as p:
        PASTA_ASSETS = p
    PASTA_AUDIO = PASTA_ASSETS / "audio"
    PASTA_SPRITES = PASTA_ASSETS / "sprites"
    PASTA_FONTES = PASTA_ASSETS / "fontes"
    TELA_LARGURA = 288
    TELA_ALTURA = 512
    FPS = 60

    # Quantidade de fps que o jogo espera antes de mudar cada animação para o próximo sprite
    FPS_POR_ANIMACAO = 5

    # Quantidade de fps que o jogo espera antes de mover tubos e o terreno para a esquerda
    FPS_POR_MOV_TELA = 1

    # Pixels adicionados a cada passo do processo anterior
    PIXELS_MOV = 5

    # Intervalo de pixels da tela em que a abertura dos canos vai ser gerada
    ABERTURA_MIN = 150
    ABERTURA_MAX = 350

    # Tamanho em pixels da abertura entre os canos
    TAM_ABERTURA = 120

    ACELERACAO_GRAVIDADE = 5
    ACELERACAO_PULO = -ACELERACAO_GRAVIDADE * 2.5
    REDUCAO_ACELERACAO_PULO = ACELERACAO_GRAVIDADE / 4

    # Posicao inicial do flappy que vai ser subtraida da posição central(quanto maior mais alto)
    POSICAO_INICAL = 200


if __name__ == "__main__":
    """
    Verificar a saída das pastas
    """
    print(Configs.PASTA_ASSETS)
    print(Configs.PASTA_AUDIO)
    print(Configs.PASTA_SPRITES)
