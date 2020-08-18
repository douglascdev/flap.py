from pathlib import Path


class Configs:
    pasta_projeto = Path(__file__).parent.parent
    pasta_assets = pasta_projeto / "assets"
    pasta_audio = pasta_assets / "audio"
    pasta_sprites = pasta_assets / "sprites"
    tela_largura = 288
    tela_altura = 512
    fps = 60


if __name__ == "__main__":
    """
    Verificar a saída das pastas
    """
    print(Configs.pasta_projeto)
    print(Configs.pasta_assets)
    print(Configs.pasta_audio)
    print(Configs.pasta_sprites)
