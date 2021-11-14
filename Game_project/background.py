from pico2d import *

import game_framework
import game_world

class Background:
    image = None
    backgroundX = 400

    def __init__(self):
        if Background.image == None:
            self.image = load_image('mario_background4.png')

    def draw(self):
        self.image.clip_draw(0 + Background.backgroundX, 0, 800, 600, 400, 300)

    def update(self):
        pass