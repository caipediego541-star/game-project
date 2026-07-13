import pygame
import config
from core.resource_manager import ResourceManager
from entities.player import Player

from patterns.command.player.move_left import MoveLeftCommand
from patterns.command.player.move_right import MoveRightCommand
from patterns.command.player.move_jump import JumpCommand
from patterns.command.player.punch import PunchCommand
from patterns.command.player.kick import KickCommand
from patterns.command.player.block import BlockCommand


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

        #sistema de controles
        self.running = True

        # Jugador
        self.player = Player()

        # Diccionario de comandos
        self.commands = {

            pygame.K_a: MoveLeftCommand(self.player),

            pygame.K_d: MoveRightCommand(self.player),

            pygame.K_SPACE: JumpCommand(self.player),

            pygame.K_j: PunchCommand(self.player),
            
            pygame.K_k: KickCommand(self.player),
            
            pygame.K_l: BlockCommand(self.player)
        }
    def run(self):
        self.running = True
        while self.running: 
           self.handle_events()
           self.update()
           #dibujar fondo
           self.fondo = self.resource_manager.get_image("fondo_prueba")
           self.ajustar_fondo()
           self.screen.blit(self.fondo, (0, 0))
           self.draw()

           pygame.display.flip()
           self.clock.tick(config.FPS)
        pygame.quit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            #testeando la entrada del teclado
            elif event.type == pygame.KEYDOWN:
                print(f"Se presionó la tecla: {pygame.key.name(event.key)}")
                if event.key in (
                 pygame.K_SPACE,
                  pygame.K_j,
                  pygame.K_k,
                  pygame.K_l
                ):
                 self.commands[event.key].execute()
                    
            elif event.type == pygame.KEYUP:
                print(f"Se soltó la tecla: {pygame.key.name(event.key)}")
            #testeando la entrada del mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Se presionó el botón del mouse: {event.button}")
            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Se soltó el botón del mouse: {event.button}")
            #cambio de tamaño de la ventana
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                print(f"Se cambió el tamaño de la ventana: {event.w} x {event.h}")
                self.ajustar_fondo()
        # movimiento continuo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.commands[pygame.K_a].execute()
        if keys[pygame.K_d]:
            self.commands[pygame.K_d].execute()
    def update(self):
        self.player.update()

    def draw(self):

        self.player.draw(self.screen)

    def ajustar_fondo(self):
        ancho_ventana, alto_ventana = self.screen.get_size()
        self.fondo = pygame.transform.scale(self.fondo, (ancho_ventana, alto_ventana))
    

    


   


