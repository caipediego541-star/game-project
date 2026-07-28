import pygame
import config

from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image
from patterns.state.stageSelectstate import StageSelectState
from patterns.state.stageSelectstate import StageSelectState
from patterns.state.characterSelectState import CharacterSelectState


class DifficultyState(State):

    def __init__(self, game):

        super().__init__(game)

        self.background = self.game.resource_manager.get_image(
            "fondo_select"
        )

        self.buttons = []
        #titulo dificultad
        self.font = self.game.resource_manager.get_font(
            "pixel",40)
        self.titulo = self.font.render("NIVEL DE DIFICULTAD",True,(255,255,255))
        self.titulo_rect = self.titulo.get_rect(center=(config.ANCHO // 2,170))
        # Fácil
        imagen_facil = pygame.transform.scale_by(
            self.game.resource_manager.get_image(
                "boton_facil"
            ),
            0.4
        )

        self.button_facil = ButtonFactory.create_button(
            image=imagen_facil,
            x=(config.ANCHO - imagen_facil.get_width()) // 2,
            y=210,
            action=self.elegir_facil
        )

        self.buttons.append(self.button_facil)



        # Medio
        imagen_medio = pygame.transform.scale_by(
            self.game.resource_manager.get_image(
                "boton_medio"
            ),
            0.4
        )

        self.button_medio = ButtonFactory.create_button(
            image=imagen_medio,
            x=(config.ANCHO - imagen_medio.get_width()) // 2,
            y=320,
            action=self.elegir_medio
        )

        self.buttons.append(self.button_medio)



        # Difícil
        imagen_dificil = pygame.transform.scale_by(
            self.game.resource_manager.get_image(
                "boton_dificil"
            ),
            0.4
        )

        self.button_dificil = ButtonFactory.create_button(
            image=imagen_dificil,
            x=(config.ANCHO - imagen_dificil.get_width()) // 2,
            y=430,
            action=self.elegir_dificil
        )

        self.buttons.append(self.button_dificil)



        # Volver
        imagen_volver = pygame.transform.scale_by(
            self.game.resource_manager.get_image(
                "boton_volver"
            ),
            0.27
        )

        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=(config.ANCHO - imagen_volver.get_width()) // 2,
            y=530,
            action=self.volver
        )

        self.buttons.append(self.button_volver)



    def handle_events(self, events):

        for event in events:

            if event.type == pygame.QUIT:
                self.game.running = False


            for button in self.buttons:
                button.handle_event(
                    event,
                    self.game.get_mouse_position()
                )



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
            (x,y)
        )
    
        self.draw_text_with_outline(
                screen,
                "NIVEL DE DIFICULTAD",
                self.titulo_rect,
                (255,255,255)
            )  

        for button in self.buttons:
            button.draw(screen)



    def elegir_facil(self):

        self.game.dificultad_bot = "facil"

        self.game.state_manager.set_state(
            CharacterSelectState(
                self.game,
                "vsbot"
            )
        )



    def elegir_medio(self):

        self.game.dificultad_bot = "medio"

        self.game.state_manager.set_state(
            CharacterSelectState(
                self.game,
                "vsbot"
            )
        )



    def elegir_dificil(self):

        self.game.dificultad_bot = "dificil"

        self.game.state_manager.set_state(
            CharacterSelectState(
                self.game,
                "vsbot"
            )
        )



    def volver(self):

        from patterns.state.gamemodestate import GameModeState

        self.game.state_manager.set_state(
            GameModeState(self.game)
        )

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
    