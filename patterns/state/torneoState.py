import pygame
from patterns.state.stateBase import State
from ui.hud import HUD
import config
from utils.constants import INITAL_LIVES, INVULNAERABILITY_TIME

from patterns.game_mode.game_mode import GameMode
from patterns.state.fightState import FightState

from core.control_config import ControlsConfig

class TournamentState(State):

    def __init__(self, game):
        
        
        super().__init__(game)

        self.fight = FightState(game)

        self.name = "Tournament"

        self.round = 1

        self.max_rounds = 3

        self.player1_score = 0

        self.player2_score = 0

        self.player1_lives = 2

        self.player2_lives = 2

    def start(self, game):

        game.player2 = game.factory.create_player(
            game,
            "profe",
            852,
            False,
            "assets/images/personajes/profe.png"
        )

        ControlsConfig.configurar_jugador2(
            game.input_manager,
            game.player2
        )

        game.hud = HUD(game)

        self.background = game.resource_manager.get_image(
            "tournament_background"
            )

    def update(self):
        
        self.fight.update()

        if not self.fight.combate_terminado:
            return

        if self.fight.tiempo_victoria < self.fight.esperar_victoria:
            return

        if self.fight.combate_terminado:

            if self.game.player1.health.dead:
                self.player2_score += 1
                self.player1_lives - 1
                self.next_round()
                return

            elif self.game.player2.health.dead:
                self.player1_score += 1
                self.player2_lives -1

                self.next_round()
                return

    def next_round(self):
        
        if self.player1_score == 2:

            print("Jugador 1 gana el torneo")

            return

        if self.player2_score == 2:

            print("Jugador 2 gana el torneo")

            return

        self.round += 1

        self.reset_players()

    def reset_players(self):
        
        self.game.player1.reset(
        426,
        True
        )

        self.game.player2.reset(
        852,
        False
        )
        # Crear un nuevo estado de pelea para limpiar la ronda anterior
        self.fight = FightState(self.game)

    def draw(self, screen):
        fondo = pygame.transform.scale(
            self.background,
            (config.ANCHO, config.ALTO)
    )

        screen.blit(fondo, (0, 0))

        self.game.player1.draw(screen)
        self.game.player2.draw(screen)

        if self.game.hud:
            self.game.hud.draw()

    def handle_events(self, events):
        return super().handle_events(events)
   