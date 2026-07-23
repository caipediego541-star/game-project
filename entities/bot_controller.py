import random

class BotController:

    def __init__(self, bot, enemy, strategy):

        self.bot = bot
        self.enemy = enemy
        self.strategy = strategy

        self.timer = 0
        self.decision_time = strategy.decision_time

        self.current_action = None

        self.blocking = False
        self.block_timer = 0
        self.block_duration = 0


    def update(self):
        if self.blocking:
            self.block_timer += 1
            if self.block_timer >= self.block_duration:
                self.stop_defense()
            return

        self.execute_current_action()
        self.timer += 1

        if self.timer >= self.decision_time:
            self.timer = 0
            self.strategy.execute(self)

    def execute_current_action(self):
        if self.current_action == "move":
            self.move_towards_enemy()

    def set_action(self, action):
        self.current_action = action

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
        self.current_action = 70
        self.bot.punch()

    def kick(self):
        self.current_action = 95
        self.bot.kick()

    def jump(self):
        self.current_action = None
        self.bot.jump()

    def defend(self):
        self.current_action = None

        if self.blocking:
            return

        self.blocking = True
        self.block_timer = 0
        self.block_duration = random.randint(
            70,
            100
        )
        self.bot.block()

    def stop_defense(self):
        self.blocking = False
        self.block_timer = 0
        self.bot.stop_block()