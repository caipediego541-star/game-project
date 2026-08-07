from patterns.decorator.item_decorator import ItemDecorator

class SpeedDecorator(ItemDecorator):
    def use(self, player):
        super().use(player)
        player.speed = (
            player.base_speed * 1.4
        )
        player.movement.speed = (
            player.speed
        )
        player.speed_timer = (
            15 * 60
        )
        mensaje = f"{player.character} tiene velocidad aumentada"
        return mensaje