import pygame
import config
from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from patterns.state.mainMenuState import MainMenuState


class VictoryState(State):

    def __init__(self, game, ganador):

        super().__init__(game)

        self.ganador = ganador
        self.image = None
        
        self.font = pygame.font.SysFont(
            "Arial",
            48
        )
        self.buttons = []
        # Botón revancha
        imagen_revancha = self.game.resource_manager.get_image(
            "boton_revancha")
        imagen_revancha = pygame.transform.scale_by(
            imagen_revancha,0.4)
        x_revancha = (
            config.ANCHO - imagen_revancha.get_width()) // 2
        self.button_revancha = ButtonFactory.create_button(
            image=imagen_revancha,x=x_revancha,y=250,action=self.revancha)
        self.buttons.append(
            self.button_revancha)
        # Botón reiniciar
        imagen_reiniciar = self.game.resource_manager.get_image(
            "boton_reiniciar")
        imagen_reiniciar = pygame.transform.scale_by(
            imagen_reiniciar,0.4)
        x_reiniciar = (config.ANCHO - imagen_reiniciar.get_width()) // 2
        self.button_reiniciar = ButtonFactory.create_button(
            image=imagen_reiniciar,x=x_reiniciar, y=350,action=self.reiniciar)
        self.buttons.append(
            self.button_reiniciar)
        # Botón menu
        imagen_menu = self.game.resource_manager.get_image(
            "boton_menu")
        imagen_menu = pygame.transform.scale_by(
            imagen_menu,0.4)
        x_menu = (
            config.ANCHO - imagen_menu.get_width()) // 2
        self.button_menu = ButtonFactory.create_button(
            image=imagen_menu,x=x_menu,y=450,action=self.ir_menu)
        self.buttons.append(
            self.button_menu)
    def enter(self):
        self.image = self.game.game_screen.copy()
    def handle_events(self, events):
        for event in events:
            for button in self.buttons:
                button.handle_event(
                    event,self.game.get_mouse_position())


    def update(self):
        pass


    def draw(self, screen):
        if self.image:
            screen.blit(
                self.image,(0,0))
        # capa oscura arriba del escenario
        dark = pygame.Surface(
            screen.get_size())
        dark.set_alpha(130)
        dark.fill((0,0,0))
        screen.blit(
            dark,(0,0))
        if self.ganador == self.game.player1:
            mensaje = "PLAYER 1 GANO"

        else:
            mensaje = "PLAYER 2 GANO"

        text = self.font.render(
            mensaje,
            True,
            (255, 255, 255)
        )
        screen.blit(
            text,
            (150, 100)
        )
        for button in self.buttons:
            button.draw(screen)
    def revancha(self):
        print("REVANCHA")
        self.game.player1.reset()
        if self.game.player2:
            self.game.player2.reset()
        self.game.iniciar_pelea(False)

    def reiniciar(self):
        print("REINICIAR")
        self.game.player1.reset()

        if self.game.player2:
            self.game.player2.reset()
            
        self.game.iniciar_pelea(False)
    def ir_menu(self):
        print("MENU")
        self.game.state_manager.set_state(
        MainMenuState(self.game))