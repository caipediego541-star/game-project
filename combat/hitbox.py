import pygame

class Hitbox:
    def __init__(self):
        """Representa la zona de ataque de un personaje"""
        self.rect = pygame.Rect(0,0,0,0)
        self.active=False
    def activate(self,x,y,width,height):
        """Activa la hitbox con la posición y tamaño indicados"""
        self.rect=pygame.Rect(x,y,width,height)
        self.active=True
    def desactivate(self):
        """desactiva la hitbox"""
        self.active=False
    def draw(self,screen):
        """dibuja la hitbox unicamente para la depuracion"""
        if self.active:
            pygame.draw.rect(screen,(0,255,0),self.rect,2)


