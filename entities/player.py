import pygame
from combat.hitbox import Hitbox
from combat.hurtbox import Hurtbox


class Player:

    def __init__(self, game, character, x, facing_right, profile_picture):

        self.character= character
        self.profile_picture= pygame.image.load(
            profile_picture
        ).convert_alpha()
        self.game = game
        self.ground = 650

        # Posición
        self.x = x
        self.y = self.ground

        # Tamaño visual
        self.sprite_width = 350
        self.sprite_height = 350

        self.width = self.sprite_width -20
        self.height = self.sprite_height

        # Stats
        self.health = 100
        self.max_health= 100
        self.damage = 10
        self.speed = 10
        self.dead= False
        self.victory= False
        self.has_hit = False
       
        #hitbox del ataque
        self.hitbox=Hitbox()

        #hurtbox
        # se cambia las medidas del personaje para que el impacto sea mas real y 
        # que no solo al rozar al personaje se genere el impacto (esto si colocamos 
        # las medidas exactas del personaje)
        self.hurtbox = Hurtbox(
            self.x - self.width // 2 + 30,
            self.y - self.height + 10,
            self.width - 120,
            self.height - 30
        )

        # Configuración de las hitboxes de ataque
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
            "golpe": 0.25,
            "patada": 0.3,
            "cubrirse": 0.3,
            "recibir_golpe": 0.18,
            "derrota": 0.18,
            "victoria": 0.15
        }

        self.facing_right = facing_right
        self.animations = self.game.resource_manager.load_character(character)

    def move_left(self):
        if self.busy or self.is_finished():
            return

        self.x -= self.speed

        if self.x < 0:
            self.x = 0

        self.facing_right = False

        if not self.jumping:
            self.change_animation("caminar")

    def move_right(self):
        if self.busy or self.is_finished():
            return

        self.x += self.speed
        if self.x > self.game.ancho - self.width:
            self.x = self.game.ancho - self.width

        self.facing_right = True

        if not self.jumping:
            self.change_animation("caminar")

    def jump(self):

        if self.busy or self.is_finished():
            return

        if not self.jumping:
            self.velocity_y = -18
            self.jumping = True

            self.change_animation("saltar")

    def draw(self, screen):

        frames = self.animations[self.current_animation]
        image = frames[int(self.current_frame)]

        if self.current_animation == "derrota":
            scale_w= 1.6
            scale_h= 1.2
        else:
            scale_w = 1.0
            scale_h = 1.0

        width = int(self.sprite_width * scale_w)
        height = int(self.sprite_height * scale_h)

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

        if self.current_animation== "derrota":
            y = self.y - height + 15 

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

        self.hurtbox.update(
            self.x - self.width // 2 + 40,
            self.y - self.height + 10,
            self.width - 130 ,
            self.height -20
        )


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
        
        if self.current_animation in ["victoria", "derrota"]:
            if self.current_frame >= len(frames):
                self.current_frame = len(frames) - 1


            return

        if self.current_animation in (
            "golpe",
            "patada",
            "recibir_golpe"
        ):

            frame_actual = int(self.current_frame)

            if self.current_animation != "recibir_golpe":
                datos = self.attack_hitboxes[self.current_animation]
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

            if self.current_frame >= len(frames):

                self.hitbox.desactivar()
                self.busy = False

                if self.jumping:
                    self.change_animation("saltar")
                else:
                    self.change_animation("idle")

            return
        if self.current_frame >= len(frames):

            self.current_frame = 0

    def change_animation(self, animation):
        if self.current_animation in ["victoria", "derrota"]:
                return

        if self.current_animation != animation:

            self.current_animation = animation
            self.current_frame = 0


    def punch(self):
        if self.busy or self.is_finished():
            return
        
        self.has_hit = False

        self.busy = True
        self.change_animation("golpe")


    def kick(self):
        if self.busy or self.is_finished():
           return
        
        self.has_hit = False
        
        self.busy = True
        self.change_animation("patada")
   


    def block(self):
        if self.busy or self.is_finished():
           return

        self.busy = True
        self.blocking = True
        self.change_animation("cubrirse")

    def stop_block(self):
        self.blocking = False

    def stop_move(self):
        if not self.busy and not self.jumping:
            self.change_animation("idle")

    def receive_damage(self, damage):
        if self.dead:
            return

        if self.blocking:
            damage *= 0.5
            self.health -= damage
            return damage

        self.health -= damage
        self.change_animation("recibir_golpe")

        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.busy = True
            self.blocking = False

            self.change_animation("derrota")

        return damage

    def is_finished(self):

        return self.current_animation in [
            "victoria",
            "derrota"
        ]