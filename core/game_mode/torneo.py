from ui.hud import HUD

from core.game_mode.game_mode import GameMode
from patterns.state.fightState import FightState

from core.control_config import ControlsConfig


class TournamentMode(GameMode):

    def __init__(self):

        super().__init__()

        self.name = "Tournament"

        self.round = 1

        self.max_rounds = 3

        self.player1_score = 0

        self.player2_score = 0

    def start(self, game):

        game.state_manager.set_state(
            FightState(game)
        )

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

        game.set_background("tournament_background")

    def update(self, game):

        if not game.player2:
            return

        if game.player1.health.dead:

            self.player2_score += 1

            self.next_round(game)

        elif game.player2.health.dead:

            self.player1_score += 1

            self.next_round(game)

    def next_round(self, game):

        if self.player1_score == 2:

            print("Jugador 1 gana el torneo")

            return

        if self.player2_score == 2:

            print("Jugador 2 gana el torneo")

            return

        self.round += 1

        self.reset_players(game)

    def reset_players(self, game):

        game.player1.health.reset()

        game.player2.health.reset()

        game.player1.x = 426

        game.player2.x = 852

        game.player1.y = game.player1.ground

        game.player2.y = game.player2.ground

        game.player1.busy = False

        game.player2.busy = False

        game.player1.blocking = False

        game.player2.blocking = False

        game.player1.change_animation("idle")

        game.player2.change_animation("idle")

    def update(self, game):
        pass