import game_framework
from pico2d import *

import main_state
from main_state2 import *
from main_state3 import *

name = "TitleState"
image = None
title_frame = 0


def enter():
    global image, title_frame
    image = load_image('title.png')
    title_frame = 0


def exit():
    global image, title_frame
    del(image)
    del(title_frame)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 1 or (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 5:
                main_state.stage = 1
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 2:
                game_framework.change_state(main_state2)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 3:
                game_framework.change_state(main_state3)


def draw():
    clear_canvas()
    image.clip_draw(title_frame * 800, 0, 800, 600, 400, 300)
   # image.draw(400, 300)
    update()
    update_canvas()


def update():
    global title_frame
    title_frame = ( title_frame + 1 ) % 10
    delay(0.01)


def pause():
    pass


def resume():
    pass






