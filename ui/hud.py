import pygame
import config

from ui.barra_vida import BarraVida


class HUD:

    def __init__(self, game):

        self.game = game

        self.hud_image = (
            self.game.resource_manager.get_image("hud")
        )

        self.hud_width = 570
        self.hud_height = 170

        self.hud_image = pygame.transform.scale(
            self.hud_image,
            (
                self.hud_width,
                self.hud_height
            )
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

        self.nombre_jugador1= self.game.player1.character

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
        
        self.nombre_jugador2= self.game.player2.character


    def draw(self):

        self.barra_jugador1.draw(
            self.game.game_screen
        )

        self.barra_jugador2.draw(
            self.game.game_screen
        )

        imagen1 = pygame.transform.scale(
            self.barra_jugador1.jugador.profile_picture,
            (120,90)
        )

        imagen2 = pygame.transform.scale(
            self.barra_jugador2.jugador.profile_picture,
            (120,90)
        )

        self.game.game_screen.blit(
            imagen1,
            (57,60)
        )

        self.game.game_screen.blit(
            imagen2,
            (config.ANCHO - 170,60)
        )

        # HUD izquierda
        self.game.game_screen.blit(
            self.hud_image,
            (20, 20)
        )

        # HUD derecha
        hud_flip = pygame.transform.flip(
            self.hud_image,
            True,
            False
        )

        self.game.game_screen.blit(
            hud_flip,
            (
                config.ANCHO - self.hud_width - 20,
                20
            )
        )

        