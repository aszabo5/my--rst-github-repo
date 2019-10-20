import arcade
from sprites.coin import Coin
from sprites.monster import Enemy
from random import randint
from sprites.chest import Chest
from sprites.player import Player
from sprites.character import FIELD_SIZE
from sprites.wall import Wall

BG_WIDTH = 640
BG_HEIGHT = 360

LEFT_CORRIDOR = 48 # Eddig mehet a játékos (képének középpontja) balra
RIGHT_CORRIDOR = 592 # Eddig mehet a játékos (képének középpontja) jobbra
UPPER_CORRIDOR = 128 # Eddig mehet a játékos (képének középpontja) felfele
BOTTOM_CORRIDOR = 48 # Eddig mehet a játékos (képének középpontja) lefele

#Main game

class WarriorGame(arcade.Window):

    def __init__(self):
        super().__init__(BG_WIDTH, BG_HEIGHT, "WarriorGame")

        self.step_count = 0
        self.playlist = None
        self.gold_text_list = None
        self.health_list = None
        self.coin_list = None
        self.health_symbol_list = None
        self.damage_suffered = None
        self.health = 1
        self.health_2 = 1
        self.wall_list = None

    def on_draw(self):
        arcade.start_render()
        self.show_bg()
        self.gold_text_list.draw()
        self.show_gold_text()
        self.show_health_text()
        self.health_list.draw()
        self.coin_list.draw()
        self.enemy_list.draw()
        self.chest_list.draw()
        self.playlist.draw()
        self.health_symbol_list.draw()
        self.wall_list.draw()

    def start(self):
        self.graphics_init()
        self.health = 0
        for i in range(Player.health_start):
            self.new_life()
        self.gold = 12

        self.health2 = 0
        for i in range(Player.health_start):
            self.health2 += 1
        self.gold2 = 10
        arcade.run()

    def graphics_init(self):
        self.bg_position_x, self.bg_position_y = BG_WIDTH / 2, BG_HEIGHT / 2
        self.bg_picture = arcade.load_texture("img/forest_background.png")

        self.players_sprite_init()
        self.enemy_list_init()
        self.gold_text_sprite_init()
        self.health_sprite_init()
        self.gold_text_list_init()
        self.health_list_init()
        self.coin_list_init()
        self.chest_list_init()
        self.wall_list_init()

    def wall_list_init(self):
        self.wall_list = arcade.SpriteList()
        for w in range(0, 2):
            self.wall_list.append(Wall(8, w))

    def players_sprite_init(self):
        self.playlist = arcade.SpriteList()

        self.player1 = Player(3, 4, self.health)
        self.playlist.append(self.player1)

        self.player2 = Player(5, 3, self.health)
        self.playlist.append(self.player2)

    def enemy_list_init(self):
        self.enemy_list = arcade.SpriteList()
        self.enemy_list.append(Enemy(10, 3, 4, 2))
        self.enemy_list.append(Enemy(14, 2, 3, 1))

    def gold_text_sprite_init(self):
        self.gold_text_sprite = arcade.Sprite("img/Coin1.png")
        self.gold_text_sprite.center_x = FIELD_SIZE / 2
        self.gold_text_sprite.center_y = BG_HEIGHT - 1.5 * FIELD_SIZE

        # Second player gold_sprite:
        self.gold_text_sprite2 = arcade.Sprite("img/Coin1.png")
        self.gold_text_sprite2.center_x = BG_WIDTH - (FIELD_SIZE / 2)
        self.gold_text_sprite2.center_y = BG_HEIGHT - 1.5 * FIELD_SIZE

    def health_sprite_init(self):
        self.health_sprite = arcade.Sprite("img/Heart.png")
        self.health_sprite.center_x = FIELD_SIZE / 2
        self.health_sprite.center_y = BG_HEIGHT - 2.5 * FIELD_SIZE

        # Second player health_sprite:
        self.health_sprite2 = arcade.Sprite("img/Heart.png")
        self.health_sprite2.center_x = BG_WIDTH - (FIELD_SIZE / 2)
        self.health_sprite2.center_y = BG_HEIGHT - 2.5 * FIELD_SIZE

    def gold_text_list_init(self):
        self.gold_text_list = arcade.SpriteList()
        self.gold_text_list.append(self.gold_text_sprite)
        self.gold_text_list.append(self.gold_text_sprite2)

    def health_list_init(self):
        self.health_list = arcade.SpriteList()
        self.health_list.append(self.health_sprite)
        self.health_list.append(self.health_sprite2)

        self.health_symbol_list = arcade.SpriteList()

    def coin_list_init(self):
        self.coin_list = arcade.SpriteList()
        self.coin_list.append(Coin(8, 2, 6))
        self.coin_list.append(Coin(15, 2, 4))
        self.coin_list.append(Coin(17, 3, 3))

    def show_bg(self):
        arcade.draw_texture_rectangle(
            self.bg_position_x,
            self.bg_position_y,
            self.bg_picture.width,
            self.bg_picture.height,
            self.bg_picture)

    def chest_list_init(self):
        self.chest_list = arcade.SpriteList()
        self.chest_list.append(Chest(10, 4, ["sword", "shield"], True))
        self.chest_list.append(Chest(19, 2, ["axe"], False))
        self.chest_list.append(Chest(15, 3, ["arrow"], True))
        self.chest_list.append(Chest(17, 1, [], True))

    def show_gold_text(self):
        arcade.draw_text(str(self.gold), FIELD_SIZE, BG_HEIGHT - 2 * FIELD_SIZE, arcade.color.WHITE, 30)

        #Second player's gold_text:
        arcade.draw_text(str(self.gold2), BG_WIDTH - FIELD_SIZE * 2.5, BG_HEIGHT - 2 * FIELD_SIZE, arcade.color.WHITE, 30)

    def show_health_text(self):
        arcade.draw_text(str(self.health), FIELD_SIZE, BG_HEIGHT - 3 * FIELD_SIZE, arcade.color.YELLOW, 30)

        # Second player's health_text:
        arcade.draw_text(str(self.health2), BG_WIDTH - FIELD_SIZE * 2.5, BG_HEIGHT - 3 * FIELD_SIZE, arcade.color.YELLOW, 30)

    def move_player_1(self, button):
        if button == arcade.key.LEFT:
            if self.player1.center_x > LEFT_CORRIDOR:
                self.player1.player_to_left(self.wall_list)

        elif button == arcade.key.RIGHT:
            if button == arcade.key.RIGHT:
                if self.player1.center_x < RIGHT_CORRIDOR:
                    self.player1.player_to_right(self.wall_list)

        elif button == arcade.key.UP:
            if self.player1.center_y < UPPER_CORRIDOR:
                self.player1.player_to_up(self.wall_list)

        elif button == arcade.key.DOWN:
            if self.player1.center_y > BOTTOM_CORRIDOR:
                self.player1.player_to_down(self.wall_list)

#Second player's movement:

    def move_player_2(self, button):
        if button == arcade.key.A:
            if self.player2.center_x > LEFT_CORRIDOR:
                self.player2.player_to_left(self.wall_list)

        elif button == arcade.key.D:
            if button == arcade.key.D:
                if self.player2.center_x < RIGHT_CORRIDOR:
                    self.player2.player_to_right(self.wall_list)

        elif button == arcade.key.W:
            if self.player2.center_y < UPPER_CORRIDOR:
                self.player2.player_to_up(self.wall_list)

        elif button == arcade.key.S:
            if self.player2.center_y > BOTTOM_CORRIDOR:
                self.player2.player_to_down(self.wall_list)

    def on_key_press(self, pushed_button, modifier):
        self.move_player_1(pushed_button)
        self.move_player_2(pushed_button)

    def on_mouse_press(self, x, y, button, modifier):
        print("You are in a freakin' forest :)")

    def update(self, delata_time):
        # Coin acquisition:
        acquired_coins = arcade.check_for_collision_with_list(self.player1, self.coin_list)
        for coin in acquired_coins:
            coin.kill()
            self.gold += coin.gold_value
            Coin.counter -= 1

        acquired_coins2 = arcade.check_for_collision_with_list(self.player2, self.coin_list)
        for coin in acquired_coins2:
            coin.kill()
            self.gold2 += coin.gold_value
            Coin.counter -= 1

        #Battle:
        enemy_in_battle = arcade.check_for_collision_with_list(self.player1, self.enemy_list)

        for enemy in enemy_in_battle:
            chance = randint(1,2)
            if chance == 1:
                self.lost_life()
                self.player1.center_x -= FIELD_SIZE * 2
            else:
                self.new_life()
                enemy.kill()

        enemy_in_battle2 = arcade.check_for_collision_with_list(self.player2, self.enemy_list)
        for enemy in enemy_in_battle2:
            chance = randint(1,2)
            if chance == 1:
                self.health2 -= 1
                self.player2.center_x -= FIELD_SIZE * 2
            else:
                self.health2 += 1
                enemy.kill()

        #Chest operations:
        chest_opened = arcade.check_for_collision_with_list(self.player1, self.chest_list)

        for chest in chest_opened:
            if chest.open_status == True:
                if bool(chest.objects) != False:
                    loot = ", ".join(chest.objects)
                    self.player1.loot += chest.loot_to_player()
                    print("Player 1 looted:", chest.objects)
                    chest.objects = []
            else:
                if chest.chest_message_player_1 == 0:
                    print("Player 1: Sorry, the chest is closed :(")
                    chest.chest_message_player_1 = 1
                else:
                    pass


        chest_opened2 = arcade.check_for_collision_with_list(self.player2, self.chest_list)

        for chest in chest_opened2:
            if chest.open_status == True:
                if bool(chest.objects) != False:
                    loot = ", ".join(chest.objects)
                    self.player2.loot += chest.loot_to_player()
                    print("Player 2 looted:", chest.objects)
                    chest.objects = []
            else:
                if chest.chest_message_player_2 == 0:
                    print("Player 2: Sorry, the chest is closed :(")
                    chest.chest_message_player_2 = 1
                else:
                    pass

        #Game Over:

        if self.player1.health <= 0 or self.player2.health <= 0 or Coin.counter == 0:
            print("GAME OVER")
            if bool(self.player1.loot) != False:
                print("Player 1 looted:", ", ".join(self.player1.loot) + ".")
            print("Player 1 gold:", self.gold)

            if bool(self.player2.loot) != False:
                print("Player 2 looted:", ", ".join(self.player2.loot) + ".")
            print("Player 2 gold:", self.gold2)
            self.close()

    def new_life(self):
        new_life_sprite = arcade.Sprite("img/Heart.png")
        new_life_sprite.center_x = self.health * FIELD_SIZE + FIELD_SIZE / 2
        new_life_sprite.center_y = BG_HEIGHT - FIELD_SIZE / 2
        self.health_symbol_list.append(new_life_sprite)
        self.health += 1

    def lost_life(self):
        lost_health = self.health_symbol_list[self.health - 1]
        lost_health.kill()
        self.health -= 1

if __name__ == "__main__":
    game = WarriorGame()
    game.start()