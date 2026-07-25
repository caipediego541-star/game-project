import pygame
import config
from patterns.state.stateBase import State
from utils.helpers import scale_image
from patterns.factory.button_factory import ButtonFactory



class MainMenuState(State):

    def __init__(self, game):

        self.game = game

        self.background = (
            self.game.resource_manager.get_image(
                "menu_background"
            )
        )
        self.buttons = []
        #boton de jugar
        imagen_boton = self.game.resource_manager.get_image("boton_jugar")
        imagen_boton = pygame.transform.scale_by(imagen_boton,0.4)
        separacion = 10
        x_jugar = (config.ANCHO - imagen_boton.get_width()) // 2
        y_jugar = 180
        y_opciones = y_jugar + imagen_boton.get_height() + separacion
        y_salir = y_opciones + imagen_boton.get_height() + separacion - 70
        self.play_button = ButtonFactory.create_button(
            image=imagen_boton,
            x=x_jugar,
            y=y_jugar,
            action=self.start_game
        )
        self.buttons.append(self.play_button)
        #boton opciones
        imagen_opciones = self.game.resource_manager.get_image("boton_opciones")
        imagen_opciones = pygame.transform.scale_by(imagen_opciones, 0.4)
        x_opciones = (config.ANCHO - imagen_opciones.get_width()) // 2 + 12
        self.options_button = ButtonFactory.create_button(
            image=imagen_opciones,
            x=x_opciones,
            y=y_opciones,
            action=self.options
        )
        self.buttons.append(self.options_button)
        
        #boton salir
        imagen_salir = self.game.resource_manager.get_image("boton_salir")
        imagen_salir = pygame.transform.scale_by(imagen_salir, 0.4)
        x_salir = (config.ANCHO - imagen_salir.get_width()) // 2 + 4
        self.exit_button = ButtonFactory.create_button(
            image=imagen_salir,
            x=x_salir,
            y=y_salir,
            action=self.exit_game
        )
        self.buttons.append(self.exit_button)
        print("jugar", self.play_button.rect)
        print("opciones", self.options_button.rect)
        print("salir", self.exit_button.rect)

    def handle_events(self, events):

        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            for button in self.buttons:
                button.handle_event(event,self.game.get_mouse_position())



    def update(self):
        pass


    def draw(self, screen):

        fondo = scale_image(
            self.background,
            screen
        )

        x = (screen.get_width() - fondo.get_width()) // 2
        y = (screen.get_height() - fondo.get_height()) // 2

        screen.blit(
            fondo,
            (x, y)
        )
        for button in self.buttons:
            button.draw(screen)
            
    def start_game(self):
         from patterns.state.gamemodestate import GameModeState
         self.game.state_manager.set_state(GameModeState(self.game))


    def options(self):
        print("BOTON OPCIONES PRESIONADO")
        from patterns.state.optionsState import OptionsState
        self.game.state_manager.set_state(OptionsState(self.game))

    def exit_game(self):
        print("BOTON SALIR PRESIONADO")
        pygame.quit()
        exit()
    