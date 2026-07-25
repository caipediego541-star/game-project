import pygame
import config
from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image
from patterns.state.torneoState import TournamentState

class GameModeState(State):

    def __init__(self, game):

        self.game = game
        self.background = self.game.resource_manager.get_image("menu_background")
        self.buttons = []

        separacion = 20

        #1vs1

        imagen_1vs1 = self.game.resource_manager.get_image("boton_1vs1")
        imagen_1vs1 = pygame.transform.scale_by(imagen_1vs1, 0.4)
        x_1vs1 = (config.ANCHO - imagen_1vs1.get_width()) // 2
        self.button_1vs1 = ButtonFactory.create_button(
            image=imagen_1vs1,
            x=x_1vs1,
            y=120,
            action=self.start_1vs1
        )
        self.buttons.append(self.button_1vs1)
        # VS BOT
        imagen_vsbot = self.game.resource_manager.get_image("boton_vsbot")
        imagen_vsbot = pygame.transform.scale_by(imagen_vsbot, 0.4)
        x_vsbot = (config.ANCHO - imagen_vsbot.get_width()) // 2
        self.button_vsbot = ButtonFactory.create_button(
            image=imagen_vsbot,
            x=x_vsbot,
            y=260,
            action=self.start_vsbot
        )
        self.buttons.append(self.button_vsbot)
        # Torneo
        imagen_torneo = self.game.resource_manager.get_image("boton_torneo")
        imagen_torneo = pygame.transform.scale_by(imagen_torneo, 0.4)
        x_torneo = (config.ANCHO - imagen_torneo.get_width()) // 2
        self.button_torneo = ButtonFactory.create_button(
            image=imagen_torneo,
            x=x_torneo,
            y=400,
            action=self.start_torneo
        )
        self.buttons.append(self.button_torneo)
        # Volver
        imagen_volver = self.game.resource_manager.get_image("boton_volver")
        imagen_volver = pygame.transform.scale_by(imagen_volver, 0.27)
        x_volver = (config.ANCHO - imagen_volver.get_width()) // 2
        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=x_volver,
            y=530,
            action=self.go_back
        )
        self.buttons.append(self.button_volver)


    def handle_events(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.game.running = False

            for button in self.buttons:
                button.handle_event(event,self.game.get_mouse_position())


    def update(self):
        pass


    def draw(self, screen):

        fondo = scale_image(self.background, screen)
        x = (screen.get_width() - fondo.get_width()) // 2
        y = (screen.get_height() - fondo.get_height()) // 2

        screen.blit(fondo, (x, y))

        for button in self.buttons:
            button.draw(screen)
    
    def start_1vs1(self):
        print("1 VS 1")
        self.game.iniciar_pelea(False)
        

    def start_vsbot(self):
        print("VS BOT")
        self.game.iniciar_pelea(True)
       

    def start_torneo(self):
        print("TORNEO")
        self.game.state_manager.set_state(TournamentState(self.game))

    def go_back(self):
        print("VOLVER")
        from patterns.state.mainMenuState import MainMenuState
        self.game.state_manager.set_state(MainMenuState(self.game))