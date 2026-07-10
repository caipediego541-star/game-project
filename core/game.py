import pygame
import config
from utils.resource_loader import IMAGES
from core.resource_manager import ResourceManager
from core.state_manager import StateManager
from patterns.state.mainMenuState import MainMenuState
from patterns.state.fightState import FightState
from patterns.state.pauseState import PauseState
from patterns.state.victoryState import VictoryState
from patterns.state.torneoState import TournamentState

class Game:
    def __init__(self):
        pygame.init()
        #creamos la ventana usando las variables de la configuración
        self.game_screen= pygame.Surface((config.ANCHO, config.ALTO))
        self.screen = pygame.display.set_mode((config.ANCHO,config.ALTO), pygame.RESIZABLE)

        #titulo de la ventana
        pygame.display.set_caption(config.TITULO)

        #inicializamos el ResourceManager
        self.resource_manager = ResourceManager()
        self.cargar_recursos()
        
        #inicializamos el StateManager
        self.state_manager = StateManager()
        self.state_manager.set_state(MainMenuState(self))

        #reloj del juego
        self.clock=pygame.time.Clock()

    def run(self):
        running = True

        while running:

            events = []

            for event in pygame.event.get():

                events.append(event)

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode(
                        (event.w, event.h),
                        pygame.RESIZABLE
                    )

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        self.state_manager.set_state(MainMenuState(self))

                    elif event.key == pygame.K_2:
                        self.state_manager.set_state(FightState(self))

                    elif event.key == pygame.K_3:
                        self.state_manager.set_state(PauseState(self))

                    elif event.key == pygame.K_4:
                        self.state_manager.set_state(VictoryState(self))

                    elif event.key == pygame.K_5:
                        self.state_manager.set_state(TournamentState(self))
                        
            self.state_manager.handle_events(events)
            self.state_manager.update()

            self.state_manager.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(config.FPS)

        pygame.quit()

    def ajustar_fondo(self):
        ancho_ventana, alto_ventana = self.screen.get_size()
        self.fondo = pygame.transform.scale(self.fondo, (ancho_ventana, alto_ventana))
    
    def cargar_recursos(self):
        for nombre, direccion in IMAGES.items():
            self.resource_manager.load_image(nombre, direccion)


