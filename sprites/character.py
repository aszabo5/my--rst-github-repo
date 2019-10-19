import arcade

FIELD_SIZE = 32

class Character(arcade.Sprite):
    picture = None

    def __init__(self, x, y):
        super().__init__(self.picture)
        self.center_x, self.center_y = self.count_coordinates(x, y)

    def count_coordinates(self, x_field, y_field):
        x_pixels = FIELD_SIZE * x_field + FIELD_SIZE / 2
        y_pixels = FIELD_SIZE * y_field + FIELD_SIZE / 2
        return x_pixels, y_pixels