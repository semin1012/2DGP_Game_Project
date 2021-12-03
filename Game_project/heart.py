import main_state
from main_state import *
from main_state2 import *
from main_state3 import *


class Heart:
    def __init__(self, x):
        self.image_heart = load_image('heart.png')
        self.x, self.y = x, 550

    def update(self):
        pass

    def draw(self):
        self.image_heart.clip_composite_draw(0, 0, 150, 150, 0, '', self.x, self.y, 50, 50)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x - 25, self.y - 25, self.x + 25, self.y + 25
