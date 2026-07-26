import pygame
import config

from patterns.state.stateBase import State
from combat.combat_controller import CombatController
from patterns.state.victoryState import VictoryState
from ui.question_box import QuestionBox


class FightState(State):

    def __init__(self, game):

        super().__init__(game)

        self.game.fight_state = self
        self.background = (
            self.game.resource_manager.get_image(
                "fight_background1"
            )
        )


        self.question_box = QuestionBox(
            game
        )


        self.combat = CombatController(
            game
        )


        self.combat.start()


        self.cambio_victoria = False

        self.question_box = QuestionBox(game)

    def update(self):

        self.question_box.update()

        if self.question_box.active:
            return

        self.combat.update()

        if (
            self.combat.combate_terminado
            and
            self.combat.tiempo_victoria >= self.combat.esperar_victoria
            and
            not self.cambio_victoria
        ):

            self.cambio_victoria = True


            self.game.state_manager.set_state(
                VictoryState(
                    self.game,
                    self.combat.ganador
                )
            )



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


        self.combat.draw(
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


        # siempre arriba de todo
        self.question_box.draw(
            screen
        )



    def handle_events(self, events):

        for event in events:

            if self.question_box.active:

                self.question_box.handle_event(
                    event
                )

                continue


            if self.game.hud:

                self.game.hud.handle_event(
                    event
                )