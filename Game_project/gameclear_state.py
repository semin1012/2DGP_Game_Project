from main_state3 import *
from main_state2 import *
from key import Key

name = "GameClearState"
image = None
image_key = None
clear_sound = None

def enter():
    global image, image_key, clear_sound
    image = load_image('gameclear.png')
    image_key = load_image('gameclear_key.png')
    clear_sound = load_music('clear.mp3')
    clear_sound.set_volume(40)
    clear_sound.play()

def exit():
    global image, image_key
    del(image)
    del(image_key)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Coin.coin_num = 0
                game_framework.change_state(title_state)



def draw():
    clear_canvas()
    if Key.key_check == 0:
        image.clip_draw(0, 0, 800, 600, 400, 300)
    else:
        image_key.clip_draw(0, 0, 800, 600, 400,  300)
    update()
    update_canvas()


def update():
    delay(0.05)


def pause():
    pass


def resume():
    pass






