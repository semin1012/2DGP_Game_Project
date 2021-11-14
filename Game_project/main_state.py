import random
import json
import os

import game_framework
import game_world
from pico2d import *

from character import Character
from object import Object
from background import Background

import title_state

name = "MainState"

background = None
mario = None
object = None
stage = None

# Game object class here

def enter():
    global background, mario, object, stage
    stage = 1
    mario = Character()
    background = Background()
    game_world.add_object(mario, 1)
    game_world.add_object(background, 0)


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
