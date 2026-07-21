import pygame
class Hurtbox:
    """"representa la zona del personaje que puede recibir daño, zona vulnerable"""
    def __init__(self,x,y,width,height):
        """crea la hurtbox con una sola posicion y un tamaño inicial"""
        self.rect=pygame.Rect(x,y,width,height)
    def update(self,x,y,width,height):
        """actualiza la psosicion y el tamaño de la hurtbox"""
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
    def draw(self,screen):
        """dibuja la hurtbox (solo para depuracion)"""
        pygame.draw.rect(screen,(255,0,0),self.rect,2)