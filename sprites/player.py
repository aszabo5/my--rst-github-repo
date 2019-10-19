from sprites.character import Character, FIELD_SIZE
import arcade

class Player(Character):
    picture = "img/warrior_1.png"
    health_start = 5

    def __init__(self, x, y, health):
        super().__init__(x, y)
        self.health = health
        self.gold = 0
        self.loot = []

    def player_to_left(self, wall_list):
        self.center_x -= FIELD_SIZE
        if self.wall_collision(wall_list):
            pass
        else:
            self.center_x += FIELD_SIZE

    def player_to_right(self, wall_list):
        self.center_x += FIELD_SIZE
        if self.wall_collision(wall_list):
            pass
        else:
            self.center_x -= FIELD_SIZE

    def player_to_up(self, wall_list):
        self.center_y += FIELD_SIZE
        if self.wall_collision(wall_list):
            pass
        else:
            self.center_y -= FIELD_SIZEy

    def player_to_down(self, wall_list):
        self.center_y -= FIELD_SIZE
        if self.wall_collision(wall_list):
            pass
        else:
            self.center_y += FIELD_SIZE

    def wall_collision(self, walls):
        return bool(arcade.check_for_collision_with_list(self, walls) == [])

