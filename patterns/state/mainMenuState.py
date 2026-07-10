from core.stateBase import State
import pygame
class MainMenuState(State):
    """Estado del menú principal"""
    def __init__(self, game):
        super().__init__(game)

    def handle_events(self, events):
        """Maneja los eventos del menu principal"""
        pass
    def update(self):
        """Actualiza la lógica del menú principal"""
        pass
    def draw(self,screen):
        """Dibuja el menu principal"""
        screen.fill((30,30,30))
        font=pygame.font.SysFont("Arial",48)
        text=font.render("MENU PRINCIPAL", True,(255,255,255))
        screen.blit(text,(180,100))