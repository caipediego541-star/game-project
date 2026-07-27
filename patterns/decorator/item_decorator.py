from entities.item import Item

class ItemDecorator(Item):
    def __init__(self, item):
        super().__init__(
            item.name,
            item.image
        )
        self.item = item
    def use(self, player):
        self.item.use(player)