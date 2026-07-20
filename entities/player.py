import pygame
from combat.hitbox import Hitbox
from combat.hurtbox import Hurtbox


class Player:

    def __init__(self, game, character, x, facing_right):

        self.character= character
        self.game = game
        self.ground = 650

        # Posición
        self.x = x
        self.y = self.ground

        # Hitbox
        self.width = 50
        self.height = 80

        # Tamaño visual
        self.sprite_width = 350
        self.sprite_height = 350

        # Stats
        self.health = 100
        self.damage = 10
        self.speed = 10
        #direccion del personaje
        self.direction="right"
        #hitbox del ataque
        self.hitbox=Hitbox()
        #hurtbox
        #se cambia las medidas del personaje para que el impacto sea mas real y que no solo al rozar al personaje se genere el impacto (esto si colocamos las medidas exactas del personaje)
        self.hurtbox=Hurtbox(self.x + 5,self.y + 5,self.width - 10 ,self.height - 10) 
        # -----------------

        # Física
        self.velocity_y = 0
        self.gravity = 0.7
        self.jumping = False

        # Estado de acción
        self.busy = False

        # Animación
        self.current_animation = "idle"
        self.current_frame = 0
        self.blocking = False

        self.animation_speeds = {
            "idle": 0.13,
            "caminar": 0.2,
            "saltar": 0.35,
            "golpe": 0.2,
            "patada": 0.3,
            "cubrirse": 0.3
        }

        self.facing_right = facing_right

        self.animations = self.game.resource_manager.load_character(character)

    def move_left(self):
        self.direction="left"

        if self.busy:
            return

        self.x -= self.speed

        if self.x < 0:
            self.x = 0

        self.facing_right = False

        if not self.jumping:
            self.change_animation("caminar")

    def move_right(self):
        self.direction="right"

        if self.busy:
            return

        self.x += self.speed

        if self.x > self.game.ancho - self.width:
            self.x = self.game.ancho - self.width

        self.facing_right = True

        if not self.jumping:
            self.change_animation("caminar")

    def jump(self):

        if self.busy:
            return

        if not self.jumping:

            self.velocity_y = -18
            self.jumping = True

            self.change_animation("saltar")

    def draw(self, screen):

        frames = self.animations[self.current_animation]
        image = frames[int(self.current_frame)]

        if self.current_animation == "patada":
            scale = 1.1
        else:
            scale = 1.0

        width = int(self.sprite_width * scale)
        height = int(self.sprite_height * scale)

        image = pygame.transform.scale(
            image,
            (width, height)
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
            (x, y)
        )
        
    def update(self):

        self.update_animation()

        # Física del salto
        if self.jumping:

            self.velocity_y += self.gravity
            self.y += self.velocity_y

            if self.y >= self.ground:

                self.y = self.ground
                self.velocity_y = 0
                self.jumping = False

        if self.action_timer > 0:
            self.action_timer -= 1
            if self.action_timer == 0:
                self.action = "idle"
                self.hitbox.desactivate()

        self.hurtbox.update(self.x + 5,self.y + 5,self.width - 10,self.height - 10)

        if not self.busy:
                    self.change_animation("idle")


    def update_animation(self):

        frames = self.animations[self.current_animation]

        speed = self.animation_speeds.get(
            self.current_animation,
            0.15
        )

        self.current_frame += speed

        if self.current_animation == "saltar":

            if self.current_frame >= len(frames):

                self.current_frame = len(frames) - 1

            return
        
        if self.current_animation == "cubrirse":

            if self.current_frame >= len(frames):

                if self.blocking:
                    self.current_frame = len(frames) - 1
                else:
                    self.busy = False
                    self.change_animation("idle")

            return

        if self.current_animation in (
                "golpe",
                "patada"
            ):

            if self.current_frame >= len(frames):

                self.busy = False

                if self.jumping:
                    self.change_animation("saltar")
                else:
                    self.change_animation("idle")

            return 

        if self.current_frame >= len(frames):

            self.current_frame = 0

    def change_animation(self, animation):

        if self.current_animation != animation:

            self.current_animation = animation
            self.current_frame = 0


    def punch(self):

        if self.busy:
          return
        
        if self.direction=="right":
            self.hitbox.activate(self.x + self.width,self.y + 25,25,10)
        else:
            self.hitbox.activate(self.x - 25,self.y + 25,25,10)

        self.busy = True
        self.change_animation("golpe")


    def kick(self):

        if self.busy:
           return
        
        if self.direction=="right":
            self.hitbox.activate(self.x + self.width,self.y + 25,25,10)
        else:
            self.hitbox.activate(self.x - 25,self.y + 25,25,10)

        self.busy = True
        self.change_animation("patada")

    def block(self):

        if self.busy:
           return

        self.busy = True
        self.blocking = True
        self.change_animation("cubrirse")

    def stop_block(self):
        self.blocking = False

    def stop_move(self):
        if not self.busy and not self.jumping:
            self.change_animation("idle")