import pygame


class CombatController:

    def __init__(self, game):

        self.game = game

        self.combate_terminado = False

        self.tiempo_victoria = 0
        self.esperar_victoria = 120

        self.tiempo_derrota = 0
        self.esperar_derrota = 200

        self.ganador = None

        if not hasattr(self.game, "item_manager"):
            self.game.item_manager = self.game.create_item_manager()

    def start(self):

        self.start_music()

        self.reset()

    def start_music(self):

        pygame.mixer.music.load(
            "assets/sounds/pelea.mp3"
        )
        pygame.mixer.music.play(-1)

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

        if self.combate_terminado:

            self.tiempo_derrota += 1

            if self.tiempo_derrota >= self.esperar_derrota:

                if self.ganador:
                    self.ganador.change_animation(
                        "victoria"
                    )

                self.tiempo_victoria += 1

            return

        if jugador1.health.dead:

            self.finalizar_combate(
                jugador2
            )

        elif jugador2.health.dead:

            self.finalizar_combate(
                jugador1
            )

    def finalizar_combate(self, ganador):

        self.combate_terminado = True

        self.ganador = ganador

        ganador.busy = True
        ganador.blocking = False
        ganador.hitbox.desactivar()


        self.game.sound_manager.change_music(
            "assets/sounds/victoria.mp3",
            1000
        )

        ganador.change_animation(
            "victoria"
        )

    def draw(self, screen):

        self.game.item_manager.draw(
            screen
        )

    def reset(self):

        self.combate_terminado = False

        self.tiempo_victoria = 0

        self.tiempo_derrota = 0

        self.ganador = None

        self.game.item_manager.items.clear()

        self.game.item_manager.spawn_timer = 0

    def reset_round(self):
        self.game.player1.reset()
        self.game.player2.reset()
        self.reset()