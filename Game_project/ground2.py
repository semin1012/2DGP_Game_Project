from pico2d import *
import main_state
from main_state import *
from background import Background
import character


class Ground2:
    image1 = None
    image2 = None

    def __init__(self, x = 60, y = 150):
        if Ground2.image1 == None:
            Ground2.image1 = load_image('mario_tile1.png')

        if Ground2.image2 == None:
            Ground2.image2 = load_image('mario_tile2.png')

        self.x, self.y = x, y

    def update(self):
        pass

    def draw(self):
        if main_state.stage == 1:
            Ground2.image1.draw(self.x - Background.backgroundX, self.y)

        elif main_state.stage == 2:
            Ground2.image2.draw(self.x - Background.backgroundX, self.y)


        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if main_state.stage == 1:
            return self.x - 15 - Background.backgroundX, self.y - 15, self.x + 15 - Background.backgroundX, self.y + 15
        elif main_state.stage == 2:
            return self.x - 29 - Background.backgroundX, self.y - 16, self.x + 29 - Background.backgroundX, self.y + 16

