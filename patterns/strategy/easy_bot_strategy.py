import random
from patterns.strategy.bot_strategy import BotStrategy

class EasyBotStrategy(BotStrategy):

    def __init__(self):
        self.decision_time = 12

    def execute(self, bot):
        distancia = bot.distance_to_enemy()

        if distancia > 250:
            bot.set_action("move")
            return

        acciones = [
            "golpear",
            "patada",
            "defender",
            "saltar",
            "nada"
        ]

        accion = random.choice(acciones)

        if accion == "golpear":
            bot.attack()

        elif accion == "patada":
            bot.kick()

        elif accion == "defender":
            bot.defend()

        elif accion == "saltar":
            bot.jump()