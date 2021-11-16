from pico2d import *
import main_state
from main_state import *
from background import Background
import character


class Ground2:
    def __init__(self, x = 60, y = 150):
        self.image_brick1 = load_image('mario_tile1.png')
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        if main_state.stage == 1:
            self.image_brick1.draw(self.x - Background.backgroundX, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x - 17.5 - Background.backgroundX, self.y - 17.5, self.x + 17.5 - Background.backgroundX, self.y + 17.5
