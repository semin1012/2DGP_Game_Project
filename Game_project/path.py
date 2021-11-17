import main_state
from main_state import *
from background import Background

class Path:
    def __init__(self, x = 4300, y = 65):
        self.image_path = load_image('mario_path.png')
        self.x, self.y = x, y
        self.up = 0

    def update(self):
        pass


    def get_bb(self):
       return self.x - 30 - Background.backgroundX, self.y - 30, self.x + 30 - Background.backgroundX, self.y + 30

    def draw(self):
        self.image_path.clip_composite_draw(0, 0, 118, 119, 0, '', self.x - Background.backgroundX, self.y, 60, 60)
        draw_rectangle(*self.get_bb())