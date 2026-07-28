import pygame
from patterns.state.stateBase import State
import config
from patterns.factory.button_factory import ButtonFactory
from patterns.state.mainMenuState import MainMenuState

class PauseState(State):
    def __init__(self, game):
        super().__init__(game)
        self.image = None
        self.buttons = []
        # Botón reanudar
        imagen_reanudar = self.game.resource_manager.get_image(
           "boton_reanudar")
        imagen_reanudar = pygame.transform.scale_by(
            imagen_reanudar,0.4)
        x_reanudar = (config.ANCHO - imagen_reanudar.get_width()) // 2
        self.button_reanudar = ButtonFactory.create_button(
            image=imagen_reanudar,x=x_reanudar,y=250,action=self.reanudar)
        self.buttons.append(self.button_reanudar)

        # Botón reiniciar
        imagen_reiniciar = self.game.resource_manager.get_image(
            "boton_reiniciar")
        imagen_reiniciar = pygame.transform.scale_by(
            imagen_reiniciar,0.4)
        x_reiniciar = (config.ANCHO - imagen_reiniciar.get_width()) // 2
        self.button_reiniciar = ButtonFactory.create_button(
            image=imagen_reiniciar,x=x_reiniciar,y=350,action=self.reiniciar)
        self.buttons.append(self.button_reiniciar)
        # Botón menú
        imagen_menu = self.game.resource_manager.get_image(
            "boton_menu")
        imagen_menu = pygame.transform.scale_by(
            imagen_menu,0.4)
        x_menu = (config.ANCHO - imagen_menu.get_width()) // 2
        self.button_menu = ButtonFactory.create_button(
            image=imagen_menu,x=x_menu,y=450,action=self.ir_menu)
        self.buttons.append(self.button_menu)

    def enter(self):
        self.image = self.game.game_screen.copy()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state_manager.return_previous_state()
            for button in self.buttons:
                button.handle_event(
                    event,self.game.get_mouse_position())
            

    def update(self):
        pass

    def draw(self, screen):
        if self.image:
            screen.blit(
                self.image,
                (0,0)
            )

        dark = pygame.Surface(
            screen.get_size()
        )

        dark.set_alpha(
            130
        )

        dark.fill(
            (0,0,0)
        )

        screen.blit(
            dark,
            (0,0)
        )

        font = pygame.font.SysFont(
            "Lucida console",
            70
        )

        text = font.render(
            "PAUSA",
            True,
            (255,255,255)
        )

        screen.blit(
            text,
            (
                config.ANCHO//2 - text.get_width()//2,
                config.ALTO//2
            )
        )
        #dibujar botones
        for button in self.buttons:
            button.draw(screen)
    def reanudar(self):
        print("REANUDAR")
        self.game.state_manager.return_previous_state()
    def reiniciar(self):
        print("REINICIAR")
        estado = self.game.state_manager.previous_state
        from patterns.state.fightState import FightState
        from patterns.state.torneoState import TournamentState
        if isinstance(estado, FightState):
            print("REINICIAR PELEA")
            self.game.state_manager.previous_state = None
            # Detectar si era bot
            if hasattr(self.game.player2, "bot_controller"):
                self.game.iniciar_pelea(True)
            else:
                self.game.iniciar_pelea(False)
        elif isinstance(estado, TournamentState):
            print("REINICIAR TORNEO")
           
    def ir_menu(self):
        print("MENU")
        
        self.game.state_manager.set_state(
        MainMenuState(self.game))