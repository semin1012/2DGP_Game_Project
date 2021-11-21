from pico2d import *
import main_state
from main_state import *
from background import Background
from character import Character

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_COIN = 24

class Coin:

    coin3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

    def __init__(self, x = 60, y = 15):
        self.image_coin = load_image('coin.png')
        self.frame = 0
        self.x, self.y = x, y

    def update(self):
        self.frame = (self.frame + FRAMES_PER_COIN * ACTION_PER_TIME * game_framework.frame_time) % 24

    # def draw(self):
    #     if main_state.stage == 1:
    #         self.image_brick2.draw(self.x - Background.backgroundX, self.y)
    #         # self.image_brick2.clip_draw(self.x, self.y, self.x + 54, self.y + 30, 54 - Background.backgroundX, self.y)

            # for i in range(0, len(Object.brick1_1)):
                # self.image_brick1.clip_draw(0, 0, 30, 30, (30 * i) * Object.brick1_2[i] - Background.backgroundX, self.y2)
                # self.image_brick1.clip_draw(0, 0, 30, 30, (30 * i) * Object.brick1_3[i] - Background.backgroundX, self.y3)


    def get_bb(self):
        # fill here
       return self.x - 15 - Background.backgroundX, self.y - 15, self.x + 15 - Background.backgroundX, self.y + 15

    def draw(self):
        self.image_coin.clip_draw(int(self.frame) * 30, 0, 30, 30, self.x - Background.backgroundX, self.y)
        draw_rectangle(*self.get_bb())