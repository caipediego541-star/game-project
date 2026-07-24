from entities.items.basic_item import BasicItem


class Laptop(BasicItem):

    def use(self, player):

        player.damage = (
            player.base_damage * 1.45
        )

        player.damage_timer = (
            10 * 60
        )

        print(
            f"{player.character} tiene daño aumentado"
        )