from patterns.observer.subject import Subject


class PlayerHealth(Subject):

    def __init__(self, max_health=100):

        super().__init__()

        self.max_health = max_health
        self.health = max_health
        self.dead = False

    def receive_damage(self, damage, blocking=False):

        if self.dead:
            return 0
        change= True
        
        if blocking:
            change= False
            damage *= 0.8

        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.dead = True

        if self.dead:
            self.notify("dead")
        else:
            self.notify("damage")

        return damage, change
    def reset(self):
        self.health = self.max_health
        self.dead = False
        self.notify("damage")