import random
import pygame

class ItemManager:
    def __init__(self, game, factory):

        self.game = game
        self.factory = factory
        self.items = []
        self.spawn_timer = 0
        self.spawn_time = 800
        self.gravity = 0.35
        self.ground = 650


    def update(self):
        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_time:
            self.spawn_timer = 0
            self.spawn_item()

        for item in self.items:
            if not item.on_ground:
                item.velocity_y += self.gravity
                item.rect.y += item.velocity_y

                if item.rect.bottom >= self.ground - 35:
                    item.rect.bottom = self.ground - 35
                    item.velocity_y = 0
                    item.on_ground = True
        self.check_pickups()

    def spawn_item(self):
        available_items = [

            "mate",
            "cafe",
            "laptop",
            "python",
            "router",
            "calculadora",
            "mate",
            "mate",
            "cafe",
            "cafe",
            "laptop",
            "laptop",
            "mate",
            "mate",
            "cafe"

        ]

        item_type = random.choice(
            available_items
        )

        item = self.factory.create_item(
            item_type
        )

        item.image = pygame.transform.scale(
            item.image,
            (
                70,
                70
            )
        )

        item.rect = item.image.get_rect()

        item.rect.centerx = random.randint(
            150,
            1130
        )

        item.rect.y = -70

        item.velocity_y = 0

        item.on_ground = False

        self.items.append(
            item
        )

    def check_pickups(self):
        players = [

            self.game.player1,

            self.game.player2
        ]

        for item in self.items[:]:
            for player in players:
                if player:
                    if player.hurtbox.rect.colliderect(
                        item.rect
                    ):

                        if player.inventory.add_item(
                            item
                        ):
                            self.game.resource_manager.get_sound(
                                        "recoger_item"
                                    ).play()
                            
                            self.items.remove(
                                item
                            )
                        break


    def draw(self, screen):
        for item in self.items:
            screen.blit(
                item.image,
                item.rect
            )