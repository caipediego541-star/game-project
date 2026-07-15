import pygame
from combat.hitbox import Hitbox
from combat.hurtbox import Hurtbox


class Player:

    def __init__(self):
        
        self.x = 350
        self.y = 450

        self.width = 50
        self.height = 80
        # Atributos del jugador base
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
        self.velocity_y = 0
        self.gravity = 1
        self.jumping = False
        self.ground = 450
        self.action = "idle"
        self.action_timer = 0

    def move_left(self):
        self.direction="left"
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.direction="right"
        self.x += self.speed
        if self.x > 800 - self.width:
            self.x = 800 - self.width

    def jump(self):
        if not self.jumping:
            self.velocity_y = -18
            self.jumping = True

    def draw(self, screen):
        # Colores
        skin = (255, 220, 177)
        red = (255, 0, 0)
        black = (0, 0, 0)
        # Cabeza
        head_size = 20
        head_x = self.x + 15
        head_y = self.y
        # Cuerpo
        body_x = self.x + 10
        body_y = self.y + 20
        body_width = 30
        body_height = 40
        # Brazos
        left_arm_x = self.x
        right_arm_x = self.x + 40
        arm_y = self.y + 25
        arm_width = 10
        arm_height = 30
        # Piernas
        left_leg_x = self.x + 15
        right_leg_x = self.x + 30
        leg_y = self.y + 60
        leg_width = 8
        leg_height = 25
        # Cabeza
        pygame.draw.rect(screen, skin, (head_x, head_y, head_size, head_size))
        # Cuerpo
        pygame.draw.rect(screen, red, (body_x, body_y, body_width, body_height))
        if self.action == "idle":
            # Brazos
            pygame.draw.rect(screen, black, (left_arm_x, arm_y, arm_width, arm_height))
            pygame.draw.rect(screen, black, (right_arm_x, arm_y, arm_width, arm_height))
            # Piernas
            pygame.draw.rect(screen, black, (left_leg_x, leg_y, leg_width, leg_height))
            pygame.draw.rect(screen, black, (right_leg_x, leg_y, leg_width, leg_height))
        elif self.action == "punch":
            # Brazo izquierdo normal
            pygame.draw.rect(screen, black, (left_arm_x, arm_y, arm_width, arm_height))
            # Brazo derecho extendido
            pygame.draw.rect(screen, black, (body_x + body_width, arm_y + 5, 25, 8))
            # Piernas
            pygame.draw.rect(screen, black, (left_leg_x, leg_y, leg_width, leg_height))
            pygame.draw.rect(screen, black, (right_leg_x, leg_y, leg_width, leg_height))
        elif self.action == "kick":
            # Brazos normales
            pygame.draw.rect(screen, black, (left_arm_x, arm_y, arm_width, arm_height))
            pygame.draw.rect(screen, black, (right_arm_x, arm_y, arm_width, arm_height))
            # Pierna izquierda normal
            pygame.draw.rect(screen, black, (left_leg_x, leg_y, leg_width, leg_height))
            # Pierna derecha extendida
            pygame.draw.rect(screen, black, (right_leg_x, leg_y + 5, 25, 8))
        elif self.action == "block":
            # Brazos delante del cuerpo
            pygame.draw.rect(screen, black, (body_x - 5, arm_y + 5, 40, 8))
            pygame.draw.rect(screen, black, (body_x - 5, arm_y + 15, 40, 8))
            # Piernas
            pygame.draw.rect(screen, black, (left_leg_x, leg_y, leg_width, leg_height))
            pygame.draw.rect(screen, black, (right_leg_x, leg_y, leg_width, leg_height))
        #dibujar hitbox (solo para pruebas, es decir, para que nosotros veamos la simulacion de la hitbox)
        self.hitbox.draw(screen)
        #dibujamos hurtbox para simular, despues lo modificamos o eliminamos, cuando ya tengamos la animaciones
        #fecha que se hizo 15-7-2026, lo comento aca para que sea más rapido de saber cuando se hizo
        self.hurtbox.draw(screen)

    def update(self):

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

    def punch(self):
        self.action = "punch"
        self.action_timer = 10
        if self.direction=="right":
            self.hitbox.activate(self.x + self.width,self.y + 25,25,10)
        else:
            self.hitbox.activate(self.x - 25,self.y + 25,25,10)
    
    def kick(self):
        self.action = "kick"
        self.action_timer = 10
        if self.direction=="right":
            self.hitbox.activate(self.x + self.width,self.y + 60,30,10)
        else:
            self.hitbox.activate(self.x - 30,self.y + 60,30,10)
    
    def block(self):
        self.action = "block"
        self.action_timer = 10
