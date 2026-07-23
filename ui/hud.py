import pygame
import config
from ui.barra_vida import BarraVida

class HUD:

    def __init__(self, game):
        self.game = game

        self.hud_image = pygame.transform.scale(
            self.game.resource_manager.get_image("hud"),
            (570, 170)
        )

        self.hud_flip = pygame.transform.flip(
            self.hud_image,
            True,
            False
        )

        self.inventario_image = pygame.transform.scale(
            self.game.resource_manager.get_image("inventario"),
            (300, 100)
        )

        self.pausa_image = pygame.transform.scale(
            self.game.resource_manager.get_image("pausa"),
            (55, 55)
        )

        self.pause_rect = self.pausa_image.get_rect(
            center=(
                config.ANCHO // 2,
                100
            )
        )

        self.imagen1 = pygame.transform.scale(
            self.game.player1.profile_picture,
            (120, 90)
        )

        self.imagen2 = pygame.transform.scale(
            self.game.player2.profile_picture,
            (120, 90)
        )

        self.barra_jugador1 = BarraVida(
            jugador=self.game.player1,
            x=180,
            y=83,
            max_width=400,
            height=40
        )

        self.barra_jugador2 = BarraVida(
            jugador=self.game.player2,
            x=config.ANCHO - 580,
            y=83,
            max_width=400,
            height=40,
            invertida=True
        )

        self.game.player1.health.add_observer(
            self.barra_jugador1
        )

        self.game.player2.health.add_observer(
            self.barra_jugador2
        )

        self.slot_size = 70

        self.inventario1_pos = (
            40,
            config.ALTO - 120
        )

        self.inventario2_pos = (
            config.ANCHO - 330,
            config.ALTO - 120
        )

    def draw(self, screen):

        screen.blit(
            self.imagen1,
            (57, 60 )
        )

        screen.blit(
            self.imagen2,
            (
                config.ANCHO - 170,
                60
            )
        )

        self.barra_jugador1.draw(
            screen
        )

        self.barra_jugador2.draw(
            screen
        )

        screen.blit(
            self.hud_image,
            ( 20,  20)
        )

        screen.blit(
            self.hud_flip,
            (config.ANCHO - 590, 20)
        )

        screen.blit(
            self.inventario_image,
            self.inventario1_pos
        )

        screen.blit(
            self.inventario_image,
            self.inventario2_pos
        )

        self.draw_inventory_items(
            screen,
            self.game.player1,
            self.inventario1_pos
        )

        self.draw_inventory_items(
            screen,
            self.game.player2,
            self.inventario2_pos
        )

        screen.blit(
            self.pausa_image,
            self.pause_rect
        )
        

    def draw_inventory_items(self, screen, player, position):
        
        if not hasattr(player, "inventory"):
            return

        items = player.inventory.get_items()

        start_x = position[0] + 20
        y = position[1] + 20

        for index, item in enumerate(items):
            if item:
                image = pygame.transform.scale(
                    item.image,
                    (70, 60)
                )
                x = start_x + (
                    index * 95
                )

                screen.blit(
                    image,
                    (x, y)
                )

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.pause_rect.collidepoint(
                event.pos
            ):

                from patterns.state.pauseState import PauseState

                self.game.state_manager.set_state(
                    PauseState(self.game)
                )