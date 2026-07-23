from patterns.factory.button import Button


class ButtonFactory:

    @staticmethod
    def create_button(image, x, y, action=None):
        return Button(
            image=image,
            x=x,
            y=y,
            action=action
        )