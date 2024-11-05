import pygame
import constantes
import sprites
import os

pygame.init()

class Game:
    def __init__(self):
        #criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.LARGURA,constantes.ALTURA))
        pygame.display.set_caption(constantes.TITULO_JOGO)
        #Relógio que controla a taxa de frames, fps
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)
        self.carregar_arquivos()
    
    def novo_jogo(self):
        #instancia as classes das sprits do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        self.tela.fill(constantes.PRETO) #limpando a tela
        self.todas_as_sprites.draw(self.tela) #desenhando as sprites
        pygame.display.flip() #atualiza a tela a cada frame do jogo

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.diretorio_audios = os.path.join(os.getcwd(), 'audios')
        #atributo pq vamos reutilizar em outras partes da classe
        self.spritesheer = os.path.join(diretorio_imagens, constantes.SPRITESHEET)
        self.pacman_start_logo = os.path.join(diretorio_imagens, constantes.PACMAN_START_LOGO)
        self.pacman_start_logo = pygame.image.load(self.pacman_start_logo).convert()

    def mostrar_tela_start(self):
        pass

    def mostrar_tela_game_over(self):
        pass

    #depois de construir classe, vamos instanciar essa classe (criar objeto a partir dessa classe g)
    #ver videoaula sobre programção orientada a objetos pra entender sobre instanciar classes

g = Game()
g.mostrar_tela_start()


while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()

    