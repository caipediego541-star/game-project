import pygame

class Button:
    def __init__(self, image, x, y, action=None):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event,mouse_pos=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos is None:
                mouse_pos = event.pos
            if self.rect.collidepoint(mouse_pos):
                if self.action:
                    self.action()