import random
import pygame

class ItemManager:

    def __init__(self, game, factory):
        self.game = game
        self.factory = factory
        self.items = []
        self.spawn_timer = 0
        self.spawn_time = 600


    def update(self):
        self.spawn_timer += 1

        if self.spawn_timer >= self.spawn_time:
            self.spawn_timer = 0
            self.spawn_item()

        self.check_pickups()


    def spawn_item(self):
        available_items = [
            "mate",
            "cafe",
            "laptop",
            "python",
            "router",
            "calculadora"
        ]

        item_type = random.choice(
            available_items
        )

        item = self.factory.create_item(
            item_type
        )

        item.image = pygame.transform.scale(
            item.image,
            (50,50)
        )

        item.rect = item.image.get_rect(
            center=(
                random.randint(
                    150,
                    1050
                ),
                550
            )
        )
        self.items.append(item)


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