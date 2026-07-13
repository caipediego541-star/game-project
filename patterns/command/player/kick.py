from patterns.command.command import Command

class KickCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.kick()