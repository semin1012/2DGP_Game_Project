from pico2d import *
import main_state
from main_state import *
from background import Background
import character


TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_STOP = 7

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 5.0   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER )


class Monster:
    def __init__(self, x = 300, y = 60, dir = 0):
        self.monster_image = load_image('monster.png')
        self.frame = 0
        self.dir = dir
        if self.dir == 0:
            self.move = 0
        else: self.move = 400
        self.x, self.y = x, y
        self.velocity = RUN_SPEED_PPS

    def update(self):
        # print(self.velocity *game_framework.frame_time )
        if self.dir == 0:
            if self.move <= 400:
                self.frame = (self.frame + FRAMES_PER_STOP * ACTION_PER_TIME * game_framework.frame_time) % 7
                self.x += self.velocity * game_framework.frame_time
                self.move += self.velocity * game_framework.frame_time
            else: self.dir = 1

        elif self.dir == 1:
            if self.move >= 0:
                self.frame = (self.frame + FRAMES_PER_STOP * ACTION_PER_TIME * game_framework.frame_time) % 7
                self.x -= self.velocity * game_framework.frame_time
                self.move -= self.velocity * game_framework.frame_time
            else: self.dir = 0


    def draw(self):
        if self.dir == 1:
            self.monster_image.clip_composite_draw(int(self.frame) * 170, 0, 170, 190, 0, '', self.x - Background.backgroundX, self.y - 10, 51, 57)

        elif self.dir == 0:
            self.monster_image.clip_composite_draw(int(self.frame) * 170, 0, 170, 190, 0, 'h', self.x - Background.backgroundX, self.y - 10, 51, 57)

        # draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x - 25.5 - Background.backgroundX, self.y - 28.5 - 10, self.x + 25.5 - Background.backgroundX, self.y + 28.5 - 10
