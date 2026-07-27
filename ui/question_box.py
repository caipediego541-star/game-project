import pygame
import config
from patterns.factory.button_factory import ButtonFactory
import random

class QuestionBox:
    def __init__(self, game):

        self.game = game

        self.active = False
        self.bot_timer = 0
        self.bot_delay = 120 

        self.item = None
        self.player_attacker = None
        self.player_target = None

        self.question = ""
        self.options = []
        self.correct_answer = 0

        self.box_width = 700
        self.box_height = 200
        self.button_width = 500
        self.button_height = 65

        self.background = pygame.transform.scale(
            self.game.resource_manager.get_image(
                "question_box"
            ),
            (
                self.box_width,
                self.box_height
            )
        )

        self.button_image = pygame.transform.scale(
            self.game.resource_manager.get_image(
                "question_button"
            ),
            (
                self.button_width,
                self.button_height
            )
        )

        self.button_hover = pygame.transform.scale(
            self.game.resource_manager.get_image(
                "question_button_hover"
            ),
            (
                self.button_width,
                self.button_height
            )
        )

        self.title_font = self.game.resource_manager.get_font(
            "pixel",
            20
        )

        self.font = self.game.resource_manager.get_font(
            "pixel",
            16
        )

        self.buttons = []
        self.time_limit = 5
        self.time_left = 5
        self.timer_counter = 0

        self.timer_font = self.game.resource_manager.get_font(
            "pixel",
            20
        )
        self.box_x = 0
        self.box_y = 0

    def start_question(self, categoria, attacker, target):
        self.bot_timer = 0
        self.active = True
        self.player_attacker = attacker
        self.player_target = target
        self.time_left = self.time_limit
        self.timer_counter = 0
        data = self.game.question_manager.get_question(
            categoria
        )
        self.question = data["pregunta"]
        self.options = data["opciones"]
        self.correct_answer = data["correcta"]
        attacker.busy = True
        target.busy = True
        self.create_buttons()

    def create_buttons(self):

        self.buttons.clear()
        box_x = (
            config.ANCHO - self.background.get_width()
        ) // 2

        box_y = 80

        button_width = self.button_image.get_width()
        button_height = self.button_image.get_height()

        x = box_x + (
            self.background.get_width() - button_width
        ) // 2


        y = box_y + 330


        for index, option in enumerate(self.options):

            button = ButtonFactory.create_button(
                image=self.button_image,
                x=x,
                y=y + index * (button_height + 10),
                action=lambda i=index: self.check_answer(i)
            )


            self.buttons.append(
                {
                    "button": button,
                    "text": option,
                    "index": index
                }
            )

    def handle_event(self,event):
        if not self.active:
            return
        mouse = self.game.get_mouse_position()
        for data in self.buttons:
            data["button"].handle_event(
                event,
                mouse
            )

    def check_answer(self, answer):
        if answer != self.correct_answer:
            damage = int(
                self.player_target.health.max_health
                *
                0.3
            )
            if damage<30:
                damage=25

            self.player_target.receive_damage(
                damage
            )
        self.close()

    def close(self):
        self.active = False
        if self.player_attacker:
            self.player_attacker.busy = False
        if self.player_target:
            self.player_target.busy = False

        self.buttons.clear()

    def draw(self, screen):
        if not self.active:
            return

        self.box_x = (
            config.ANCHO -
            self.box_width
        ) // 2
        self.box_y = 160

        screen.blit(
            self.background,
            (
                self.box_x,
                self.box_y
            ))

        if self.player_target == self.game.player1:
            titulo = "JUGADOR 1 RESPONDE"
        else:
            titulo = "JUGADOR 2 RESPONDE"

        title = self.title_font.render(
            titulo,
            True,
            (255,255,255)
        )
        title_rect = title.get_rect(
            center=(
                config.ANCHO // 2,
                self.box_y + 55
            )
        )
        screen.blit(
            title,
            title_rect)

        self.draw_text_wrapped(
            screen,
            self.question,
            self.font,
            (self.box_x + 100, self.box_y + 75), self.box_width - 70)

        mouse = self.game.get_mouse_position()

        timer = self.timer_font.render(
            f"{self.time_left}S",
            True,
            (255,255,255)
        )

        timer_rect = timer.get_rect(
            center=(
                config.ANCHO // 2,
                300
            )
        )

        screen.blit(
            timer,
            timer_rect
        )

        for data in self.buttons:

            button = data["button"]
            image = button.image

            if button.rect.collidepoint(mouse):
                image = self.button_hover

            screen.blit( image, button.rect)

            text = self.font.render(
                data["text"],
                True,
                (255,255,255))

            text_rect = text.get_rect(
                center=button.rect.center
            )

            screen.blit( text, text_rect )

    def draw_text_wrapped(self, screen, text, font, position, max_width):
        words = text.split(" ")

        lines = []
        current = ""

        for word in words:
            test = current + word + " "
            if font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "

        lines.append(current)
        x, y = position

        for line in lines:

            rendered = font.render(
                line,
                True,
                (255,255,255))


            screen.blit(
                rendered, (x, y))
            y += font.get_height() + 5

    def update(self):

        if not self.active:
            return


        self.timer_counter += 1

        if self.player_target.is_bot:
            self.bot_timer += 1
            if self.bot_timer >= self.bot_delay:
                respuesta = random.randint(
                    0,
                    len(self.options) - 1
                )
                self.check_answer(
                    respuesta
                )
                
        # 60 FPS
        if self.timer_counter >= 60:

            self.timer_counter = 0
            self.time_left -= 1


        if self.time_left <= 0:

            self.time_out()

    def time_out(self):

        damage = int(
            self.player_target.health.max_health * 0.35
        )

        self.player_target.receive_damage(
            damage
        )

        self.close()