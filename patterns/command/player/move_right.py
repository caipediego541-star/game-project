from patterns.command.command import Command

class MoveRightCommand(Command):

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.move_right()