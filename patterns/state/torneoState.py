import pygame
import config

from patterns.state.stateBase import State

from combat.combat_controller import CombatController

from core.control_config import ControlsConfig

from ui.hud import HUD


class TournamentState(State):

    def __init__(self, game):

        super().__init__(game)

        self.name = "Tournament"

        self.round = 1
        self.max_rounds = 3

        self.player1_score = 0
        self.player2_score = 0

        self.player1_lives = 2
        self.player2_lives = 2

        self.combat = CombatController(game)

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

        self.combat.start_music()

    def handle_events(self, events):

        if self.game.hud:
            for event in events:
                self.game.hud.handle_event(event)

    def update(self):

        self.combat.update()

        if not self.combat.combate_terminado:
            return

        if self.combat.tiempo_victoria < self.combat.esperar_victoria:
            return

        if self.game.player1.health.dead:

            self.player2_score += 1
            self.player1_lives -= 1

            self.next_round()

        elif self.game.player2.health.dead:

            self.player1_score += 1
            self.player2_lives -= 1

            self.next_round()

    def next_round(self):

        if self.player1_score == self.max_rounds - 1:
            print("Jugador 1 gana el torneo")
            return

        if self.player2_score == self.max_rounds - 1:
            print("Jugador 2 gana el torneo")
            return

        self.round += 1

        self.reset_players()

    def reset_players(self):
       self.combat.reset_round()

    def draw(self, screen):

        fondo = pygame.transform.scale(
            self.background,
            (
                config.ANCHO,
                config.ALTO
            )
        )

        screen.blit(
            fondo,
            (0, 0)
        )

        self.combat.draw(screen)

        self.game.player1.draw(screen)

        self.game.player2.draw(screen)

        if self.game.hud:
            self.game.hud.draw(screen)