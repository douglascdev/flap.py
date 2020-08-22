from pathlib import Path


class Configs:
    PASTA_PROJETO = Path(__file__).parent.parent
    PASTA_ASSETS = PASTA_PROJETO / "assets"
    PASTA_AUDIO = PASTA_ASSETS / "audio"
    PASTA_SPRITES = PASTA_ASSETS / "sprites"
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


if __name__ == "__main__":
    """
    Verificar a saída das pastas
    """
    print(Configs.PASTA_PROJETO)
    print(Configs.PASTA_ASSETS)
    print(Configs.PASTA_AUDIO)
    print(Configs.PASTA_SPRITES)
