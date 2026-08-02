import pygame
import config

from patterns.state.stateBase import State
from combat.combat_controller import CombatController
from core.control_config import ControlsConfig
from ui.hud import HUD
from ui.question_box import QuestionBox
from patterns.state.victoryState import VictoryState
from patterns.repository.tournament_repository import TournamentRepository


class TournamentState(State):

    def __init__(self, game):

        super().__init__(game)

        self.name = "Tournament"

        self.round = 1
        self.max_rounds = 3

        self.game.fight_state = self

        self.player1_score = 0
        self.player2_score = 0

        self.player1_lives = 2
        self.player2_lives = 2

        self.repository = None
        self.torneo = None
        self.torneo_id = None

        self.combat = CombatController(game)
        self.question_box = QuestionBox(game)

    def start(self, game):

        self.repository = TournamentRepository()

        game.modo_actual = "torneo"

        if game.personaje_jugador == "belen":
            personaje_rival = "profe"
            imagen_rival = "assets/images/personajes/profe.png"
        else:
            personaje_rival = "belen"
            imagen_rival = "assets/images/personajes/belen.png"

        game.player2 = game.factory.create_player(
            game,
            personaje_rival,
            852,
            False,
            imagen_rival
        )

        # Si viene un torneo desde LoadTournamentState lo carga.
        # Si no, crea uno nuevo.
        if self.torneo is None:
            self.crear_torneo()
        else:
            self.cargar_torneo(self.torneo)

        ControlsConfig.configurar_jugador2(
            game.input_manager,
            game.player2
        )

        game.hud = HUD(game)

        self.background = game.resource_manager.get_image(
            "tournament_background"
        )

        self.combat.start_music()

        if game.escenario_actual is None:
            game.escenario_actual = "fight_background1"

    def handle_events(self, events):

        for event in events:

            if self.question_box.active:
                self.question_box.handle_event(event)
                continue

            if self.game.hud:
                self.game.hud.handle_event(event)

    def update(self):

        self.question_box.update()

        if self.question_box.active:
            return

        self.combat.update()

        if not self.combat.combate_terminado:
            return

        if self.combat.tiempo_victoria < self.combat.esperar_victoria:
            return

        if self.combat.ganador == self.game.player1:

            self.player1_score += 1
            self.player2_lives -= 1

            self.guardar_progreso()

            self.next_round()

        elif self.combat.ganador == self.game.player2:

            self.player2_score += 1
            self.player1_lives -= 1

            self.guardar_progreso()

            self.next_round()

        else:

            self.next_round()

    def next_round(self):

        if self.player1_score == self.max_rounds - 1:

            self.finalizar_torneo()

            self.game.state_manager.set_state(
                VictoryState(
                    self.game,
                    self.game.player1
                )
            )

            return

        if self.player2_score == self.max_rounds - 1:

            self.finalizar_torneo()

            self.game.state_manager.set_state(
                VictoryState(
                    self.game,
                    self.game.player2
                )
            )

            return

        self.round += 1

        self.guardar_progreso()

        self.reset_players()

        self.combat.start_music()

    def guardar_progreso(self):

        if self.torneo_id is None:
            return

        self.repository.actualizar_torneo(
            self.torneo_id,
            self.player1_score,
            self.player2_score,
            self.round,
            "EN_CURSO"
        )

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

        self.question_box.draw(screen)

    def finalizar_torneo(self):

        if self.torneo_id is None:
            return

        self.repository.finalizar_torneo(
            self.torneo_id
        )

    def cargar_torneo(self, torneo):

        self.torneo = torneo

        self.torneo_id = torneo["id"]

        self.player1_score = torneo["victorias_jugador1"]

        self.player2_score = torneo["victorias_jugador2"]

        self.round = torneo["ronda_actual"]

    def crear_torneo(self):

        self.torneo = None

        self.player1_score = 0
        self.player2_score = 0

        self.round = 1

        self.player1_lives = 2
        self.player2_lives = 2

        self.torneo_id = self.repository.crear_torneo(
            self.game.player1.character,
            self.game.player2.character
        )

    