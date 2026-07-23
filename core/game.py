import pygame
import config

from utils.resource_loader import IMAGES
from ui.hud import HUD

from managers.state_manager import StateManager
from patterns.state.mainMenuState import MainMenuState
from patterns.state.fightState import FightState
from patterns.state.pauseState import PauseState
from patterns.state.victoryState import VictoryState
from patterns.state.torneoState import TournamentState
from patterns.state.fightStateBot import FightStateBot

from patterns.factory.player.human_player_factory import HumanPlayerFactory
from patterns.factory.player.bot_player_factory import BotPlayerFactory

from patterns.strategy.easy_bot_strategy import EasyBotStrategy
from patterns.strategy.hard_bot_strategy import HardBotStrategy
from patterns.strategy.medium_bot_strategy import MediumBotStrategy

from core.stage import Stage
from core.control_config import ControlsConfig

from managers.input_manager import InputManager
from managers.combat_manager import CombatManager
from managers.resource_manager import ResourceManager

class Game:
   
    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        self.game_screen = pygame.Surface(
            (config.ANCHO, config.ALTO)
        )

        self.screen = pygame.display.set_mode(
            (config.ANCHO, config.ALTO),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(config.TITULO)

        self.resource_manager = ResourceManager()
        self.cargar_recursos()
        #cargar musica
        pygame.mixer.music.load("assets/sounds/menu_music.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.fondo = self.resource_manager.get_image(
            "menu_background"
        )

        self.ancho, self.alto = self.ajustar_fondo()

        self.escenario = Stage(
            self.alto,
            self.ancho
        )

        self.state_manager = StateManager()
        self.state_manager.set_state(
            MainMenuState(self)
        )

        self.factory = HumanPlayerFactory()
        self.bot_factory = BotPlayerFactory()

        self.player1 = self.factory.create_player(
            self,
            "belen",
            426,
            True,
            "assets/images/personajes/belen.png"
        )

        self.player2 = None
        self.combat_manager = CombatManager()
        self.input_manager = InputManager()
        ControlsConfig.configurar_jugador1(
            self.input_manager,
            self.player1
        )

        self.clock = pygame.time.Clock()
        self.running = True
        self.hud = None

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
                    self.player2 = self.factory.create_player(
                        self,
                        "profe",
                        852,
                        False,
                        "assets/images/personajes/profe.png"
                    )

                    self.hud = HUD(self)

                    ControlsConfig.configurar_jugador2(
                        self.input_manager,
                        self.player2
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

                elif evento.key == pygame.K_6:
                    self.state_manager.set_state(
                        FightStateBot(self)
                    )

                    estrategia = HardBotStrategy()

                    self.player2 = self.bot_factory.create_player(
                        self,
                        "profe",
                        852,
                        self.player1,
                        False,
                        "assets/images/personajes/profe.png",
                        estrategia
                    )

                    self.hud = HUD(self)

            if isinstance(
                self.state_manager.current_state,
                (FightState, FightStateBot)
            ):

                self.input_manager.manejar_evento(
                    evento
                )
        self.state_manager.handle_events(
            eventos
        )

    def update(self):
        self.input_manager.actualizar()
        self.player1.update()
        if self.player2:
            self.player2.update()
            self.combat_manager.check_collision(
                self.player1,
                self.player2
            )

        self.state_manager.update()

    def draw(self):

        self.game_screen.fill(
            (0,0,0)
        )

        self.state_manager.draw(
            self.game_screen
        )

        scaled_game = self.scale_game()

        x = (
            self.screen.get_width()
            - scaled_game.get_width()
        ) // 2

        y = (
            self.screen.get_height()
            - scaled_game.get_height()
        ) // 2

        self.screen.fill(
            (0,0,0)
        )
        self.screen.blit(
            scaled_game,
            (x,y)
        )

    def ajustar_fondo(self):
        ancho, alto = self.screen.get_size()
        self.fondo = pygame.transform.scale(
            self.resource_manager.get_image(
                "menu_background"
            ),
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

        scale = min(
            window_width / config.ANCHO,
            window_height / config.ALTO
        )

        new_width = int(
            config.ANCHO * scale
        )

        new_height = int(
            config.ALTO * scale
        )

        return pygame.transform.scale(
            self.game_screen,
            (new_width, new_height)
        )