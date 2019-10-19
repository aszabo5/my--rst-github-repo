from sprites.character import Character

class Coin(Character):
    counter = 0
    picture = "img/Coin1.png"

    def __init__(self, x, y, gold_value):
        super().__init__(x, y)
        self.gold_value = gold_value
        Coin.counter += 1