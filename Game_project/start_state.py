import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0
logo_sound = None

def enter():
    global image, logo_sound
    logo_sound = load_wav('logo.wav')
    image = load_image('credit.png')
    logo_sound.set_volume(30)
    logo_sound.play()


def exit():
    global image
    del(image)


def update():
    global logo_time

    if ( logo_time > 1.0 ):
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




