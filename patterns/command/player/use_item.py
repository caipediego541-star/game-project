class UseItemCommand:

    def __init__(self, player, slot):
        self.player = player
        self.slot = slot

    def execute(self):
        mensaje= self.player.inventory.use_item(
            self.slot,
            self.player
        )
        
        self.player.mensaje_item = mensaje
        self.player.mensaje_item_timer = 120
