import pygame
from patterns.observer.observer import Observer

class BarraVida(Observer):

    def __init__(
        self,
        jugador,
        x,
        y,
        max_width,
        height,
        invertida=False
    ):

        self.jugador = jugador
        self.health = jugador.health.health
        self.max_health = jugador.health.max_health
        self.x = x
        self.y = y

        self.max_width = max_width
        self.height = height

        self.invertida = invertida

    def draw(self, screen):
        porcentaje = (
            self.health /
            self.max_health
        )

        ancho_actual = self.max_width * porcentaje

        if not self.invertida:

            pygame.draw.rect(
                screen,
                (135, 96, 147),
                (
                    self.x,
                    self.y,
                    ancho_actual,
                    self.height
                )
            )

        else:

            pygame.draw.rect(
                screen,
                (135, 96, 147),
                (
                    self.x + self.max_width - ancho_actual,
                    self.y,
                    ancho_actual,
                    self.height
                )
            )

    def on_notify(self, subject, event):
        self.health = subject.health
        self.max_health = subject.max_health