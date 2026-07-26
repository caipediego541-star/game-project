import pygame

from patterns.state.stateBase import State


class VictoryState(State):

    def __init__(self, game, ganador):

        super().__init__(game)

        self.ganador = ganador

        self.font = pygame.font.SysFont(
            "Arial",
            48
        )


    def handle_events(self, events):
        pass


    def update(self):
        pass


    def draw(self, screen):
        screen.fill(
            (120, 120, 0)
        )

        if self.ganador == self.game.player1:
            mensaje = "PLAYER 1 GANO"

        else:
            mensaje = "PLAYER 2 GANO"

        text = self.font.render(
            mensaje,
            True,
            (255, 255, 255)
        )
        screen.blit(
            text,
            (150, 100)
        )