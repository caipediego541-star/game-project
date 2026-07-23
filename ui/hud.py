import pygame
import config
from ui.barra_vida import BarraVida

class HUD:

    def __init__(self, game):
        self.game = game
        self.hud_width = 570
        self.hud_height = 170

        self.hud_image = pygame.transform.scale(
            self.game.resource_manager.get_image("hud"),
            (
                self.hud_width,
                self.hud_height
            )
        )

        self.hud_flip = pygame.transform.flip(
            self.hud_image,
            True,
            False
        )

        self.inventario_image = pygame.transform.scale(
            self.game.resource_manager.get_image("inventario"),
            (150, 60)
        )

        self.boton_pausa = pygame.transform.scale(
            self.game.resource_manager.get_image("pausa"),
            (50, 50)
        )

        self.barra_jugador1 = BarraVida(
            jugador=self.game.player1,
            x=180,
            y=83,
            max_width=400,
            height=40
        )

        self.game.player1.health.add_observer(
            self.barra_jugador1
        )

        self.barra_jugador2 = None

        if self.game.player2:
            self.barra_jugador2 = BarraVida(
                jugador=self.game.player2,
                x=config.ANCHO - 580,
                y=83,
                max_width=400,
                height=40,
                invertida=True
            )

            self.game.player2.health.add_observer(
                self.barra_jugador2
            )

        self.imagen1 = pygame.transform.scale(
            self.game.player1.profile_picture,
            (120, 90)
        )
        self.imagen2 = None

        if self.game.player2:
            self.imagen2 = pygame.transform.scale(
                self.game.player2.profile_picture,
                (120, 90)
            )

        self.item_images = {}
        for item_name in [
            "mate",
            "cafe",
            "laptop",
            "python",
            "router",
            "calculadora"
        ]:
            image = self.game.resource_manager.get_image(
                item_name
            )

            if image:
                self.item_images[item_name] = pygame.transform.scale(
                    image,
                    ( 40, 40)
                )

    def draw(self, screen):
        if self.barra_jugador1:
            self.barra_jugador1.draw(
                screen
            )

        if self.barra_jugador2:
            self.barra_jugador2.draw(
                screen
            )

        screen.blit(
            self.hud_image,
            (20, 20)
        )

        screen.blit(
            self.hud_flip,
            (config.ANCHO - self.hud_width - 20, 20)
        )

        screen.blit(
            self.imagen1,
            (57, 60)
        )

        if self.imagen2:
            screen.blit(
                self.imagen2,
                (
                    config.ANCHO - 170,
                    60
                )
            )

        self.draw_inventory(
            screen,
            self.game.player1,
            170,
            140
        )

        if self.game.player2:
            self.draw_inventory(
                screen,
                self.game.player2,
                config.ANCHO - 320,
                140
            )

        screen.blit(
            self.boton_pausa,
            (config.ANCHO // 2 - 25, 30)
        )

    def draw_inventory(self, screen, player, x, y):
        screen.blit(
            self.inventario_image,
            (x, y)
        )

        if not player.inventory:
            return

        slots = player.inventory.get_items()
        posiciones = [
            x + 10,
            x + 55,
            x + 100
        ]

        for index, item in enumerate(slots):
            if item:
                image = self.item_images.get(
                    item.name
                )

                if image:
                    screen.blit(
                        image,
                        (
                            posiciones[index],
                            y + 10
                        )
                    )

    def update_inventory(self, inventory):
        pass