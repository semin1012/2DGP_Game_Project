from pico2d import *
import main_state
from main_state import *
from background import Background
import character


TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_STOP = 9

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER )

class Fire_ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Fire_ball.image == None:
            Fire_ball.image = load_image('fire_ball.png')
        if velocity == 0:
            velocity = 1
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.move = 0

    def draw(self):
        # self.image.draw(self.x, self.y)
        Fire_ball.image.clip_composite_draw(int(self.frame) * 33 , 0, 33, 40, 0, '', self.x, self.y, 33, 40)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x - 16.5, self.y - 20, self.x + 16.5, self.y + 20


    def update(self):
        for monster in main_state.monsters2:
            if main_state.collide(self, monster):
                game_world.remove_object(self)
                main_state.monsters2.remove(monster)
                game_world.remove_object(monster)

        for monster in main_state.monsters:
            if main_state.collide(self, monster):
                game_world.remove_object(self)
                main_state.monsters.remove(monster)
                game_world.remove_object(monster)

        if self.move <= 250:
            self.x += int(self.velocity) * RUN_SPEED_PPS * game_framework.frame_time
            self.move += self.velocity * game_framework.frame_time
            self.frame = (self.frame + FRAMES_PER_STOP * ACTION_PER_TIME * game_framework.frame_time) % 9


        else: game_world.remove_object(self)
        # self.x += self.velocity

        # if self.x < 25 or self.x > 1600 - 25:
        #     game_world.remove_object(self)
