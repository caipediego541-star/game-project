import pygame
import config


class Player:

    def __init__(self, game):

        self.game = game
        self.ground = 650
        
        self.x = 400
        self.y = self.ground
        # Hitbox
        self.width = 50
        self.height = 80

        # Tamaño visual del sprite
        self.sprite_width = 350
        self.sprite_height = 350

        # Stats
        self.health = 100
        self.damage = 10
        self.speed = 10

        # Física
        self.velocity_y = 0
        self.gravity = 0.7
        self.jumping = False

        # Acciones
        self.action = "idle"
        self.action_timer = 0

        # Animación
        self.current_animation = "caminar"
        self.current_frame = 0

        self.animation_speeds = {
            "caminar": 0.2,
            "saltar": 0.3
        }

        self.facing_right = True
        self.animations = self.game.resource_manager.load_character("belen")

    def move_left(self):

        self.x -= self.speed

        self.facing_right = False

        if not self.jumping:
            self.change_animation("caminar")

        if self.x < 0:
            self.x = 0



    def move_right(self):

        self.x += self.speed
        self.facing_right = True


        if not self.jumping:
            self.change_animation("caminar")

        if self.x > self.game.ancho - self.width:
            self.x = self.game.ancho - self.width

    def jump(self):

        if not self.jumping:

            self.velocity_y = -18
            self.jumping = True

            self.change_animation("saltar")

    def draw(self, screen):

        frames = self.animations[self.current_animation]

        image = frames[int(self.current_frame)]


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
            (x,y)
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

                self.change_animation("caminar")

        # acciones temporales

        if self.action_timer > 0:
            self.action_timer -= 1
            if self.action_timer == 0:
                self.action = "idle"


    def update_animation(self):

        frames = self.animations[self.current_animation]

        speed = self.animation_speeds.get(
            self.current_animation,
            0.15
        )

        self.current_frame += speed

        # Salto NO hace loop
        if self.current_animation == "saltar":

            if self.current_frame >= len(frames):

                self.current_frame = len(frames)-1

        else:

            if self.current_frame >= len(frames):

                self.current_frame = 0



    def change_animation(self, animation):

        if self.current_animation != animation:

            self.current_animation = animation
            self.current_frame = 0


    def punch(self):

        self.action = "punch"
        self.action_timer = 10


    def kick(self):

        self.action = "kick"
        self.action_timer = 10


    def block(self):

        self.action = "block"
        self.action_timer = 10