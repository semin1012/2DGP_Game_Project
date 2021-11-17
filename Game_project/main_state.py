import random
import json
import os

import game_framework
import game_world
from pico2d import *

from character import Character
from character import JumpState
from ground import Ground
from ground2 import Ground2
from question import Question
from coin import Coin
from monster import Monster
from heart import Heart
from star import Star
from background import Background

import title_state
name = "MainState"

background = None
mario = None
monsters = None
monsters2 = None
Brick1 = None
Brick2 = None
questions = None
coins = None
stage = None
hearts = None
star = None
damage = None
attack = None


brick1_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1]

coin2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]

brick1_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b - 5: return False
    if right_a < left_b + 5: return False
    if top_a < bottom_b + 5 : return False
    if bottom_a > top_b - 5: return False

    return True

def collide_top(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if top_a > top_b - 20: return False

    return True

def collide_bottom(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a  < left_b: return False
    if bottom_a > top_b: return False
    if bottom_a < bottom_b + 20: return False

    return True

monster_list = [1100, 1200, 1150, 1050]
monster_list_right = [2000, 2050, 2100]
heart_list = [50, 100, 150]
question_list = [900, 990]

def enter():
    global background, mario, Brick1, Brick2, stage, brick1_1, coins, monsters, monsters2, hearts, damage, questions, star
    stage = 1
    damage = 0
    mario = Character()
    background = Background()
    Brick1 = [Ground(brick1_1[i] * 54 + 54 * i, 15) for i in range(len(brick1_1))]
    Brick2 = [Ground2(brick1_2[i] * 30 * i, 150) for i in range(len(brick1_2))]
    questions = [Question(question_list[i], 150) for i in range(len(question_list))]

    star = Star(question_list[0], 150)

    coins = [Coin(coin2[i] * 30 * i, 185) for i in range(len(coin2))]
    monsters = [Monster(monster_list[i]) for i in range(len(monster_list))]
    monsters2 = [Monster(monster_list_right[i], 1) for i in range(len(monster_list_right))]
    hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
    game_world.add_object(mario, 1)
    game_world.add_object(background, 0)
    game_world.add_objects(Brick1, 0)
    game_world.add_objects(Brick2, 0)
    game_world.add_objects(coins, 0)
    game_world.add_objects(monsters, 1)
    game_world.add_objects(monsters2, 1)
    game_world.add_objects(hearts, 1)
    game_world.add_objects(questions, 1)
    game_world.add_object(star, 0)
    # game_world.add_object(Brick1, 0)


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
    global coin_check, monster_check, damage, hearts, heart_list, question_list, questions, star, attack

    for game_object in game_world.all_objects():
        game_object.update()

    for coin in coins:
        if collide(mario, coin):
            coins.remove(coin)
            game_world.remove_object(coin)

    for question in questions:
        if collide_top(mario, question):
            JumpState.jump_high = -2
            if star.y == question.y:
                Star.move = 1
            pass


    for monster in monsters:
        if collide_bottom(mario, monster) and JumpState.jump_high <= 0:
            monsters.remove(monster)
            game_world.remove_object(monster)
        elif collide(mario, monster) :
            if damage == 0:
                heart_num = len(heart_list) - 1
                if heart_num >= 0:
                    heart_list.remove(heart_list[heart_num])
                    game_world.remove_object(hearts[heart_num])
                    hearts.remove(hearts[heart_num])
                    damage = 1
                if heart_num == 0:      # heart_num == 0일 때 처리 필요
                    pass

    for monster in monsters2:
        if collide_bottom(mario, monster) and JumpState.jump_high <= 0:
            monsters2.remove(monster)
            game_world.remove_object(monster)

        elif collide(mario, monster):
            if damage == 0:
                heart_num = len(heart_list) - 1
                if heart_num > 0:
                    heart_list.remove(heart_list[heart_num])
                    game_world.remove_object(hearts[heart_num])
                    hearts.remove(hearts[heart_num])
                    damage = 1
                if heart_num == 0:         # heart_num == 0일 때 처리 필요
                    pass

    for brick in Brick1:
        if JumpState.jump_high <= 0:
            if collide(mario, brick):
                Character.y = 15 + 40
                Character.jump_timer = 0
                JumpState.jump_high = 0
                JumpState.jump = 1

    for brick in Brick2:
        if JumpState.jump_high <= 0:
            if collide_bottom(mario, brick):
                Character.y = 150 + 40
                JumpState.jump_high = 0
                Character.jump_timer = 0
                JumpState.jump = 1

    if collide(mario, star):

        game_world.remove_object(star)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
