import pygame
import config

from utils.resource_loader import IMAGES
from core.resource_manager import ResourceManager

from core.state_manager import StateManager
from patterns.state.mainMenuState import MainMenuState
from patterns.state.fightState import FightState
from patterns.state.pauseState import PauseState
from patterns.state.victoryState import VictoryState
from patterns.state.torneoState import TournamentState

from patterns.factory.player.human_player_factory import HumanPlayerFactory

from core.stage import Stage
from core.control_config import ControlsConfig
from core.input_manager import InputManager



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
        self.ancho, self.alto = self.ajustar_fondo()
        self.escenario = Stage(self.alto, self.ancho)

        # State Manager
        self.state_manager = StateManager()
        self.state_manager.set_state(MainMenuState(self))

        # Jugador
        factory = HumanPlayerFactory()

        self.player1 = factory.create_player(
            self,
            "belen",
            426,
            True
        )

        self.player2 = factory.create_player(
            self,
            "profe",
            852,
            False
        )


        # Comandos
        
        self.input_manager = InputManager()

        ControlsConfig.configurar_jugador1(
            self.input_manager,
            self.player1
        )

        ControlsConfig.configurar_jugador2(
            self.input_manager,
            self.player2
        )
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

        eventos = pygame.event.get()
        for evento in eventos:

            if evento.type == pygame.QUIT:
                self.running = False

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_1:
                    self.state_manager.set_state(
                        MainMenuState(self)
                    )

                elif evento.key == pygame.K_2:
                    self.state_manager.set_state(
                        FightState(self)
                    )

                elif evento.key == pygame.K_3:
                    self.state_manager.set_state(
                        PauseState(self)
                    )

                elif evento.key == pygame.K_4:
                    self.state_manager.set_state(
                        VictoryState(self)
                    )

                elif evento.key == pygame.K_5:
                    self.state_manager.set_state(
                        TournamentState(self)
                    )

            self.input_manager.manejar_evento(evento)

        self.state_manager.handle_events(eventos)

    def update(self):
        self.input_manager.actualizar()

        self.player1.update()
        self.player2.update()

        self.state_manager.update()

    def draw(self):
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

        self.screen.fill((0,0,0))

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
            self.resource_manager.load_image(
                nombre,
                direccion
            )

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