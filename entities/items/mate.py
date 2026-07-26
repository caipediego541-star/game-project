from entities.items.basic_item import BasicItem


class Mate(BasicItem):
    def use(self, player):
        curacion = int(
            player.health.health * 0.60
        )

        player.health.heal(
            curacion
        )

        print(
            f"{player.character} recuperó {curacion} de vida"
        )