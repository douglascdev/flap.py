from pathlib import Path


class Configs:
    def __init__(self):
        self.pasta_projeto = Path(__file__).parent.parent
        self.pasta_assets = self.pasta_projeto / "assets"
        self.pasta_audio = self.pasta_assets / "audio"
        self.pasta_sprites = self.pasta_assets / "sprites"
        self.tela_largura = 600
        self.tela_altura = 400


if __name__ == "__main__":
    print(Configs().pasta_projeto)
    print(Configs().pasta_assets)
    print(Configs().pasta_audio)
    print(Configs().pasta_sprites)
