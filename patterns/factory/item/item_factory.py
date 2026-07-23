from entities.items.item import Item

class ItemFactory:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager

    def create_item(self, item_name):

        image = self.resource_manager.get_image(
            item_name
        )

        return Item(
            item_name,
            image
        )