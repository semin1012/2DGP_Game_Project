import main_state
from main_state import *
from main_state2 import *
from main_state3 import *
from background import Background


class Question:
    def __init__(self, x = 60, y = 150):
        self.image_question = load_image('question.png')
        self.image_ground = load_image('question_1.png')
        self.x, self.y = x, y
        self.image = 0

    def update(self):
        pass

    def draw(self):
        if self.image == 0:
            self.image_question.draw(self.x - Background.backgroundX, self.y)

        elif self.image == 1:
            self.image_ground.draw(self.x - Background.backgroundX, self.y)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
       return self.x - 15 - Background.backgroundX, self.y - 15, self.x + 15 - Background.backgroundX, self.y + 15
