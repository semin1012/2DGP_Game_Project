import main_state
from main_state import *
from main_state2 import *
from main_state3 import *
from background import Background

class Key:
    key_check = 0

    def __init__(self, x = 60, y = 50):
        self.image_key = load_image('key.png')
        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        if Key.key_check == 0:
            self.image_key.clip_composite_draw(0, 0, 600, 600, 0, '', self.x - Background.backgroundX, self.y, 50, 50)

        else:
            self.image_key.clip_composite_draw(0, 0, 600, 600, 0, '', 770, 570, 30, 30)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        # fill here
       return self.x - 25 - Background.backgroundX, self.y - 25, self.x + 25 - Background.backgroundX, self.y + 25
