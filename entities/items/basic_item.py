from entities.items.item import Item


class BasicItem(Item):

    def __init__(self, name, image):

        super().__init__(
            name,
            image
        )


    def use(self, player):

        pass