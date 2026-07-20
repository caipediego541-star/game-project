from patterns.state.stateBase import State
import pygame
import config


class FightState(State):
    def __init__(self, game):
        super().__init__(game)
        self.background= self.game.resource_manager.get_image("fight_background1")
    def handle_events(self, events):
        return super().handle_events(events)
    
    def update(self):
        pass

    def draw(self, screen):

        fondo = pygame.transform.scale(
            self.background,
            (
                config.ANCHO,
                config.ALTO
            )
        )


        screen.blit(
            fondo,
            (0,0)
        )


        self.game.player1.draw(screen)
        self.game.player2.draw(screen)