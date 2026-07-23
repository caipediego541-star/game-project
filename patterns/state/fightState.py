from patterns.state.stateBase import State
import pygame
import config


class FightState(State):
    def __init__(self, game):
        super().__init__(game)
        self.background= self.game.resource_manager.get_image("fight_background1")
        self.combate_terminado = False
        self.tiempo_victoria = 0
        self.esperar_victoria = 120
        self.tiempo_derrota = 0
        self.esperar_derrota = 200 
        self.ganador = None
        self.derrota_iniciada = False


    def handle_events(self, events):
        return super().handle_events(events)
    
    def update(self):
        jugador1 = self.game.player1
        jugador2 = self.game.player2

        if not self.combate_terminado:
            if jugador1.health.dead:
                self.combate_terminado = True
                self.ganador = jugador2
                jugador2.busy = True
                jugador2.blocking = False
                jugador2.hitbox.desactivar()

                jugador1.change_animation("derrota")

            elif jugador2.health.dead:

                self.combate_terminado = True
                self.ganador = jugador1
                jugador1.busy = True
                jugador1.blocking = False
                jugador1.hitbox.desactivar()

                jugador2.change_animation("derrota")


        else:
            self.tiempo_derrota += 1

            if self.tiempo_derrota >= self.esperar_derrota:
                self.ganador.change_animation("victoria")
                self.tiempo_victoria += 1

                if self.tiempo_victoria >= self.esperar_victoria:
                    print("Cambiar a pantalla de victoria")
            return

    def draw(self, screen):

        fondo = pygame.transform.scale(
            self.background,
            (
                config.ANCHO,
                config.ALTO
            )
        )


        screen.blit(
            fondo,
            (0,0)
        )


        self.game.player1.draw(screen)
        self.game.player2.draw(screen)
    
        if self.game.hud:
            self.game.hud.draw()