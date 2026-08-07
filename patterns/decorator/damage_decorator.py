from patterns.decorator.item_decorator import ItemDecorator

class DamageDecorator(ItemDecorator):
    def use(self, player):
        super().use(player)
        player.damage = (
            player.base_damage * 1.45
        )

        player.damage_timer = (
            10 * 60
        )
        mensaje= f"{player.damage} puntos de ataque"
        return mensaje