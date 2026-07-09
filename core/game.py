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
    def run(self):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            self.clock.tick(config.FPS)
        pygame.quit()
   


