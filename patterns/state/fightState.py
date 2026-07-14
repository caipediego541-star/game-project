from patterns.state.stateBase import State
import pygame
from utils.helpers import scale_image

class FightState(State):
    def __init__(self, game):
        super().__init__(game)
        self.background= self.game.resource_manager.get_image("fight_background1")
    def handle_events(self, events):
        return super().handle_events(events)
    
    def update(self):
        pass

    def draw(self, screen):

        fondo = scale_image(
            self.background,
            screen
        )

        x = (screen.get_width() - fondo.get_width()) // 2
        y = (screen.get_height() - fondo.get_height()) // 2

        screen.blit(
            fondo,
            (x, y)
        )

        self.game.player.draw(screen)