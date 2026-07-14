import pygame
from patterns.state.stateBase import State

class TournamentState(State):
    def __init__(self, game):
        super().__init__(game)
        
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((120, 0, 120))

        font = pygame.font.SysFont("Arial", 48)
        text = font.render("TOURNAMENT STATE", True, (255, 255, 255))

        screen.blit(text, (90, 100))