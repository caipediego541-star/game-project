import pygame
import config
from entities.player import Player

from patterns.command.player.move_left import MoveLeftCommand
from patterns.command.player.move_right import MoveRightCommand
from patterns.command.player.move_jump import JumpCommand


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((config.ANCHO, config.ALTO))

        pygame.display.set_caption(config.TITULO)

        self.clock = pygame.time.Clock()

        self.running = True

        # Jugador
        self.player = Player()

        # Diccionario de comandos
        self.commands = {

            pygame.K_a: MoveLeftCommand(self.player),

            pygame.K_d: MoveRightCommand(self.player),

            pygame.K_SPACE: JumpCommand(self.player)
        }

    def handle_events(self):

    # Eventos que ocurren una sola vez
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.commands[event.key].execute()

    # Movimiento continuo
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.commands[pygame.K_a].execute()

        if keys[pygame.K_d]:
            self.commands[pygame.K_d].execute()

    def update(self):
        self.player.update()

    def draw(self):

        self.screen.fill((30,30,30))

        self.player.draw(self.screen)

        pygame.display.flip()

    def run(self):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)
            
        pygame.quit()
    

    


   


