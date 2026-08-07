from abc import ABC, abstractmethod


class GameMode(ABC):

    def __init__(self):
        self.name = "GameMode"

    @abstractmethod
    def start(self, game):
        """
        Configura el modo de juego.
        """
        pass

    @abstractmethod
    def update(self, game):
        """
        Lógica propia del modo.
        """
        pass