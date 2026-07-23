class CombatManager:

    def __init__(self):
        pass

    def check_collision(self, player1, player2):

        if player1.hitbox.colisiones(player2.hurtbox):
            if not player1.has_hit:
                damage= player2.receive_damage(player1.damage)
                player1.has_hit = True

                print(
                    "Jugador 2 recibió",
                    damage,
                    "de daño"
                )

        if player2.hitbox.colisiones(player1.hurtbox):
            if not player2.has_hit:
                damage= player1.receive_damage(player2.damage)
                player2.has_hit = True

                print(
                    "Jugador 1 recibió",
                    damage,
                    "de daño"
                )