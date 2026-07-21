from abc import ABC, abstractmethod


class BotStrategy(ABC):

    @abstractmethod
    def execute(self, bot):
        pass