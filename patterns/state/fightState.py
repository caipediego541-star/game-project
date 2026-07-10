from patterns.state.stateBase import State
import pygame

class FightState(State):
    def __init__(self, game):
        super().__init__(game)
    def handle_events(self, events):
        return super().handle_events(events)
    
    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 120, 0))

        font = pygame.font.SysFont("Arial", 48)
        text = font.render("FIGHT STATE", True, (255, 255, 255))

        screen.blit(text, (180, 100))