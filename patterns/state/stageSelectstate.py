import pygame
import config

from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image, agregar_margen_negro
from patterns.state.torneoState import TournamentState


class StageSelectState(State):

    def __init__(self, game, modo):
        super().__init__(game)

        self.modo = modo

        self.background = self.game.resource_manager.get_image(
            "fondo_select"
        )

        self.buttons = []
        ancho_imagen = int(config.ANCHO * 0.20)
        alto_imagen = int(config.ALTO * 0.14)

        #fondos de en escenarios:

        self.imagenes_escenarios = []
        for i in range(1, 6):
            imagen = pygame.transform.scale(
                self.game.resource_manager.get_image(
                    f"fight_background{i}"),
                    (ancho_imagen, alto_imagen))
            imagen = agregar_margen_negro(
                imagen,4)
            self.imagenes_escenarios.append(imagen)
        # Posiciones
        fila1 = int(config.ALTO * 0.35)
        fila2 = int(config.ALTO * 0.68)
        fila3 = int(config.ALTO * 0.55)

        # columnas
        columna_izquierda = config.ANCHO // 4
        columna_derecha = config.ANCHO * 3 // 4
        columna_centro = config.ANCHO // 2


        # Escenario 1
        imagen_escenario1 = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_escenario1"),
            0.35
        )

        x_izquierda = (
            columna_izquierda - imagen_escenario1.get_width() // 2
        )

        x_derecha = (
            columna_derecha - imagen_escenario1.get_width() // 2
        )

        x_centro = (
            columna_centro - imagen_escenario1.get_width() // 2
        )

        self.button_escenario1 = ButtonFactory.create_button(
            image=imagen_escenario1,
            x=x_izquierda,
            y=fila1,
            action=self.seleccionar_escenario1
        )

        self.buttons.append(
            self.button_escenario1
        )


        # Escenario 2
        imagen_escenario2 = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_escenario2"),
            0.35
        )

        self.button_escenario2 = ButtonFactory.create_button(
            image=imagen_escenario2,
            x=x_derecha,
            y=fila1,
            action=self.seleccionar_escenario2
        )

        self.buttons.append(
            self.button_escenario2
        )


        # Escenario 3
        imagen_escenario3 = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_escenario3"),
            0.35
        )

        self.button_escenario3 = ButtonFactory.create_button(
            image=imagen_escenario3,
            x=x_izquierda,
            y=fila2,
            action=self.seleccionar_escenario3
        )

        self.buttons.append(
            self.button_escenario3
        )

                # Escenario 4
        imagen_escenario4 = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_escenario4"),
            0.35
        )

        self.button_escenario4 = ButtonFactory.create_button(
            image=imagen_escenario4,
            x=x_derecha,
            y=fila2,
            action=self.seleccionar_escenario4
        )

        self.buttons.append(
            self.button_escenario4
        )


        # Escenario 5
        imagen_escenario5 = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_escenario5"),
            0.35
        )

        self.button_escenario5 = ButtonFactory.create_button(
            image=imagen_escenario5,
            x=x_centro,
            y=fila3,
            action=self.seleccionar_escenario5
        )

        self.buttons.append(
            self.button_escenario5
        )

        # Volver
        imagen_volver = pygame.transform.scale_by(
            self.game.resource_manager.get_image("boton_volver"),
            0.27
        )

        x_volver = (
            config.ANCHO
            - imagen_volver.get_width()
        ) // 2

        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=x_volver,
            y=int(config.ALTO * 0.75),
            action=self.go_back
        )

        self.buttons.append(
            self.button_volver
        )


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

        x = (
            screen.get_width()
            - fondo.get_width()
        ) // 2

        y = (
            screen.get_height()
            - fondo.get_height()
        ) // 2

        screen.blit(
            fondo,
            (x, y)
        )
        #botones
        botones = [
            self.button_escenario1,
            self.button_escenario2,
            self.button_escenario3,
            self.button_escenario4,
            self.button_escenario5]
        for boton, imagen in zip(
            botones,
            self.imagenes_escenarios):
            screen.blit(imagen,(
                boton.rect.centerx - imagen.get_width() // 2,
                boton.rect.top - imagen.get_height() - 10
            ))


        

        for button in self.buttons:
            button.draw(screen)


    def seleccionar_escenario1(self):
        print("ESCENARIO 1")
        self.game.escenario_actual = "fight_background1"
        self.iniciar_modo()


    def seleccionar_escenario2(self):
        print("ESCENARIO 2")
        self.game.escenario_actual = "fight_background2"
        self.iniciar_modo()


    def seleccionar_escenario3(self):
        print("ESCENARIO 3")
        self.game.escenario_actual = "fight_background3"
        self.iniciar_modo()


    def seleccionar_escenario4(self):
        print("ESCENARIO 4")
        self.game.escenario_actual = "fight_background4"
        self.iniciar_modo()


    def seleccionar_escenario5(self):
        print("ESCENARIO 5")
        self.game.escenario_actual = "fight_background5"
        self.iniciar_modo()


    def go_back(self):
        print("VOLVER")
        from patterns.state.gamemodestate import GameModeState

        self.game.state_manager.set_state(
            GameModeState(self.game)
        )


    def iniciar_modo(self):

        self.game.modo_actual = self.modo

        if self.modo == "1vs1":
            self.game.iniciar_pelea(False)

        elif self.modo == "vsbot":
            self.game.iniciar_pelea(True)

        elif self.modo == "torneo":
            self.game.state_manager.set_state(
                TournamentState(self.game)
            )