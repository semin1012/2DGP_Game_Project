import random
import json
import os

import gameover_state
import game_framework
import game_world
import main_state
import gameclear_state
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
from key import Key
from peach import Peach

import title_state
name = "MainState3"

path3 = None
peach = None

def enter():
    global path3, peach
    brick4 = [ -1600 + 58 * i for i in range(20)]

    if main_state.stage == 3:

        main_state.heart_check = 0
        main_state.damage = 0
        main_state.hearts = [Heart(main_state.heart_list[i]) for i in range(len(main_state.heart_list))]
        game_world.add_object(main_state.mario, 1)
        game_world.add_object(main_state.background, 0)
        game_world.add_objects(main_state.hearts, 1)


        main_state.Brick4 = [Ground(brick4[i]) for i in range(len(brick4))]
        main_state.Brick2 = [Ground2(main_state.brick3_2[i] * 58 * i, 150) for i in range(len(main_state.brick3_2))]
        main_state.Brick3 = [Ground2(main_state.brick3_3[i] * 58 * i, 300) for i in range(len(main_state.brick3_3))]
        main_state.coins = [Coin(main_state.coin2_3[i] * 58 * i, 185) for i in range(len(main_state.coin2_3))]
        main_state.coins3 = [Coin(main_state.coin3_3[i] * 58 * i, 335) for i in range(len(main_state.coin3_3))]
        main_state.questions = [Question(main_state.question_list3[i], main_state.question_list_top3[i]) for i in range(len(main_state.question_list3))]
        main_state.monsters = [Monster(main_state.monster_list3[i], main_state.monster_list_top3[i]) for i in range(len(main_state.monster_list3))]
        main_state.monsters2 = [Monster(main_state.monster_list_right3[i], 60, 1) for i in range(len(main_state.monster_list_right3))]
        main_state.star = Star(main_state.question_list3[0], 300)
        main_state.path = Path(300, 55)
        main_state.path2 = Path(600, 55)
        path3 = Path(-700, 55)
        main_state.pupple = Pupple(6000, 450)
        main_state.pupple2 = Pupple(9000, 300)
        main_state.green = Green(4000, 300)
        main_state.green2 = Green(9000, 150)
        main_state.key = Key(-1000, 55)
        peach = Peach(-1400, 65)


        game_world.add_objects(main_state.Brick4, 0)
        game_world.add_objects(main_state.Brick2, 0)
        game_world.add_objects(main_state.Brick3, 0)
        game_world.add_objects(main_state.coins, 0)
        game_world.add_objects(main_state.coins3, 0)
        game_world.add_objects(main_state.questions, 1)
        game_world.add_object(main_state.star, 0)
        game_world.add_object(main_state.green, 0)
        game_world.add_object(main_state.green2, 0)
        game_world.add_object(main_state.pupple, 0)
        game_world.add_object(main_state.pupple2, 0)
        game_world.add_objects(main_state.monsters, 1)
        game_world.add_objects(main_state.monsters2, 1)
        game_world.add_object(main_state.path2, 2)
        game_world.add_object(path3, 2)
        game_world.add_object(main_state.path, 2)
        game_world.add_object(main_state.key, 1)
        game_world.add_object(peach, 2)


def exit():
    game_world.clear()
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    global path3
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and main_state.collide_bottom(main_state.mario, main_state.path) and main_state.stage == 3:
            Character.x = 500
            Background.backgroundX = -1200
            main_state.stage = 4

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and main_state.collide_bottom(main_state.mario, path3):
            main_state.stage = 3
            Character.x = 300
            Background.backgroundX = 0

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP and main_state.collide_bottom(main_state.mario, main_state.path2) and main_state.stage == 3:
            main_state.stage = 5
            if Key.key_check == 0:
                game_framework.change_state(gameclear_state)
            else:
                Character.x = 500
                Background.backgroundX = -1600

            # game_framework.change_state(main_state_sc)
            # pass

        else:
            main_state.mario.handle_event(event)


def update():
    global path3

    main_state.heart_num = len(main_state.heart_list)

    for game_object in game_world.all_objects():
        game_object.update()

    for coin in main_state.coins:
        if main_state.collide(main_state.mario, coin):
            main_state.mario.coin_sound()
            Coin.coin_num += 10
            main_state.coins.remove(coin)
            game_world.remove_object(coin)

    if main_state.stage != 1:
        for coin in main_state.coins3:
            if main_state.collide(main_state.mario, coin):
                main_state.mario.coin_sound()
                Coin.coin_num += 10
                main_state.coins3.remove(coin)
                game_world.remove_object(coin)

    for question in main_state.questions:
        if main_state.collide_top(main_state.mario, question):
            question.sound()
            JumpState.jump_high = -2
            question.image = 1
            if main_state.star.y == question.y and main_state.star.x == question.x:
                Star.move = 1
            if main_state.green.y == question.y and main_state.green.x == question.x:
                main_state.green.move = 1
            if main_state.green2.y == question.y and main_state.green2.x == question.x:
                main_state.green2.move = 1
            if main_state.pupple.y == question.y and main_state.pupple.x == question.x:
                main_state.Pupple.move = 1

        if JumpState.jump_high <= 0:
            if main_state.stage == 3:
                if main_state.collide_bottom(main_state.mario, main_state.questions[0]):
                    Character.jump_timer = 0
                    JumpState.jump_high = 0
                    Character.y = 300 + 45
                    JumpState.jump = 1

                if main_state.collide_bottom(main_state.mario, main_state.questions[1]):
                    Character.jump_timer = 0
                    JumpState.jump_high = 0
                    Character.y = 450 + 45
                    JumpState.jump = 1



    for monster in main_state.monsters:
        if main_state.collide_bottom(main_state.mario, monster) and JumpState.jump_high <= 0:
            main_state.mario.monster_sound()
            main_state.monsters.remove(monster)
            game_world.remove_object(monster)
        elif main_state.collide(main_state.mario, monster):
            if Character.item2 == 1:
                main_state.damage = 1
                Character.item2 = 0
            elif main_state.damage == 0:
                if main_state.heart_num > 1:
                    main_state.mario.damage_sound()

                    for heart in main_state.hearts:
                        game_world.remove_object(heart)

                    main_state.hearts.clear()

                    main_state.heart_list.pop()

                    main_state.hearts = [Heart(main_state.heart_list[i]) for i in range(len(main_state.heart_list))]
                    game_world.add_objects(main_state.hearts, 1)

                    main_state.damage = 1
                else:      # heart_num == 0일 때 처리 필요
                    game_framework.change_state(gameover_state)
                    if Coin.coin_num - 100 >= 0:
                        Coin.coin_num -= 100
                    else:
                        Coin.coin_num = 0


    for monster in main_state.monsters2:
        if main_state.collide_bottom(main_state.mario, monster) and JumpState.jump_high <= 0:
            main_state.mario.monster_sound()
            main_state.monsters2.remove(monster)
            game_world.remove_object(monster)

        elif main_state.collide(main_state.mario, monster):
            if Character.item2 == 1:
                Character.item2 = 0
                main_state.damage = 1
            if main_state.damage == 0:
                if main_state.heart_num > 1:
                    main_state.mario.damage_sound()

                    for heart in main_state.hearts:
                        game_world.remove_object(heart)

                    main_state.hearts.clear()

                    main_state.heart_list.pop()

                    main_state.hearts = [Heart(main_state.heart_list[i]) for i in range(len(main_state.heart_list))]
                    game_world.add_objects(main_state.hearts, 1)

                    main_state.damage = 1

                else:         # heart_num == 0일 때 처리 필요
                    game_framework.change_state(gameover_state)
                    if Coin.coin_num - 100 >= 0:
                        Coin.coin_num -= 100
                    else:
                        Coin.coin_num = 0

    if main_state.collide(main_state.mario, main_state.key):
        Key.key_check = 1



    for brick in main_state.Brick1:
        if JumpState.jump_high <= 0:
            if main_state.collide(main_state.mario, brick):
                Character.jump_timer = 0
                JumpState.jump_high = 0
                Character.y = 15 + 40
                JumpState.jump = 1

    for brick in main_state.Brick2:
        if JumpState.jump_high <= 0:
            if main_state.collide_bottom(main_state.mario, brick):
                JumpState.jump_high = 0
                Character.jump_timer = 0
                Character.y = 150 + 40
                JumpState.jump = 1

    if main_state.stage >= 2:
        for brick in main_state.Brick3:
            if JumpState.jump_high <= 0:
                if main_state.collide_bottom(main_state.mario, brick):
                    JumpState.jump_high = 0
                    Character.jump_timer = 0
                    Character.y = 300 + 40
                    JumpState.jump = 1

    for brick in main_state.Brick4:
        if JumpState.jump_high <= 0:
            if main_state.collide(main_state.mario, brick):
                Character.jump_timer = 0
                JumpState.jump_high = 0
                Character.y = 15 + 40
                JumpState.jump = 1

    if main_state.collide(main_state.mario, peach):
        game_framework.change_state(gameclear_state)

    if main_state.collide(main_state.mario, main_state.star):
        Character.item1 = 0
        Character.item2 = 1
        game_world.remove_object(main_state.star)


    if main_state.collide_bottom(main_state.mario, main_state.path) and Character.next_state_table == 0:
        JumpState.jump_high = 0
        Character.jump_timer = 0
        Character.y = 115
        JumpState.jump = 1


    if main_state.collide_bottom(main_state.mario, main_state.path2) and Character.next_state_table == 0:
        JumpState.jump_high = 0
        Character.jump_timer = 0
        Character.y = 115
        JumpState.jump = 1


    if main_state.collide_bottom(main_state.mario, path3) and Character.next_state_table == 0:
        JumpState.jump_high = 0
        Character.jump_timer = 0
        Character.y = 115
        JumpState.jump = 1


    if main_state.collide(main_state.mario, main_state.green):

        for heart in main_state.hearts:
            game_world.remove_object(heart)

        main_state.hearts.clear()

        if main_state.heart_num > 0:
            main_state.heart_list.append(main_state.heart_list[main_state.heart_num - 1] + 50)
        # else:
        #     heart_list.insert(heart_num + 1, 50)

        main_state.hearts = [Heart(main_state.heart_list[i]) for i in range(len(main_state.heart_list))]
        game_world.add_objects(main_state.hearts, 1)

        game_world.remove_object(main_state.green)
        main_state.green = Green(8000, 150)

    if main_state.collide(main_state.mario, main_state.green2):

        for heart in main_state.hearts:
            game_world.remove_object(heart)

        main_state.hearts.clear()

        if main_state.heart_num >  0:
            main_state.heart_list.append(main_state.heart_list[main_state.heart_num - 1] + 50)
        # else:
            # heart_list.insert(heart_num + 1, 50)

        main_state.hearts = [Heart(main_state.heart_list[i]) for i in range(len(main_state.heart_list))]
        game_world.add_objects(main_state.hearts, 1)

        game_world.remove_object(main_state.green2)
        main_state.green2 = Green(8000, 150)

    if main_state.collide(main_state.mario, main_state.pupple):
        main_state.pupple.sound()
        game_world.remove_object(main_state.pupple)
        if Character.item1 == 0:
            Character.item2 = 0
            Character.item1 = 1
        elif Character.item1 == 1:
            pass    # 게임 오버 되어야 함



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    main_state.font.draw(720, 570, '%d' % Coin.coin_num, (255, 255, 0))
    update_canvas()
