from pico2d import *
import main_state
from main_state import *
from main_state2 import *
from main_state3 import *
from background import Background
from character import Character

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_COIN = 24

class Coin:
    coin_num = 0

    def __init__(self, x = 60, y = 15):
        self.image_coin = load_image('coin.png')
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.x, self.y = x, y


    def update(self):
        self.frame = (self.frame + FRAMES_PER_COIN * ACTION_PER_TIME * game_framework.frame_time) % 24

    def get_bb(self):
        # fill here
       return self.x - 15 - Background.backgroundX, self.y - 15, self.x + 15 - Background.backgroundX, self.y + 15

    def draw(self):
        self.image_coin.clip_composite_draw(0, 0, 30, 30, 0, '', 700, 570, 20, 20)

        # self.image_coin.clip_draw(int(self.frame) * 30, 0, 30, 30, self.x - Background.backgroundX, self.y)
        self.image_coin.clip_composite_draw(int(self.frame) * 30, 0, 30, 30, 0, '', self.x - Background.backgroundX, self.y, 30, 30)

        # draw_rectangle(*self.get_bb())