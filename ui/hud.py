import pygame
import config
from entities import player
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

        self.font = self.game.resource_manager.get_font(
            "pixel",
            30
        )

        self.font_item = self.game.resource_manager.get_font(
            "pixel",
            10
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

        self.draw_item_message(
            screen,
            self.game.player1
        )

        self.draw_item_message(
            screen,
            self.game.player2
        )

        screen.blit(
            self.pausa_image,
            self.pause_rect
        )

        combat = self.game.state_manager.current_state.combat

        if not combat.combate_terminado:

            tiempo = combat.tiempo_restante

            texto = self.font.render(
                str(tiempo),
                True,
                (255,255,255)
            )

            texto_rect = texto.get_rect(
                center=(
                    config.ANCHO // 2,
                    30
                )
            )

            self.draw_text_with_outline(
                screen,
                str(tiempo),
                texto_rect,
                (255,255,255)
            )
            self.draw_inventory_commands(
            screen,
            self.inventario1_pos,
            [
                "Z",
                "X",
                "C"
            ]
        )


        self.draw_inventory_commands(
            screen,
            self.inventario2_pos,
            [
                "B",
                "N",
                "M"
            ]
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
            mouse_pos = self.game.get_mouse_position()

            if self.pause_rect.collidepoint(
                mouse_pos
            ):

                from patterns.state.pauseState import PauseState

                self.game.state_manager.set_state(
                    PauseState(self.game)
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

    def draw_inventory_commands(self, screen, position, commands):
        for index, command in enumerate(commands):
            texto = self.font.render(
                command,
                True,
                (255,255,255)
            )

            x = position[0] + 55 + (index * 95)
            y = position[1] - 30

            texto_rect = texto.get_rect(
                center=(
                    x,
                    y
                )
            )

            self.draw_text_with_outline(
                screen,
                command,
                texto_rect,
                (255,255,255)
            )

    def draw_item_message(self, screen, player):

        if player.mensaje_item_timer <= 0:
            return

        player.mensaje_item_timer -= 1

        texto = self.font_item.render(
            player.mensaje_item,
            True,
            (255, 255, 255)
        )

        texto_rect = texto.get_rect(
            center=(
                config.ANCHO // 2,
                config.ALTO // 2
            )
        )

        for x in range(-2, 3):
            for y in range(-2, 3):
                if x != 0 or y != 0:
                    screen.blit(
                        self.font_item.render(
                            player.mensaje_item,
                            True,
                            (0, 0, 0)
                        ),
                        (
                            texto_rect.x + x,
                            texto_rect.y + y
                        )
                    )

        screen.blit(
            texto,
            texto_rect
        )