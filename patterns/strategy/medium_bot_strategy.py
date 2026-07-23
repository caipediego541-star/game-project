import random
from patterns.strategy.bot_strategy import BotStrategy

class MediumBotStrategy(BotStrategy):
    def __init__(self):
        self.decision_time = 5

    def execute(self, bot):
        distancia = bot.distance_to_enemy()

        if distancia > 220:
            bot.set_action("move")
            return

        acciones = [
            "golpe",
            "golpe",
            "golpe",
            "patada",
            "patada",
            "defender",
            "alejarse",
            "saltar"
        ]

        accion = random.choice(acciones)

        if accion == "golpe":
            bot.attack()

        elif accion == "patada":
            bot.kick()

        elif accion == "defender":
            bot.defend()

        elif accion == "alejarse":
            bot.move_away_from_enemy()

        elif accion == "saltar":
            bot.jump()