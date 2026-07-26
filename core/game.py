import pygame
import config
from utils.resource_loader import (IMAGES, ITEMS, BOTONES, SOUNDS, FONTS)

from patterns.state.mainMenuState import MainMenuState
from patterns.state.fightState import FightState
from patterns.state.pauseState import PauseState
from patterns.state.victoryState import VictoryState
from patterns.state.torneoState import TournamentState

from patterns.factory.player.human_player_factory import HumanPlayerFactory
from patterns.factory.player.bot_player_factory import BotPlayerFactory

from patterns.strategy.easy_bot_strategy import EasyBotStrategy


from core.stage import Stage
from core.control_config import ControlsConfig

from managers.input_manager import InputManager
from managers.combat_manager import CombatManager
from managers.resource_manager import ResourceManager
from managers.item_manager import ItemManager
from managers.question_manager import QuestionManager
from managers.state_manager import StateManager

from patterns.factory.item.item_factory import ItemFactory
from patterns.singleton.sound_manager import SoundManager
from ui.hud import HUD

class Game:
   
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.game_screen = pygame.Surface(
            (
                config.ANCHO,
                config.ALTO
            )
        )

        self.screen = pygame.display.set_mode(
            (
                config.ANCHO,
                config.ALTO
            ),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(
            config.TITULO
        )

        self.resource_manager = ResourceManager()
        self.cargar_recursos()
        #cargar musica
        self.sound_manager = SoundManager()
        self.sound_manager.play_music(
             "assets/sounds/menu_music.mp3")
        self.fondo = self.resource_manager.get_image(
            "menu_background"
        )
        self.ancho = config.ANCHO
        self.alto = config.ALTO

        self.ajustar_fondo()

        self.escenario = Stage(
            self.alto,
            self.ancho
        )
        self.state_manager = StateManager()
        self.state_manager.set_state(
            MainMenuState(self)
        )

        self.factory = HumanPlayerFactory()
        self.question_manager = QuestionManager()
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

        self.item_factory = ItemFactory(
            self.resource_manager
        )

        self.item_manager = ItemManager(
            self,
            self.item_factory
        )

        self.clock = pygame.time.Clock()
        self.running = True
        self.hud = None

    def create_item_manager(self):
        return ItemManager(
            self,
            self.item_factory
        )

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(
                config.FPS
            )

        pygame.quit()

    def handle_events(self):
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                self.running = False

            if isinstance(
                self.state_manager.current_state,
                (FightState, TournamentState)
            ):
                self.input_manager.manejar_evento(
                    evento
                )
                pregunta = self.question_manager.get_question(
                    "redes"
                )

        self.state_manager.handle_events(
            eventos
        )

    def iniciar_pelea(
        self,
        contra_bot=False
    ):
        if contra_bot:
            estrategia = EasyBotStrategy()
            self.player2 = self.bot_factory.create_player(
                self,
                "profe",
                852,
                self.player1,
                False,
                "assets/images/personajes/profe.png",
                estrategia
            )
        else:
            self.player2 = self.factory.create_player(
                self,
                "profe",
                852,
                False,
                "assets/images/personajes/profe.png"
            )

            ControlsConfig.configurar_jugador2(
                self.input_manager,
                self.player2
            )

        self.hud = HUD(
            self
        )

        self.item_manager.items.clear()
        
        self.state_manager.set_state(
            FightState(self))
        

    def update(self):
        if isinstance(
            self.state_manager.current_state,
            PauseState
        ):
            self.state_manager.update()
            return

        self.input_manager.actualizar()
        self.state_manager.update()

    def draw(self):
        self.game_screen.fill(
            (0,0, 0)
        )

        self.state_manager.draw(
            self.game_screen
        )

        scaled_game = self.scale_game()

        x = (
            self.screen.get_width()
            -
            scaled_game.get_width()
        ) // 2


        y = (
            self.screen.get_height()
            -
            scaled_game.get_height()
        ) // 2

        self.screen.fill(
            (0, 0, 0 )
        )
        self.screen.blit(
            scaled_game,
            (x, y)
        )

    def ajustar_fondo(self):
        ancho, alto = self.screen.get_size()

        self.fondo = pygame.transform.scale(
            self.resource_manager.get_image(
                "menu_background")
                ,(ancho, alto)
        )


    def cargar_recursos(self):
        for nombre, direccion in IMAGES.items():
            self.resource_manager.load_image(
                nombre,
                direccion
            )

        for nombre, direccion in ITEMS.items():
            self.resource_manager.load_image(
                nombre,
                direccion
            )

        for nombre, direccion in BOTONES.items():
            self.resource_manager.load_image(
                nombre,
                direccion
            )

        for nombre, direccion in SOUNDS.items():
            self.resource_manager.load_sound(
                nombre,
                direccion
            )

        for nombre, direccion in FONTS.items():
                    self.resource_manager.load_font(
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
            (
                new_width,
                new_height
            )
        )
    def get_mouse_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        window_width, window_height = self.screen.get_size()
        scale = min(
            window_width / config.ANCHO,
            window_height / config.ALTO)

        new_width = int(config.ANCHO * scale)
        new_height = int(config.ALTO * scale)

        offset_x = (window_width - new_width) // 2
        offset_y = (window_height - new_height) // 2

        game_x = (mouse_x - offset_x) / scale
        game_y = (mouse_y - offset_y) / scale

        return (game_x,game_y)


