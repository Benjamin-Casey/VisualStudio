# Monsters

class Monster:
    def __init__(self, name, hp, atk, rating, xp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.rating  = rating
        self.xp = xp

    def is_alive(self):
        return self.hp > 0

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name = "Skeleton", hp = 10, atk = 3, rating = 1, xp = 10)