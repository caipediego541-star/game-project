from ui.hud import HUD

from patterns.game_mode.game_mode import GameMode
from patterns.state.fightStateBot import FightStateBot

from patterns.strategy.hard_bot_strategy import HardBotStrategy


class PvEMode(GameMode):

    def __init__(self):
        super().__init__()
        self.name = "PvE"

    def start(self, game):

        game.state_manager.set_state(
            FightStateBot(game)
        )

        estrategia = HardBotStrategy()

        game.player2 = game.bot_factory.create_player(
            game,
            "profe",
            852,
            game.player1,
            False,
            "assets/images/personajes/profe.png",
            estrategia
        )

        game.hud = HUD(game)

        game.set_background("bot_background")

    def update(self, game):
        pass