import pygame

from combat.hitbox import Hitbox
from combat.hurtbox import Hurtbox
from entities.player_health import PlayerHealth
from entities.inventory import Inventory
from entities.components.animation_controller import AnimationController
from entities.components.movement_controller import MovementController


class Player:

    def __init__(self, game, character, x, facing_right, profile_picture):
        self.character = character
        self.game = game

        self.profile_picture = pygame.image.load(
            profile_picture
        ).convert_alpha()

        self.ground = 650

        self.x = x
        self.y = self.ground
        self.sprite_width = 350
        self.sprite_height = 350

        self.width = self.sprite_width - 20
        self.height = self.sprite_height

        self.health = PlayerHealth()
        self.inventory = Inventory()

        self.damage = 10
        self.speed = 10

        self.victory = False
        self.has_hit = False
        self.attack_cooldown = 0

        self.hitbox = Hitbox()

        self.attack_hitboxes = {

            "golpe": {
                "width": 90,
                "height": 70,
                "offset_x": 70,
                "offset_y": -280,
                "start_frame": 3,
                "end_frame": 5
            },

            "patada": {
                "width": 120,
                "height": 90,
                "offset_x": 45,
                "offset_y": -160,
                "start_frame": 5,
                "end_frame": 7
            }
        }

        self.hurtbox = Hurtbox(
            self.x - self.width // 2 + 30,
            self.y - self.height + 10,
            self.width - 120,
            self.height - 30
        )

        self.movement = MovementController(
            speed=self.speed,
            gravity=0.7,
            ground=self.ground
        )

        self.busy = False
        self.blocking = False

        self.facing_right = facing_right
        animations = self.game.resource_manager.load_character(
            character
        )
        self.animation = AnimationController(
            animations
        )

    def move_left(self):
        if self.busy or self.is_finished():
            return

        self.movement.move_left(
            self
        )

        self.facing_right = False
        if not self.movement.jumping:
            self.change_animation(
                "caminar"
            )

    def move_right(self):
        if self.busy or self.is_finished():
            return
        self.movement.move_right(
            self
        )
        self.facing_right = True
        if not self.movement.jumping:
            self.change_animation(
                "caminar"
            )

    def jump(self):
        if self.busy or self.is_finished():
            return

        if not self.movement.jumping:
            self.movement.jump()
            self.change_animation(
                "saltar"
            )

    def draw(self, screen):
        image = self.animation.get_image()
        width = self.sprite_width
        height = self.sprite_height

        image = pygame.transform.scale(
            image,
            (
                width,
                height
            )
        )

        if not self.facing_right:
            image = pygame.transform.flip(
                image,
                True,
                False
            )

        x = self.x - width // 2
        y = self.y - height

        screen.blit(
            image,
            (
                x,
                y
            )
        )

    def update(self):
        termino = self.animation.update(
            self.blocking
        )

        if termino:
            self.animation_finished()

        self.movement.update(
            self
        )

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        self.hurtbox.update(
            self.x - self.width // 2 + 40,
            self.y - self.height + 10,
            self.width - 130,
            self.height - 20
        )

        self.update_attack_hitbox()

    def update_attack_hitbox(self):
        animation = self.animation.get_current_animation()

        if animation not in [
            "golpe",
            "patada"
        ]:
            self.hitbox.desactivar()
            return

        frame_actual = int(
            self.animation.current_frame
        )

        datos = self.attack_hitboxes[
            animation
        ]

        if datos["start_frame"] <= frame_actual <= datos["end_frame"]:
            ancho = datos["width"]
            alto = datos["height"]
            offset_x = datos["offset_x"]
            offset_y = datos["offset_y"]


            if self.facing_right:
                hitbox_x = self.x + offset_x

            else:
                hitbox_x = self.x - offset_x - ancho

            hitbox_y = self.y + offset_y

            self.hitbox.activar(
                hitbox_x,
                hitbox_y,
                ancho,
                alto
            )

        else:
            self.hitbox.desactivar()



    def animation_finished(self):
        current = self.animation.get_current_animation()

        if current in [
            "golpe",
            "patada",
            "recibir_golpe"
        ]:

            self.hitbox.desactivar()
            self.busy = False

            if self.movement.jumping:
                self.change_animation(
                    "saltar"
                )

            else:
                self.change_animation(
                    "idle"
                )


        elif current == "cubrirse":
            self.busy = False
            self.change_animation(
                "idle"
            )
        elif current == "saltar":
            if self.movement.jumping:
                return
            self.change_animation(
                "idle"
            )

    def change_animation(self, animation, force=False):
        self.animation.change_animation(
            animation,
            force
        )



    def punch(self):
        if self.busy or self.is_finished():
            return

        if self.attack_cooldown > 0:
            return

        self.has_hit = False
        self.busy = True
        self.attack_cooldown = 60
        self.change_animation(
            "golpe"
        )

    def kick(self):
        if self.busy or self.is_finished():
            return

        if self.attack_cooldown > 0:
            return

        self.has_hit = False
        self.busy = True
        self.attack_cooldown = 60
        self.change_animation(
            "patada"
        )

    def block(self):
        if self.busy or self.is_finished():
            return
        self.busy = True
        self.blocking = True
        self.change_animation(
            "cubrirse"
        )

    def stop_block(self):
        self.blocking = False
        self.busy = False

    def stop_move(self):
        if not self.busy and not self.movement.jumping:
            self.change_animation(
                "idle"
            )



    def receive_damage(self, damage):
        damage, change = self.health.receive_damage(
            damage,
            self.blocking
        )

        if damage == 0:
            return 0

        if self.health.dead:
            self.busy = True
            self.blocking = False
            self.change_animation(
                "derrota"
            )

        else:
            if change:
                self.change_animation(
                    "recibir_golpe"
                )

        return damage

    def is_finished(self):
        return self.animation.get_current_animation() in [
            "victoria",
            "derrota"
        ]
    
    def reset(self, x, facing_right):

        self.x = x
        self.y = self.ground

        self.facing_right = facing_right

        self.busy = False
        self.blocking = False
        self.has_hit = False

        self.hitbox.desactivar()

        self.movement.jumping = False
        self.movement.velocity_y = 0

        self.change_animation("idle", force=True)

        self.health.reset()

    def reset_state(self):

        self.busy = False
        self.blocking = False
        self.has_hit = False
        self.hitbox.desactivar()
        self.movement.jumping = False
        self.movement.velocity_y = 0
        self.change_animation("idle")
        self.health.reset()