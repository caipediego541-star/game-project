from ui.hud import HUD

from core.game_mode.game_mode import GameMode
from patterns.state.fightState import FightState

from core.control_config import ControlsConfig


class PvPMode(GameMode):

    def __init__(self):
        super().__init__()
        self.name = "PvP"

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

        game.set_background("pvp_background")

    def update(self, game):
        pass