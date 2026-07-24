from entities.items.basic_item import BasicItem


class Cafe(BasicItem):

    def use(self, player):

        player.speed = player.base_speed * 1.4
        player.movement.speed = player.speed

        player.speed_timer = (
            15 * 60
        )

        print(
            f"{player.character} tiene velocidad aumentada"
        )