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
        self.is_bot = False
        self.mensaje_item = ""
        self.mensaje_item_timer = 0

        self.profile_picture = pygame.image.load(
            profile_picture
        ).convert_alpha()

        self.ground = 650

        self.x = x
        self.y = self.ground

        # Posición inicial para reinicios
        self.spawn_x = x
        self.spawn_facing_right = facing_right

        self.sprite_width = 350
        self.sprite_height = 350

        self.width = self.sprite_width - 20
        self.height = self.sprite_height

        self.inventory = Inventory()

        self.health = PlayerHealth()

        self.damage = 10
        self.base_damage = self.damage

        self.speed = 10
        self.base_speed = self.speed

        self.damage_timer = 0
        self.speed_timer = 0

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

        self.walk_sound_playing = False

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

        self.movement.move_left(self)

        self.facing_right = False

        if not self.movement.jumping:
            self.change_animation(
                "caminar"
            )

        if not self.walk_sound_playing:

            self.game.resource_manager.get_sound(
                f"{self.character}_caminar"
            ).play(-1)

            self.walk_sound_playing = True


    def move_right(self):

        if self.busy or self.is_finished():
            return

        self.movement.move_right(self)

        self.facing_right = True

        if not self.movement.jumping:
            self.change_animation(
                "caminar"
            )

        if not self.walk_sound_playing:

            self.game.resource_manager.get_sound(
                f"{self.character}_caminar"
            ).play(-1)

            self.walk_sound_playing = True


    def jump(self):

        if self.busy or self.is_finished():
            return

        if not self.movement.jumping:

            self.movement.jump()

            self.change_animation(
                "saltar"
            )

        self.game.resource_manager.get_sound(
            f"{self.character}_saltar"
        ).play()


    def draw(self, screen):

        image = self.animation.get_image()

        image = pygame.transform.scale(
            image,
            (
                self.sprite_width,
                self.sprite_height
            )
        )

        if not self.facing_right:

            image = pygame.transform.flip(
                image,
                True,
                False
            )

        x = self.x - self.sprite_width // 2
        y = self.y - self.sprite_height

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


        if self.damage_timer > 0:

            self.damage_timer -= 1

            if self.damage_timer == 0:

                self.damage = self.base_damage


        if self.speed_timer > 0:

            self.speed_timer -= 1

            if self.speed_timer == 0:

                self.speed = self.base_speed
                self.movement.speed = self.base_speed


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
        self.attack_cooldown = 30


        self.change_animation(
            "golpe"
        )


        self.game.resource_manager.get_sound(
            f"{self.character}_golpe"
        ).play()



    def kick(self):

        if self.busy or self.is_finished():
            return

        if self.attack_cooldown > 0:
            return


        self.has_hit = False
        self.busy = True
        self.attack_cooldown = 30


        self.change_animation(
            "patada"
        )


        self.game.resource_manager.get_sound(
            f"{self.character}_patada"
        ).play()



    def block(self):

        if self.busy or self.is_finished():
            return


        self.busy = True
        self.blocking = True


        self.change_animation(
            "cubrirse"
        )


        self.game.resource_manager.get_sound(
            f"{self.character}_cubrirse"
        ).play()



    def stop_block(self):

        self.blocking = False
        self.busy = False



    def stop_move(self):

        sonido = self.game.resource_manager.get_sound(
            f"{self.character}_caminar"
        )

        sonido.stop()

        self.walk_sound_playing = False


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

            self.game.resource_manager.get_sound(
                f"{self.character}_derrota"
            ).play()

        else:
            if change:
                self.change_animation(
                    "recibir_golpe"
                )


                self.game.resource_manager.get_sound(
                    f"{self.character}_recibir_golpe"
                ).play()


        return damage

    def is_finished(self):

        return self.animation.get_current_animation() in [
            "victoria",
            "derrota"
        ]

    def reset(self):

        self.x = self.spawn_x
        self.y = self.ground

        self.facing_right = self.spawn_facing_right
        self.health.reset()

        self.reset_state()



    def reset_state(self):

        self.stop_move()
        self.busy = False
        self.blocking = False
        self.has_hit = False

        self.hitbox.desactivar()

        self.movement.jumping = False
        self.movement.velocity_y = 0

        self.health.reset()

        self.change_animation(
            "idle",
            force=True
        )