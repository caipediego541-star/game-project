from patterns.decorator.item_decorator import ItemDecorator

class HealDecorator(ItemDecorator):
    def use(self, player):
        super().use(player)
        curacion = int(
            player.health.health * 0.60
        )
        player.health.heal(
            curacion
        )

        print(
            f"{player.character} recuperó {curacion} de vida"
        )