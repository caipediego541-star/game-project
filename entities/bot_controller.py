import random


class BotController:

    def __init__(self, bot, enemy, strategy):

        self.bot = bot
        self.enemy = enemy
        self.strategy = strategy

        self.timer = 0
        self.decision_time = strategy.decision_time

        self.blocking = False
        self.block_timer = 0
        self.block_duration = 0

        self.item_timer = 0
        self.item_cooldown = random.randint(
            240,
            420
        )

    def update(self):
        self.item_timer += 1

        if self.item_timer >= self.item_cooldown:
            self.item_timer = 0
            self.item_cooldown = random.randint(240, 420)
            self.use_item()

        if self.blocking:
            self.block_timer += 1

            if self.block_timer >= self.block_duration:
                self.stop_defense()

            return


        distancia = self.distance_to_enemy()


        if distancia > 250:

            self.move_towards_enemy()
            return


        self.timer += 1

        if self.timer >= self.decision_time:

            self.timer = 0

            self.strategy.execute(self)


    def distance_to_enemy(self):

        return abs(
            self.bot.x -
            self.enemy.x
        )


    def move_towards_enemy(self):

        if self.bot.x < self.enemy.x:

            self.bot.move_right()

        else:

            self.bot.move_left()


    def move_away_from_enemy(self):

        if self.bot.x < self.enemy.x:

            self.bot.move_left()

        else:

            self.bot.move_right()


    def attack(self):

        self.bot.punch()


    def kick(self):

        self.bot.kick()


    def jump(self):

        self.bot.jump()
    
    def set_action(self, action):

        if action == "move":
            self.move_towards_enemy()

        elif action == "attack":
            self.attack()

        elif action == "kick":
            self.kick()

        elif action == "defend":
            self.defend()

        elif action == "jump":
            self.jump()

    def defend(self):

        if self.blocking:
            return

        self.blocking = True

        self.block_timer = 0

        self.block_duration = random.randint(
            60,
            120
        )

        self.bot.block()


    def stop_defense(self):

        self.blocking = False

        self.block_timer = 0

        self.bot.stop_block()

    def use_item(self):
        disponibles = []
        for i, item in enumerate(self.bot.inventory.get_items()):
            if item is not None:
                disponibles.append(i)
        if not disponibles:
            return

        indice = random.choice(disponibles)
        self.bot.inventory.use_item(
            indice,
            self.bot
        )  