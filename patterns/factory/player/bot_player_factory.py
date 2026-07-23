from entities.bot_player import BotPlayer
from patterns.factory.player.player_factory import PlayerFactory


class BotPlayerFactory(PlayerFactory):

    def create_player(self, game, character, x, enemy, facing_right, profile_picture, strategy):
        return BotPlayer(game, character, x, enemy, facing_right, profile_picture, strategy)