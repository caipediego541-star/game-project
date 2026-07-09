import pygame
import config
class Game:
    def __init__(self):
        pygame.init()
        #creamos la ventana usando las variables de la configuración
        self.screen = pygame.display.set_mode((config.ANCHO,config.ALTO))
        #titulo de la ventana
        pygame.display.set_caption(config.TITULO)

        #reloj del juego
        self.clock=pygame.time.Clock()