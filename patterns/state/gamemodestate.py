import pygame
from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image
from patterns.state.fightState import FightState
from patterns.state.torneoState import TournamentState

class GameModeState(State):

    def __init__(self, game):

        self.game = game
        self.background = self.game.resource_manager.get_image("menu_background")
        self.buttons = []
        #1vs1

        imagen_1vs1 = self.game.resource_manager.get_image("boton_1vs1")
        imagen_1vs1 = pygame.transform.scale_by(imagen_1vs1, 0.4)
        self.button_1vs1 = ButtonFactory.create_button(
            image=imagen_1vs1,
            x=260,
            y=80,
            action=self.start_1vs1
        )
        self.buttons.append(self.button_1vs1)
        # VS BOT
        imagen_vsbot = self.game.resource_manager.get_image("boton_vsbot")
        imagen_vsbot = pygame.transform.scale_by(imagen_vsbot, 0.4)
        self.button_vsbot = ButtonFactory.create_button(
            image=imagen_vsbot,
            x=260,
            y=230,
            action=self.start_vsbot
        )
        self.buttons.append(self.button_vsbot)
        # Torneo
        imagen_torneo = self.game.resource_manager.get_image("boton_torneo")
        imagen_torneo = pygame.transform.scale_by(imagen_torneo, 0.4)
        self.button_torneo = ButtonFactory.create_button(
            image=imagen_torneo,
            x=260,
            y=380,
            action=self.start_torneo
        )
        self.buttons.append(self.button_torneo)
        # Volver
        imagen_volver = self.game.resource_manager.get_image("boton_volver")
        imagen_volver = pygame.transform.scale_by(imagen_volver, 0.27)
        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=255,
            y=530,
            action=self.go_back
        )
        self.buttons.append(self.button_volver)


    def handle_events(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.game.running = False

            for button in self.buttons:
                button.handle_event(event)


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
        self.game.state_manager.set_state(FightState(self.game))

    def start_vsbot(self):
        print("VS BOT")
        self.game.state_manager.set_state(FightState(self.game))

    def start_torneo(self):
        print("TORNEO")
        self.game.state_manager.set_state(TournamentState(self.game))

    def go_back(self):
        print("VOLVER")
        from patterns.state.mainMenuState import MainMenuState
        self.game.state_manager.set_state(MainMenuState(self.game))