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
        
        self.font = self.game.resource_manager.get_font(
                    "pixel",
                    30
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

        texto = self.font.render(
                        mensaje,
                        True,
                        (255,255,255)
                    )
        
        texto_rect = texto.get_rect(
                center=(
                    config.ANCHO // 2,100
                    
                )
            )

        self.draw_text_with_outline(
                screen,
                mensaje,
                texto_rect,
                (255,255,255)
            )  
             
        for button in self.buttons:
            button.draw(screen)
    def revancha(self):
        print("REVANCHA")
        print(self.game.modo_actual)

        if self.game.modo_actual == "torneo":
            from patterns.state.characterSelectState import CharacterSelectState
            self.game.state_manager.set_state(
             CharacterSelectState(self.game, "torneo")
        )

        elif self.game.modo_actual == "vsbot":
            self.game.iniciar_pelea(True)

        else:
            self.game.iniciar_pelea(False)
        

    def reiniciar(self):
        print("REINICIAR")
        print(self.game.modo_actual)
        if self.game.modo_actual == "torneo":
            from patterns.state.characterSelectState import CharacterSelectState
            self.game.state_manager.set_state(
                CharacterSelectState(self.game, "torneo")
            )

        elif self.game.modo_actual == "vsbot":
            self.game.iniciar_pelea(True)

        else:
            self.game.iniciar_pelea(False)
    def ir_menu(self):
        print("MENU")
        self.game.sound_manager.play_music(
            "assets/sounds/menu_music.mp3")

        self.game.state_manager.set_state(
        MainMenuState(self.game))

    def draw_text_with_outline(self, screen, text, position, color, outline_color=(0,0,0), outline=3):
            for x in range(-outline, outline + 1):
                for y in range(-outline, outline + 1):
    
                    if x != 0 or y != 0:
    
                        outline_text = self.font.render(
                            text,
                            True,
                            outline_color
                        )
    
                        screen.blit(
                            outline_text,
                            (
                                position[0] + x,
                                position[1] + y
                            )
                        )
    
    
            normal_text = self.font.render(
                text,
                True,
                color
            )
    
            screen.blit(
                normal_text,
                position
            )
    