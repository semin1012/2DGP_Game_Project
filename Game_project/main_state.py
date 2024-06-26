import random
import json
import os

import gameover_state
import game_framework
import game_world
import main_state2
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
from green import Green
from pupple import Pupple
from background import Background
from path import Path
from server import *
from key import Key

import title_state
name = "MainState"

background = None
mario = None
monsters = None
monsters2 = None
Brick1 = None
Brick2 = None
Brick3 = None
Brick4 = None
questions = None
coins = None
coins3 = None
stage = 1
hearts = None
star = None
path = None
path2 = None
green = None
green2 = None
pupple = None
pupple2 = None
damage = None
attack = None
key = None
font = None


heart_num = None
heart_check = None


brick1_1 = [ -1, -1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
             -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

brick1_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 1, 1]

coin2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1]

brick2_2 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 1, 1]


brick2_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 0]

coin2_2 = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
            0, 0, 1, 1, 1, 1, 1, 1]

coin3_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 0]




brick3_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 0, 0]

brick3_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 1]

coin2_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 0, 0]

coin3_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 1, 1]


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b - 10: return False
    if right_a < left_b + 10: return False
    if top_a < bottom_b + 10 : return False
    if bottom_a > top_b - 10: return False

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

monster_list = [1100, 1200, 1150, 1050, 2000, 2050, 2100]
monster_list2 = [1100, 1200, 1150, 1400, 1450, 2500, 2950]
monster_list3 = [1100, 1150, 1200, 1250, 1600, 1650, 2250, 2550, 2600, 3100, 2950, 4100, 4900]
monster_list_top3 = [60, 60, 60, 60, 190, 190, 190, 60, 60, 60, 190, 190, 60]

monster_list_top = [60, 60, 60, 190, 190, 60, 190]
monster_list_right = [2000, 2050, 2100, 3500, 3550]
monster_list_right2 = [2000, 2050, 2100, 3500, 3550, 5000, 5050, 5100, 5150, 6300, 6350]
monster_list_right3 = [2050, 2100, 3500, 3550, 5500, 5550, 5100, 5150, 6300, 6350]

heart_list = [50, 100, 150]
question_list = [900, 1050, 1100, 3500]
question_list2 = [800, 1550, 2000, 3500, 5000]
question_list3 = [4000, 6000]
question_list_top = [150, 150, 300, 150]
question_list_top2 = [300, 450, 300, 150, 150]
question_list_top3 = [300, 450]



def enter():
    global background, mario, Brick1, Brick2, stage, brick1_1, coins, monsters, monsters2, hearts, damage, questions, star, green
    global pupple, green2, path, Brick3, key, font, heart_check

    font = load_font('ENCR10B.TTF', 16)
    Background.backgroundX = 600
    heart_check = 0
    damage = 0
    mario = Character()
    background = Background()
    hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
    game_world.add_object(mario, 1)
    game_world.add_object(background, 0)
    game_world.add_objects(hearts, 1)



    if stage == 1:
        Brick1 = [Ground(brick1_1[i] * 54 + 54 * i, 15) for i in range(len(brick1_1))]
        Brick2 = [Ground2(brick1_2[i] * 30 * i, 150) for i in range(len(brick1_2))]
        questions = [Question(question_list[i], question_list_top[i]) for i in range(len(question_list))]

        star = Star(question_list[0], 150)
        green = Green(question_list[1], 150)
        green2 = Green(question_list[3], 150)
        pupple = Pupple(question_list[2], 300)
        path = Path()

        coins = [Coin(coin2[i] * 30 * i, 185) for i in range(len(coin2))]
        monsters = [Monster(monster_list[i], 60) for i in range(len(monster_list))]
        monsters2 = [Monster(monster_list_right[i], 60, 1) for i in range(len(monster_list_right))]
        # game_world.add_object(Brick1, 0)


    game_world.add_objects(Brick1, 0)
    game_world.add_objects(Brick2, 0)
    game_world.add_objects(coins, 0)
    game_world.add_objects(monsters, 1)
    game_world.add_objects(monsters2, 1)
    game_world.add_objects(questions, 1)
    game_world.add_object(star, 0)
    game_world.add_object(green, 0)
    game_world.add_object(green2, 0)
    game_world.add_object(pupple, 0)
    game_world.add_object(path, 2)

def exit():
    game_world.clear()
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global background, mario, Brick1, Brick2, stage, brick1_1, coins, monsters, monsters2, hearts, damage, questions, star, green
    global pupple, green2, path, brick2_2, Brick3, coins3
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and collide_bottom(mario, path) and stage == 1:
            Background.backgroundX = 800
            stage = 2
            game_framework.change_state(main_state2)


        else:
            mario.handle_event(event)

def update():
    global coin_check, monster_check, damage, hearts, heart_list, question_list, questions, star, attack, green, heart_num, stage
    global heart_check, coins3, green2, question_collide

    heart_num = len(heart_list)

    for game_object in game_world.all_objects():
        game_object.update()

    for coin in coins:
        if collide(mario, coin):
            mario.coin_sound()
            Coin.coin_num += 10
            coins.remove(coin)
            game_world.remove_object(coin)


    for question in questions:
        if collide_top(mario, question):
            question.sound()
            JumpState.jump_high = -2
            question.image = 1
            if star.y == question.y and star.x == question.x:
                Star.move = 1
            if green.y == question.y and green.x == question.x:
                green.move = 1
            if green2.y == question.y and green2.x == question.x:
                green2.move = 1
            if pupple.y == question.y and pupple.x == question.x:
                Pupple.move = 1

        if JumpState.jump_high <= 0:

            if stage == 1:
                if collide_bottom(mario, questions[2]):
                    Character.jump_timer = 0
                    JumpState.jump_high = 0
                    Character.y = 300 + 45
                    JumpState.jump = 1
                elif collide_bottom(mario, question):
                    Character.jump_timer = 0
                    JumpState.jump_high = 0
                    Character.y = 150 + 45
                    JumpState.jump = 1



    for monster in monsters:
        if collide_bottom(mario, monster) and JumpState.jump_high <= 0:
            mario.monster_sound()
            monsters.remove(monster)
            game_world.remove_object(monster)
        elif collide(mario, monster):
            if Character.item2 == 1:
                damage = 1
                Character.item2 = 0
            elif damage == 0:
                if heart_num > 1:
                    mario.damage_sound()

                    for heart in hearts:
                        game_world.remove_object(heart)

                    hearts.clear()

                    heart_list.pop()

                    hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
                    game_world.add_objects(hearts, 1)

                    damage = 1
                else:      # heart_num == 0일 때 처리 필요
                    game_framework.change_state(gameover_state)
                    if Coin.coin_num - 100 >= 0:
                        Coin.coin_num -= 100
                    else:
                        Coin.coin_num = 0


    for monster in monsters2:
        if collide_bottom(mario, monster) and JumpState.jump_high <= 0:
            mario.monster_sound()
            monsters2.remove(monster)
            game_world.remove_object(monster)

        elif collide(mario, monster):
            if Character.item2 == 1:
                Character.item2 = 0
                damage = 1
            if damage == 0:
                if heart_num > 1:
                    mario.damage_sound()

                    for heart in hearts:
                        game_world.remove_object(heart)

                    hearts.clear()

                    heart_list.pop()

                    hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
                    game_world.add_objects(hearts, 1)

                    damage = 1

                else:         # heart_num == 0일 때 처리 필요
                    game_framework.change_state(gameover_state)
                    if Coin.coin_num - 100 >= 0:
                        Coin.coin_num -= 100
                    else:
                        Coin.coin_num = 0


    for brick in Brick1:
        if JumpState.jump_high <= 0:
            if collide(mario, brick):
                Character.jump_timer = 0
                JumpState.jump_high = 0
                Character.y = 15 + 40
                JumpState.jump = 1

    for brick in Brick2:
        if JumpState.jump_high <= 0:
            if collide_bottom(mario, brick):
                JumpState.jump_high = 0
                Character.jump_timer = 0
                Character.y = 150 + 40
                JumpState.jump = 1

    if stage >= 2:
        for brick in Brick3:
            if JumpState.jump_high <= 0:
                if collide_bottom(mario, brick):
                    JumpState.jump_high = 0
                    Character.jump_timer = 0
                    Character.y = 300 + 40
                    JumpState.jump = 1

    if collide(mario, star):
        Character.item1 = 0
        Character.item2 = 1
        game_world.remove_object(star)


    if collide_bottom(mario, path) and Character.next_state_table == 0:
        JumpState.jump_high = 0
        Character.jump_timer = 0
        Character.y = 115
        JumpState.jump = 1


    if collide(mario, green):

        for heart in hearts:
            game_world.remove_object(heart)

        hearts.clear()

        if heart_num > 0:
            heart_list.append(heart_list[heart_num - 1] + 50)
        # else:
        #     heart_list.insert(heart_num + 1, 50)

        hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
        game_world.add_objects(hearts, 1)

        game_world.remove_object(green)
        green = Green(8000, 150)

    if collide(mario, green2):

        for heart in hearts:
            game_world.remove_object(heart)

        hearts.clear()

        if heart_num >  0:
            heart_list.append(heart_list[heart_num - 1] + 50)
        # else:
            # heart_list.insert(heart_num + 1, 50)

        hearts = [Heart(heart_list[i]) for i in range(len(heart_list))]
        game_world.add_objects(hearts, 1)

        game_world.remove_object(green2)
        green2 = Green(8000, 150)


    if collide(mario, pupple):
        pupple.sound()
        game_world.remove_object(pupple)
        if Character.item1 == 0:
            Character.item2 = 0
            Character.item1 = 1
        elif Character.item1 == 1:
            pass    # 게임 오버 되어야 함



def draw():
    global font
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    font.draw(720, 570, '%d' % Coin.coin_num, (255, 255, 0))
    update_canvas()
