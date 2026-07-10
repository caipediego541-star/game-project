import pygame
from patterns.state.stateBase import State
from utils.helpers import scale_image


class MainMenuState(State):

    def __init__(self, game):

        self.game = game

        self.background = (
            self.game.resource_manager.get_image(
                "menu_background"
            )
        )

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False


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