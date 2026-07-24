class UseItemCommand:

    def __init__(self, player, slot):
        self.player = player
        self.slot = slot

    def execute(self):
        self.player.inventory.use_item(
            self.slot,
            self.player
        )
