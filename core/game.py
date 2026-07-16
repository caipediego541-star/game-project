import pygame
import config

from utils.resource_loader import IMAGES
from core.resource_manager import ResourceManager
from entities.player import Player

from patterns.command.player.move_left import MoveLeftCommand
from patterns.command.player.move_right import MoveRightCommand
from patterns.command.player.move_jump import JumpCommand
from patterns.command.player.punch import PunchCommand
from patterns.command.player.kick import KickCommand
from patterns.command.player.block import BlockCommand

from core.state_manager import StateManager
from patterns.state.mainMenuState import MainMenuState
from patterns.state.fightState import FightState
from patterns.state.pauseState import PauseState
from patterns.state.victoryState import VictoryState
from patterns.state.torneoState import TournamentState

from core.stage import Stage


class Game:

    def __init__(self):

        pygame.init()

        self.game_screen = pygame.Surface((config.ANCHO, config.ALTO))
        self.screen = pygame.display.set_mode(
            (config.ANCHO, config.ALTO),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(config.TITULO)

        # Resource Manager
        self.resource_manager = ResourceManager()
        self.cargar_recursos()

        # Fondo
        self.fondo = self.resource_manager.get_image("menu_background")
        self.ancho, self.alto =self.ajustar_fondo()
        self.escenario = Stage(self.alto, self.ancho)

        # State Manager
        self.state_manager = StateManager()
        self.state_manager.set_state(MainMenuState(self))

        # Jugador
        self.player = Player(self)

        # Comandos
        self.commands = {
            pygame.K_a: MoveLeftCommand(self.player),
            pygame.K_d: MoveRightCommand(self.player),
            pygame.K_SPACE: JumpCommand(self.player),
            pygame.K_j: PunchCommand(self.player),
            pygame.K_k: KickCommand(self.player),
            pygame.K_l: BlockCommand(self.player)
        }

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):

        self.running = True

        while self.running:

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(config.FPS)

        pygame.quit()

    def handle_events(self):

        events = []

        for event in pygame.event.get():

            events.append(event)

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:

                print(f"Se presionó la tecla: {pygame.key.name(event.key)}")

                if event.key == pygame.K_1:
                    self.state_manager.set_state(MainMenuState(self))

                elif event.key == pygame.K_2:
                    self.state_manager.set_state(FightState(self))

                elif event.key == pygame.K_3:
                    self.state_manager.set_state(PauseState(self))

                elif event.key == pygame.K_4:
                    self.state_manager.set_state(VictoryState(self))

                elif event.key == pygame.K_5:
                    self.state_manager.set_state(TournamentState(self))

                elif event.key in (
                    pygame.K_SPACE,
                    pygame.K_j,
                    pygame.K_k,
                    pygame.K_l
                ):
                    self.commands[event.key].execute()

            elif event.type == pygame.KEYUP:
                print(f"Se soltó la tecla: {pygame.key.name(event.key)}")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Se presionó el botón del mouse: {event.button}")

            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Se soltó el botón del mouse: {event.button}")

            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(
                    (event.w,event.h),
                    pygame.RESIZABLE
    )

        # Movimiento continuo
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.commands[pygame.K_a].execute()

        if keys[pygame.K_d]:
            self.commands[pygame.K_d].execute()

        if not keys[pygame.K_a] and not keys[pygame.K_d] and not self.player.jumping:
            self.player.current_animation = "caminar"
        # Delegar eventos al estado actual
        self.state_manager.handle_events(events)

    def update(self):

        self.player.update()
        self.state_manager.update()

    def draw(self):

        # Limpiar pantalla interna
        self.game_screen.fill((0,0,0))
        self.state_manager.draw(
            self.game_screen
        )


        # Escalar todo el juego
        scaled_game = self.scale_game()


        # Centrar
        x = (
            self.screen.get_width()
            - scaled_game.get_width()
        ) // 2

        y = (
            self.screen.get_height()
            - scaled_game.get_height()
        ) // 2


        # Limpiar ventana real
        self.screen.fill((0,0,0))


        # Dibujar juego escalado
        self.screen.blit(
            scaled_game,
            (x,y)
        )

    def ajustar_fondo(self):

        ancho, alto = self.screen.get_size()

        self.fondo = pygame.transform.scale(
            self.resource_manager.get_image("menu_background"),
            (ancho, alto)
        )
        return ancho, alto

    def cargar_recursos(self):

        for nombre, direccion in IMAGES.items():
            self.resource_manager.load_image(nombre, direccion)

    def scale_game(self):

        window_width, window_height = self.screen.get_size()

        game_width = config.ANCHO
        game_height = config.ALTO


        scale = min(
            window_width / game_width,
            window_height / game_height
        )


        new_width = int(game_width * scale)
        new_height = int(game_height * scale)


        scaled = pygame.transform.scale(
            self.game_screen,
            (new_width, new_height)
        )


        return scaled