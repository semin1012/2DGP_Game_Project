from pico2d import *
import main_state
from main_state import *
from background import Background
from character import Character


class Ground:
    coin2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
             0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
             1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

    coin3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]

    brick1_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
                0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0]

    def __init__(self, x = 60, y = 15):
        self.image_brick1 = load_image('mario_tile1.png')
        self.image_brick2 = load_image('mario_tile4.png')
        self.image_coin = load_image('coin.png')
        self.coin_frame = 0
        self.x, self.y = x, y

    def Coin_update(self):
        self.coin_frame = (self.coin_frame + 1) % 24

    def update(self):
        pass

    def draw(self):
        if main_state.stage == 1:
            self.image_brick2.draw(self.x - Background.backgroundX, self.y)
            # self.image_brick2.clip_draw(self.x, self.y, self.x + 54, self.y + 30, 54 - Background.backgroundX, self.y)

            # for i in range(0, len(Object.brick1_1)):
                # self.image_brick1.clip_draw(0, 0, 30, 30, (30 * i) * Object.brick1_2[i] - Background.backgroundX, self.y2)
                # self.image_brick1.clip_draw(0, 0, 30, 30, (30 * i) * Object.brick1_3[i] - Background.backgroundX, self.y3)

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
       return self.x - 27 - Background.backgroundX, self.y - 15, self.x + 27 - Background.backgroundX, self.y + 15

    def Coin_draw1(self):
        if stage == 1:
            for i in range(1, len(Ground.coin2)):
                self.image_coin.clip_draw(self.coin_frame*35, 0, 35, 35, (54 * i) * Ground.coin2[i] - Background.backgroundX, 200-Character.y)
                self.image_coin.clip_draw(self.coin_frame*35, 0, 35, 35, (54 * i) * Ground.coin3[i] - Background.backgroundX, 350-Character.y)
