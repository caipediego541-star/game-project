from entities.items.cafe import Cafe
from entities.items.laptop import Laptop
from entities.items.mate import Mate
from entities.items.examen import Examen

class ItemFactory:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager

    def create_item(self, item_name):

        image = self.resource_manager.get_image(
            item_name
        )

        if item_name == "mate":
            return Mate(item_name, image)

        elif item_name == "cafe":
            return Cafe(item_name, image)

        elif item_name == "laptop":
            return Laptop(item_name, image)

        elif item_name == "python":

            return Examen(
                item_name,
                image,
                "programacion"
            )


        elif item_name == "router":

            return Examen(
                item_name,
                image,
                "redes"
            )


        elif item_name == "calculadora":

            return Examen(
                item_name,
                image,
                "matematica"
            )