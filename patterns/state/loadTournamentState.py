import pygame
import config

from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from patterns.state.torneoState import TournamentState
from patterns.repository.tournament_repository import TournamentRepository


class LoadTournamentState(State):

    def __init__(self, game, torneo):
        super().__init__(game)

        self.game = game
        self.torneo = torneo
        self.repository = TournamentRepository()

        # Fondo
        self.background = self.game.resource_manager.get_image(
            "fondo_select"
        )

        # Imagen del mensaje
        self.question_image = self.game.resource_manager.get_image(
            "load_tournament"
        )
        self.question_image = pygame.transform.scale_by(
            self.question_image,
            0.35
        )

        # Botón SI
        imagen_si = self.game.resource_manager.get_image(
            "button_yes"
        )
        imagen_si = pygame.transform.scale_by(
            imagen_si,
            0.35
        )

        # Botón NO
        imagen_no = self.game.resource_manager.get_image(
            "button_no"
        )
        imagen_no = pygame.transform.scale_by(
            imagen_no,
            0.35
        )

        self.x_mensaje = (
            config.ANCHO - self.question_image.get_width()
        ) // 2

        self.y_mensaje = 80

        separacion = 80

        x_si = (
            config.ANCHO // 2
        ) - imagen_si.get_width() - (separacion // 2)

        x_no = (
            config.ANCHO // 2
        ) + (separacion // 2)

        y_botones = 400

        self.btn_si = ButtonFactory.create_button(
            image=imagen_si,
            x=x_si,
            y=y_botones,
            action=self.click_si
        )

        self.btn_no = ButtonFactory.create_button(
            image=imagen_no,
            x=x_no,
            y=y_botones,
            action=self.click_no
        )

    def click_si(self):

        torneo_state = TournamentState(self.game)

        torneo_state.torneo = self.torneo

        self.game.state_manager.set_state(
            torneo_state
        )

    def click_no(self):

        self.repository.eliminar_torneo(
            self.torneo["id"]
        )

        torneo_state = TournamentState(self.game)

        self.game.state_manager.set_state(
            torneo_state
        )

    def handle_events(self, events):

        for event in events:

            self.btn_si.handle_event(
                event,
                self.game.get_mouse_position()
            )

            self.btn_no.handle_event(
                event,
                self.game.get_mouse_position()
            )

    def update(self):
        pass

    def draw(self, screen):

        fondo = pygame.transform.scale(
            self.background,
            (
                config.ANCHO,
                config.ALTO
            )
        )

        screen.blit(
            fondo,
            (0, 0)
        )

        screen.blit(
            self.question_image,
            (
                self.x_mensaje,
                self.y_mensaje
            )
        )

        self.btn_si.draw(screen)
        self.btn_no.draw(screen)
        