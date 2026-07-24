from entities.items.basic_item import BasicItem


class Examen(BasicItem):

    def __init__(self, name, image, materia):

        super().__init__(
            name,
            image
        )

        self.materia = materia


    def use(self, player):

        print(
            f"{player.character} respondió un examen de {self.materia}"
        )