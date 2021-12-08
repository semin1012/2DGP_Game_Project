import main_state
from main_state import *
from main_state2 import *
from main_state3 import *


class Peach:
    def __init__(self, x, y):
        self.image_peach = load_image('peach.png')
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        self.image_peach.clip_composite_draw(0, 0, 320, 600, 0, '', self.x - Background.backgroundX, self.y, 45, 90)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x  - Background.backgroundX - 25, self.y - 25, self.x  - Background.backgroundX + 25, self.y + 25
