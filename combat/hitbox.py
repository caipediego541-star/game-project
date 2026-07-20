import pygame

class Hitbox:

    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.active = False

    def activar(self, x, y, width, height):
        self.rect.update(x, y, width, height)
        self.active = True

    def desactivar(self):
        self.active = False
        # Evita que siga colisionando
        self.rect.update(0, 0, 0, 0)

    def draw(self, screen):
       pygame.draw.rect(screen, (0,255,0), self.rect, 2)

    def colisiones(self, hurtbox):
        if not self.active:
            return False
        
        return self.rect.colliderect(hurtbox.rect)

