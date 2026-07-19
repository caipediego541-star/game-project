from abc import ABC, abstractmethod

class PlayerFactory(ABC):

    @abstractmethod
    def create_player(self, game, character, x, facing_right):
        pass