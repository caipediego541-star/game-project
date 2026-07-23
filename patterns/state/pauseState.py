import pygame
from patterns.state.stateBase import State
import config

class PauseState(State):
    def __init__(self, game):
        super().__init__(game)
        self.image = None

    def enter(self):
        self.image = self.game.game_screen.copy()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state_manager.return_previous_state()

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