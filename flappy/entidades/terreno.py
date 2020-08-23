from flappy.configs import Configs
from flappy.controlador import pg_utils
from flappy.entidades.entidade import Entidade


class Terreno(Entidade):
    def __init__(self, tela_pg):
        # TODO: não carregar toda a pasta outros
        # Talvez criar dicionario de sprites ao inves de lista, com o nome do arquivo de key
        super(Terreno, self).__init__('outros', tela_pg)
        self.rect.y = pg_utils.posicao_baixo(self.imagem.get_height())
        self.contador_mov = 0
        # Quantidade de pixels do terreno que pode ser movido para a esquerda durante a animação, antes de voltar para 0
        # TODO: ver se ao fim da animação não está fazendo um corte visível
        self.limite_x = self.imagem.get_width() - Configs.TELA_LARGURA

    def desenhar(self):
        # TODO: não usar esses ifs pra fazer contagem, usar o clock do pygame
        if self.movimentar:
            if self.contador_mov == Configs.FPS_POR_MOV_TELA:
                self.mover(-Configs.PIXELS_MOV, 0)
                self.contador_mov = 0
            else:
                self.contador_mov += 1

        # Não deixa o terreno voltar para antes do limite
        if self.imagem.get_width() + self.rect.x <= Configs.TELA_LARGURA:
            self.rect.x = 0

        super(Terreno, self).desenhar()

    def proximo_sprite(self):
        pass  # Não precisa trocar de sprite
