import pygame

class Item:

    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.velocity_y = 0
        self.on_ground = False

    def use(self, player):

        print(f"{player.character} usó {self.name}")