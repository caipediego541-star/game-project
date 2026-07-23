import pygame

class Hurtbox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def update(self, x, y, width, height):
        self.rect.update(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)