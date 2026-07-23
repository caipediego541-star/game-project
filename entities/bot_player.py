from entities.player import Player
from entities.bot_controller import BotController

class BotPlayer(Player):
    def __init__(self, game, character, x, enemy, facing_right, profile_picture, strategy):
        super().__init__(game, character, x, facing_right, profile_picture)
        self.bot_controller = BotController(
            self,
            enemy,
            strategy
        )

    def update(self):
        super().update()
        self.bot_controller.update()