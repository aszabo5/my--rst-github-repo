from sprites.character import Character

class Enemy(Character):
    picture = "img/demon.png"

    def __init__(self, x, y, vitality, damage):
        super().__init__(x, y)
        self.vitality = vitality
        self.damage = damage