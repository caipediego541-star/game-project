from patterns.command.command import Command

class StopBlockCommand(Command):

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.stop_block()