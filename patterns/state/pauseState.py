import pygame
from core.stateBase import State

class PauseState(State):
    def __init__(self, game):
        super().__init__(game)
        
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((30, 30, 120))

        font = pygame.font.SysFont("Arial", 48)
        text = font.render("PAUSE STATE", True, (255, 255, 255))

        screen.blit(text, (170, 100))