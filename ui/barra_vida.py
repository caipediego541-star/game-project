import pygame


class BarraVida:

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

        self.x = x
        self.y = y

        self.max_width = max_width
        self.height = height

        self.invertida = invertida

    def draw(self, screen):
        porcentaje = (
            self.jugador.health /
            self.jugador.max_health
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