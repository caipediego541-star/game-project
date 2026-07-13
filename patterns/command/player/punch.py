from patterns.command.command import Command


class PunchCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.punch()