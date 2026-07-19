from entities.player import Player
from patterns.factory.player.player_factory import PlayerFactory

class HumanPlayerFactory(PlayerFactory):

    def create_player(self, game, character, x, facing_right):

        return Player(game, character, x, facing_right)