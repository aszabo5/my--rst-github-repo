from sprites.character import Character

class Chest(Character):
    picture = "img/lada.png"

    def __init__(self, x, y, objects, open_status):
        super().__init__(x, y)
        self.objects = objects
        self.open_status = open_status
        self.chest_message_player_1 = 0
        self.chest_message_player_2 = 0

    def loot_to_player(self):
        return self.objects