from pico2d import *
from main_state import *
from main_state2 import *
from main_state3 import *
import main_state

import game_framework
import game_world

class Background:
    image = None
    image2 = None
    image3 = None
    image4 = None
    image5 = None
    image5_key = None
    image_path = None
    backgroundX = 3800
    bgm = None

    def __init__(self):

        Background.bgm = load_music('mario2.mp3')
        Background.bgm.set_volume(64)

        if main_state.stage < 5:
            self.bgm.play()

        if Background.image == None:
            Background.image = load_image('mario_background4.png')

        if Background.image2 == None:
            Background.image2 = load_image('mario_background2.png')

        if Background.image3 == None:
            Background.image3 = load_image('mario_background3.png')

        if Background.image4 == None:
            Background.image4 = load_image('mario_background5.png')

        if Background.image5_key == None:
            Background.image5_key = load_image('key_background.png')

    def draw(self):
        if main_state.stage == 1:
            Background.image.clip_draw(0 + Background.backgroundX, 0, 800, 600, 400, 300)
        elif main_state.stage == 2:
            Background.image2.clip_draw(0 + Background.backgroundX, 0, 800, 600, 400, 300)
        elif main_state.stage == 3:
            Background.image3.clip_draw(0 + Background.backgroundX, 0, 800, 600, 400, 300)
        elif main_state.stage == 4:
            Background.image4.clip_draw(0, 0, 800, 600, 400, 300)

        elif main_state.stage == 5:
            Background.image5_key.clip_draw(0, 0, 800, 600, 400, 300)


    def update(self):
        pass