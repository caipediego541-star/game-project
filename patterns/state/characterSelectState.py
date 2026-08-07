import pygame
import config

from patterns.state.stateBase import State
from patterns.factory.button_factory import ButtonFactory
from utils.helpers import scale_image
from patterns.state.torneoState import TournamentState
from core.control_config import ControlsConfig

from patterns.repository.tournament_repository import TournamentRepository
from patterns.state.loadTournamentState import LoadTournamentState

class CharacterSelectState(State):

    def __init__(self, game, modo):

        super().__init__(game)

        self.modo = modo

        self.background = self.game.resource_manager.get_image(
            "fondo_select"
        )

        self.buttons = []
        self.imagen_belen = pygame.transform.scale(
            self.game.resource_manager.get_image(
                "belen"),(220, 220))
        self.imagen_profesor = pygame.transform.scale(
            self.game.resource_manager.get_image(
                "profe"),(220, 220))
        # Posiciones
        columna_izquierda = config.ANCHO // 4
        columna_derecha = config.ANCHO * 3 // 4
        fila_personajes = int(config.ALTO * 0.25)
        fila_botones = int(config.ALTO * 0.45)
        fila_volver = int(config.ALTO * 0.72)

        imagen_seleccionar = pygame.transform.scale_by(
        self.game.resource_manager.get_image(
            "boton_seleccionar"),0.30)
        self.button_belen = ButtonFactory.create_button(
            image=imagen_seleccionar,x=columna_izquierda - imagen_seleccionar.get_width() // 2, y=fila_botones,action=self.seleccionar_belen)
        self.buttons.append(self.button_belen)

        self.button_profesor = ButtonFactory.create_button(
            image=imagen_seleccionar,
            x=columna_derecha - imagen_seleccionar.get_width() // 2,
            y=fila_botones,
            action=self.seleccionar_profesor)
        self.buttons.append(self.button_profesor)


        imagen_volver = pygame.transform.scale_by(
        self.game.resource_manager.get_image(
            "boton_volver"),0.27)

        
        self.button_volver = ButtonFactory.create_button(
            image=imagen_volver,
            x=(config.ANCHO - imagen_volver.get_width()) // 2,
            y=fila_volver,
            action=self.volver)
        self.buttons.append(
            self.button_volver)

        
    def seleccionar_belen(self):

        print("BELEN SELECCIONADO")

        self.game.personaje_jugador = "belen"
        self.continuar()


    def seleccionar_profesor(self):

        self.game.personaje_jugador = "profe"

        self.continuar()
    def continuar(self):
        if self.modo == "torneo":
            self.game.modo_actual = "torneo"
            self.game.player1 = self.game.factory.create_player(
                self.game,self.game.personaje_jugador,426,True,
                f"assets/images/personajes/{self.game.personaje_jugador}.png")
            
            ControlsConfig.configurar_jugador1(
                self.game.input_manager,self.game.player1)
            
            repository = TournamentRepository()

            torneo = repository.obtener_torneo()

            if torneo:

                self.game.state_manager.set_state(
                    LoadTournamentState(
                        self.game,
                        torneo
                    )
                )

            else:

                self.game.state_manager.set_state(
                    TournamentState(
                        self.game, 
                    )
                )
        else:
            from patterns.state.stageSelectstate import StageSelectState
            self.game.state_manager.set_state(
                StageSelectState(
                    self.game,self.modo))

    def volver(self):
        if self.modo == "vsbot":
            from patterns.state.difficultyState import DifficultyState
            self.game.state_manager.set_state(
                DifficultyState(self.game))
        else: 
            from patterns.state.gamemodestate import GameModeState
            self.game.state_manager.set_state(
                GameModeState(self.game))


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

        y = ( screen.get_height() - fondo.get_height()) // 2


        screen.blit(
            fondo,
            (x, y))


        # personajes

        screen.blit(
            self.imagen_belen,
            (
                config.ANCHO // 4 - self.imagen_belen.get_width() // 2,
                int(config.ALTO * 0.20)))


        screen.blit(
            self.imagen_profesor,
            (
                config.ANCHO * 3 // 4 - self.imagen_profesor.get_width() // 2,
                int(config.ALTO * 0.20)))


        # botones

        for button in self.buttons:
            button.draw(screen)