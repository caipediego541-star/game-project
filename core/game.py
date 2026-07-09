import pygame
import config
from core.resource_manager import ResourceManager
class Game:
    def __init__(self):
        pygame.init()
        #creamos la ventana usando las variables de la configuración
        self.screen = pygame.display.set_mode((config.ANCHO,config.ALTO), pygame.RESIZABLE)
        #titulo de la ventana
        pygame.display.set_caption(config.TITULO)

        #inicializamos el ResourceManager
        self.resource_manager = ResourceManager()
        self.resource_manager.load_image("fondo_prueba", "assets/images/imagen_prueba.png")


        #reloj del juego
        self.clock=pygame.time.Clock()
    def run(self):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #Testeando la entrada del teclado
                if event.type == pygame.KEYDOWN:
                    print(f"Se presionó la tecla: {pygame.key.name(event.key)}")
                if event.type == pygame.KEYUP:
                    print(f"Se soltó la tecla: {pygame.key.name(event.key)}")
                #Testeando la entrada del mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(f"Se presionó el botón del mouse: {event.button}")
                if event.type == pygame.MOUSEBUTTONUP:
                    print(f"Se soltó el botón del mouse: {event.button}")
                #Cambio de tamaño de la ventana
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    print(f"Se cambió el tamaño de la ventana: {event.w} x {event.h}")
                    self.ajustar_fondo()
            #Dibujar imagen de fondo
            self.fondo = self.resource_manager.get_image("fondo_prueba")
            self.ajustar_fondo()
            self.screen.blit(self.fondo, (0, 0))
            pygame.display.flip()
            self.clock.tick(config.FPS)
        pygame.quit()

    def ajustar_fondo(self):
        ancho_ventana, alto_ventana = self.screen.get_size()
        self.fondo = pygame.transform.scale(self.fondo, (ancho_ventana, alto_ventana))


