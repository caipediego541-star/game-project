from entities.items.basic_item import BasicItem

class ItemFactory:

    def __init__(self, resource_manager):
        self.resource_manager = resource_manager


    def create_item(self, item_type):
        image = self.resource_manager.get_image(
            item_type
        )

        return BasicItem(
            item_type,
            image
        )