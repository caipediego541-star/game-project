import pygame
import config

from patterns.state.stateBase import State


class FightState(State):
    def __init__(self, game):
        super().__init__(game)
        self.background = self.game.resource_manager.get_image(
            "fight_background1"
        )

        self.combate_terminado = False
        self.tiempo_victoria = 0
        self.esperar_victoria = 600
        self.tiempo_derrota = 0
        self.esperar_derrota = 120
        self.ganador = None

        if not hasattr(
            self.game,
            "item_manager"
            ):
            self.game.item_manager = self.game.create_item_manager()

        pygame.mixer.music.load(
            "assets/sounds/pelea.mp3"
        )

        pygame.mixer.music.set_volume(
            0.1
        )

        pygame.mixer.music.play(-1)
    def handle_events(self, events):
        pass

    def update(self):
        jugador1 = self.game.player1
        jugador2 = self.game.player2

        if jugador1:
            jugador1.update()

        if jugador2:
            jugador2.update()

        self.game.combat_manager.check_collision(
            jugador1,
            jugador2
        )

        self.game.item_manager.update()

        if not self.combate_terminado:
            if jugador1.health.dead:
                self.finalizar_combate(
                    jugador2
                )

            elif jugador2.health.dead:
                self.finalizar_combate(
                    jugador1
                )

        else:
            self.tiempo_derrota += 1
            if self.tiempo_derrota >= self.esperar_derrota:

                if self.ganador:
                    self.ganador.change_animation(
                        "victoria"
                    )
                self.tiempo_victoria += 1

                if self.tiempo_victoria >= self.esperar_victoria:
                    print("Cambiar a pantalla de victoria")

    def finalizar_combate(self, ganador):
        self.combate_terminado = True
        self.ganador = ganador

        ganador.busy = True
        ganador.blocking = False
        ganador.hitbox.desactivar()

    def draw(self, screen):

        fondo = pygame.transform.scale(
            self.background,
            (config.ANCHO, config.ALTO)
        )

        screen.blit(
            fondo,
            (0, 0)
        )

        self.game.item_manager.draw(
            screen
        )

        self.game.player1.draw(
            screen
        )

        if self.game.player2:
            self.game.player2.draw(
                screen
            )

        if self.game.hud:
            self.game.hud.draw(
                screen
            )

    def handle_events(self, events):
        if self.game.hud:
            for event in events:
                self.game.hud.handle_event(
                    event
                )