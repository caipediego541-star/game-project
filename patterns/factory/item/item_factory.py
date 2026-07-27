from entities.item import Item

from patterns.decorator.heal_decorator import HealDecorator
from patterns.decorator.speed_decorator import SpeedDecorator
from patterns.decorator.damage_decorator import DamageDecorator
from patterns.decorator.exam_decorator import ExamDecorator


class ItemFactory:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager

    def create_item(self, item_name):
        image = self.resource_manager.get_image(
            item_name
        )
        if item_name == "mate":
            return HealDecorator(
                Item(
                    item_name,
                    image
                ))

        elif item_name == "cafe":
            return SpeedDecorator(
                Item(
                    item_name,
                    image
                ))

        elif item_name == "laptop":
            return DamageDecorator(
                Item(
                    item_name,
                    image
                ))

        elif item_name == "python":
            return ExamDecorator(
                Item(
                    item_name,
                    image,
                    "programacion"
                ))

        elif item_name == "router":
            return ExamDecorator(
                Item(
                    item_name,
                    image,
                    "redes"
                ))

        elif item_name == "calculadora":
            return ExamDecorator(
                Item(
                    item_name,
                    image,
                    "matematica"
                ))