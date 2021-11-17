import main_state
from main_state import *
from background import Background

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_COIN = 5

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER )

class Star:
    move = 0
    def __init__(self, x = 60, y = 15):
        self.image_star = load_image('star.png')
        self.frame = 0
        self.x, self.y = x, y
        self.up = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_COIN * ACTION_PER_TIME * game_framework.frame_time) % 5

        if Star.move == 1:
            if self.up <= 33:
                self.y += RUN_SPEED_PPS * game_framework.frame_time
                self.up += RUN_SPEED_PPS * game_framework.frame_time


    def get_bb(self):
        # fill here
       return self.x - 15 - Background.backgroundX, self.y - 15, self.x + 15 - Background.backgroundX, self.y + 15

    def draw(self):
        self.image_star.clip_composite_draw(int(self.frame) * 652, 0, 652, 660, 0, '', self.x - Background.backgroundX, self.y, 30, 30)
        draw_rectangle(*self.get_bb())