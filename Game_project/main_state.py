import random
import json
import os

import game_framework
from pico2d import *
import title_state
open_canvas(800, 600)
name = "MainState"
backGround = None
Mario = None
object = None

brick1_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1]

brick1_2 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]

coin2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
         0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
         1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0]

coin3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
         0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0]

brick1_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0]

x, y = 50, 0
cx, cy = 400, 50
dir, cdir = 0, 0
jump, jump_count = 0, 0
cy_org = 0
cy_dir = 5
stage = 1

# Game object class here
class BackGround:
    def __init__(self):
        self.image = load_image('mario_background4.png')

    def draw(self):
        global x
        self.image.clip_draw(0 + x, 0, 800, 600, 400, 300)


class Character:                # 마리오
    def __init__(self):
        self.image_org = load_image('mario_character.png')
        self.image_left = load_image('mario_left.png')
        self.image_right = load_image('mario_right.png')
        self.image_jump_left = load_image('mario_jump_left.png')
        self.image_jump_right = load_image('mario_jump_right.png')
        self.frame = 0
        self.frame_jump = 0
        self.frame_run = 0

    def update(self):
        self.frame = (self.frame + 1) % 9               # 마리오 스탠드 이미지
        self.frame_jump = (self.frame_jump + 1) % 5     # 마리오 Jump 이미지
        self.frame_run = (self.frame_run + 1) % 2     # 마리오 Run 이미지

    def draw(self):         # 보는 방향에 대해 다른 sprite 적용
        global jump, dir, cdir, cx, cy
        if dir == 0 and cdir == 0 and jump == 0:
            self.image_org.clip_draw(self.frame*46, 0, 46, 60, cx, cy)
        elif jump == 1 or jump == 2:
            if dir == 1:
                self.image_jump_right.clip_draw(184 - self.frame_jump*46, 0, 46, 60, cx, cy)
            elif dir == -1:
                self.image_jump_left.clip_draw(self.frame_jump*46, 0, 46, 60, cx, cy)
            else:
                self.image_jump_right.clip_draw(184 - self.frame_jump*46, 0, 46, 60, cx, cy)
        elif dir == -1 or cdir == -1:
            self.image_left.clip_draw(self.frame_run*46, 0, 46, 60, cx, cy)
        elif dir == 1 or cdir == 1:
            self.image_right.clip_draw(self.frame_run*46, 0, 46, 60, cx, cy)

class Object:
    def __init__(self):
        self.image_brick1 = load_image('mario_tile4.png')
        self.image_brick2 = load_image('mario_tile2.png')
        self.image_brick3 = load_image('mario_tile3.png')
        self.image_coin = load_image('coin.png')
        self.coin_frame = 0

    def Coin_update(self):
        self.coin_frame = (self.coin_frame + 1) % 24

    def Brick_draw1(self):
        if stage == 1:
            for i in range(0, len(brick1_1)):
                self.image_brick1.clip_draw(0, 0, 54, 30, (54 * i) * brick1_1[i] - x, 15 - y)
                self.image_brick1.clip_draw(0, 0, 54, 30, (54 * i) * brick1_2[i] - x, 150 - y)
                self.image_brick1.clip_draw(0, 0, 54, 30, (54 * i) * brick1_3[i] - x, 300 - y)

    def Coin_draw1(self):
        if stage == 1:
            for i in range(1, len(coin2)):
                self.image_coin.clip_draw(self.coin_frame*35, 0, 35, 35, (54 * i) * coin2[i] - x, 200-y)
                self.image_coin.clip_draw(self.coin_frame*35, 0, 35, 35, (54 * i) * coin3[i] - x, 350-y)

def enter():
    global backGround, Mario, object, brick1_1, brick1_2, brick1_3, coin2, coin3
    backGround = BackGround()
    Mario = Character()
    object = Object()


def exit():
    global Mario, object, backGround
    del(Mario)
    del(object)
    del(backGround)

def pause():
    pass

def resume():
    pass

def update():
    Mario.update()
    object.Coin_update()


def draw():
    clear_canvas()
    backGround.draw()
    if stage == 1:
        object.Brick_draw1()
        object.Coin_draw1()
    Mario.draw()
    update_canvas()

def handle_events():
    global x
    global dir, cdir, jump, cy_org, cy_dir, jump_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.quit()
                if event.key == SDLK_LEFT:
                    dir = -1
                    cdir = -1
                    Mario.update()
                if event.key == SDLK_RIGHT:
                    dir = 1
                    cdir = 1
                if event.key == SDLK_SPACE:   # 스페이스바 = 점프
                    if jump_count < 2:          # 2단점프까지 가능
                        jump = 1
                        jump_count += 1
                        cy_org = cy
                        cy_dir = 5

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dir = 0
                cdir = 0
            elif event.key == SDLK_RIGHT:
                dir = 0
                cdir = 0

# initialization code

# game main loop code


while game_framework.running:
    if cx == 400:
        if x + 5 * dir >= 0 and x + 5 * dir <= 7500-800 :
            x += 7 * dir
        else:
            dir = 0
            cx += 5 * cdir

    else:
        cx += 5 * cdir
        state = 1
    state = 0
    # 발판에 발을 밝고 있을 때 state
    if stage == 1:
        for i in range(0, len(brick1_1)):
            if cx >= (54 * i * brick1_1[i] - x) - 30 and cx <= (54 * i * brick1_1[i] - x + 54) - 30 and cy >= 30 and cy <= 50:
                state = 1
                cy = 50
            if cx >= (54 * i * brick1_2[i] - x - 30) and cx <= (54 * i * brick1_2[i] - x + 54 - 30) and cy >= 140 and cy <= 190:
                state = 1
                cy = 190
            if cx >= (54 * i * brick1_3[i] - x - 30) and cx <= (54 * i * brick1_3[i] - x + 54 - 30) and cy >= 290 and cy <= 340:
                state = 1
                cy =340

        # if dir == 0:
        #     cx += 5 * cdir
        #     state = 1

        # 점프 위치에 따른 충돌처리, 땅 밝기
        if jump == 1:
            cy += 50 - cy_dir
            cy_dir += 5
            for i in range(0, len(brick1_1)):
                if cx >= (54 * i * brick1_1[i] - x ) and cx <= ( 54 * i * brick1_1[i] - x + 54 ) and cy <= 50:
                    cy = 50
                    jump = 0
                    jump_count = 0
                if cx >= (54 * i * brick1_2[i] - x - 30) and cx <= (54 * i * brick1_2[i] - x + 54 - 30) and cy >= 160 and cy <= 200:
                    cy = 190
                    jump = 0
                    jump_count = 0
                if cx >= (54 * i * brick1_3[i] - x - 30) and cx <= (54 * i * brick1_3[i] - x + 54 - 30) and cy >= 310 and cy <= 360:
                    cy = 340
                    jump = 0
                    jump_count = 0

    # 점프를 하지 않을 상태에서 추락할 때
    if state != 1:
        jump = 1
        if cy - 10 >= 20:
            cy -= 10
        for i in range(0, len(brick1_1)):
            if cx >= (54 * i * brick1_1[i] - x ) and cx <= ( 54 * i * brick1_1[i] - x + 54 ) and cy <= 50:
                cy = 50
                jump = 0
                jump_count = 0
            if cx >= (54 * i * brick1_2[i] - x - 30) and cx <= (54 * i * brick1_2[i] - x + 54 - 30) and cy >= 160 and cy <= 200:
                cy = 190
                jump = 0
                jump_count = 0
            if cx >= (54 * i * brick1_3[i] - x - 30) and cx <= (54 * i * brick1_3[i] - x + 54 - 30) and cy >= 310 and cy <= 360:
                cy = 340
                jump = 0
                jump_count = 0

        # 추락 -> 체력 게이지 깎이게 구현해야 함
        if cy <= -10:
            cy = 50
            cx = 400
            jump = 0
            jump_count = 0
            x = 50
            y = 0

    # 오브젝트와 충돌 시 (코인)
    for i in range(len(coin2)):
        if cx >= (54 * i * coin2[i] - x - 30) and cx <= (54 * i * coin2[i] - x + 35 - 30) and cy >= 190 and cy <= 230:
            coin2[i] = 0
        if cx >= (54 * i * coin3[i] - x - 30) and cx <= (54 * i * coin3[i] - x + 35 - 30) and cy >= 340 and cy <= 380:
            coin3[i] = 0

    # if dir != 0 or cdir != 0:
    #     Mario.update()
    update()
    draw()

    # game draw
    delay(0.001)



# finalization code
close_canvas()