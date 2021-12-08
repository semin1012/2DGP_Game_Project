import game_framework
from pico2d import *

import main_state
from main_state2 import *
from main_state3 import *
from background import Background

name = "TitleState"
image = None
title_frame = 0
title_sound = None

def enter():
    global image, title_frame, title_sound
    image = load_image('title.png')
    title_frame = 0
    title_sound = load_music('mario1.mp3')
    title_sound.set_volume(40)
    title_sound.play()
    Background.bgm = load_music('mario2.mp3')
    Background.bgm.set_volume(30)



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
                Background.bgm.play()
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 2:
                game_framework.change_state(main_state2)
                Background.bgm.play()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and main_state.stage == 3:
                game_framework.change_state(main_state3)
                Background.bgm.play()


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






