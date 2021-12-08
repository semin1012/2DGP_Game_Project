import game_framework
from pico2d import *

import start_state
import main_state
from main_state3 import *
from main_state2 import *
from pupple import Pupple
from green import Green
from star import Star

from background import Background

name = "GameOverState"
image = None
gameover_frame = 0
gameover_sound = None


def enter():
    global image, gameover_frame, gameover_sound

    gameover_sound = load_music('gameover.mp3')
    gameover_sound.set_volume(40)
    gameover_sound.play()
    image = load_image('gameover.png')
    gameover_frame = 0


def exit():
    global image, gameover_frame
    del(image)
    del(gameover_frame)
    main_state.heart_list = [50, 100, 150]


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)
                Pupple.move = 0
                Star.move = 0
                Green.move = 0


def draw():
    clear_canvas()
    image.clip_draw(gameover_frame * 800, 0, 800, 600, 400, 300)
   # image.draw(400, 300)
    update()
    update_canvas()


def update():
    global gameover_frame
    gameover_frame = ( gameover_frame + 1 ) % 5
    delay(0.05)


def pause():
    pass


def resume():
    pass






