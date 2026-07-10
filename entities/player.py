import pygame

class Player:

    def __init__(self):

        self.x = 350
        self.y = 450

        self.width = 50
        self.height = 80

        self.speed = 10

        self.velocity_y = 0
        self.gravity = 1
        self.jumping = False
        self.ground = 450

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > 800 - self.width:
            self.x = 800 - self.width

    def jump(self):
        if not self.jumping:
            self.velocity_y = -18
            self.jumping = True

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255,0,0),
            (self.x,self.y,self.width,self.height)
        )

    def update(self):

        if self.jumping:

            self.velocity_y += self.gravity
            self.y += self.velocity_y

            if self.y >= self.ground:
                self.y = self.ground
                self.velocity_y = 0
                self.jumping = False