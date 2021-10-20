from pico2d import *
import random

# Game object class here
class BackGround:
    def __init__(self):
        self.image = load_image('mario_background1.png')

    def draw(self):
        self.image.clip_draw(0 + x, 0, 800, 600, 400, 300)


class Character:                # 마리오
    def __init__(self):
        self.image_left = load_image('mario_org_run_left.png')
        self.image_right = load_image('mario_org_run_right.png')
        self.image_jump_left = load_image('mario_org_jump_left.png')
        self.image_jump_right = load_image('mario_org_jump_right.png')
        self.frame = 0
        self.frame_jump = 0

    def update(self):
        self.frame = (self.frame + 1) % 2               # 마리오 RUN 이미지
        self.frame_jump = (self.frame_jump + 1) % 5     # 마리오 Jump 이미지

    def draw(self):         # 보는 방향에 대해 다른 sprite 적용
        if jump == 1 or jump == 2:
            if dir == 1:
                self.image_jump_right.clip_draw(220 - self.frame_jump*56, 0, 56, 60, cx, cy)
            elif dir == -1:
                self.image_jump_left.clip_draw(self.frame_jump*56, 0, 56, 60, cx, cy)
            else:
                self.image_jump_right.clip_draw(220 - self.frame_jump*56, 0, 56, 60, cx, cy)
        elif dir == -1 or cdir == -1:
            self.image_left.clip_draw(self.frame*56, 0, 56, 60, cx, cy)
        elif dir == 1 or cdir == 1:
            self.image_right.clip_draw(self.frame*56, 0, 56, 60, cx, cy)
        elif dir == 0 or cdir == 0:
            self.image_right.clip_draw(self.frame*56, 0, 56, 60, cx, cy)

class Object:
    def __init__(self):
        self.image_brick1 = load_image('mario_tile1.png')
        self.image_brick2 = load_image('mario_tile2.png')
        self.image_brick3 = load_image('mario_tile3.png')

    def Brick_draw1(self):
        if stage == 1:
            for i in range(0, len(brick1_1)):
                self.image_brick1.clip_draw(0, 0, 60, 30, (60 * i) * brick1_1[i] - x, 15 - y)
                self.image_brick1.clip_draw(0, 0, 60, 30, (60 * i) * brick1_2[i] - x, 150 - y)
                self.image_brick1.clip_draw(0, 0, 60, 30, (60 * i) * brick1_3[i] - x, 300 - y)


def handle_events():
    global running
    global x
    global dir, cdir, jump, cy_org, cy_dir, jump_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    running = False
                elif event.key == SDLK_LEFT:
                    dir = -1
                    cdir = -1
                    Mario.update()
                elif event.key == SDLK_RIGHT:
                    dir = 1
                    cdir = 1
                elif event.key == SDLK_SPACE:   # 스페이스바 = 점프
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
open_canvas(800, 600)

backGround = BackGround()
Mario = Character()
object = Object()
brick1_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
          1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

brick1_2 = [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
          0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1,
          1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

brick1_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
          0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# team = [Boy() for i in range(1, 11+1)]



running = True
x, y = 5, 0
cx, cy = 400, 50
dir, cdir = 0, 0
jump, jump_count = 0, 0
cy_org = 0
cy_dir = 5
stage = 1

# game main loop code

while running:
    handle_events()

    # game logic
    # for boy in team:
    #     boy.update()
    # self.image_brick1.clip_draw(0, 0, 60, 30, (60 * i) * brick1[i] - x, 15 - y)

    if x + 5 * dir >= 0 and x + 5 * dir <= 7500-800 and cx != 300:
        x += 7 * dir
    else: dir = 0

    state = 0
    # 발판에 발을 밝고 있을 때 state
    if stage == 1:
        for i in range(0, len(brick1_1)):
            if cx >= (60 * i * brick1_1[i] - x) - 30 and cx <= (60 * i * brick1_1[i] - x + 60) - 30 and cy >= 30 and cy <= 50:
                state = 1
                cy = 50
            elif cx >= (60 * i * brick1_2[i] - x - 30) and cx <= (60 * i * brick1_2[i] - x + 60 - 30) and cy >= 160 and cy <= 200:
                state = 1
                cy = 190
            elif cx >= (60 * i * brick1_3[i] - x - 30) and cx <= (60 * i * brick1_3[i] - x + 60 - 30) and cy >= 310 and cy <= 350:
                state = 1
                cy =340
        if state != 1:
            cy -= 10

        if dir == 0:
            cx += 5 * cdir
            state = 1

        # 점프 위치에 따른 충돌처리, 땅 밝기
        if jump == 1:
            cy += 50 - cy_dir
            cy_dir += 5
            for i in range(0, len(brick1_1)):
                if cx >= (60 * i * brick1_1[i] - x ) and cx <= ( 60 * i * brick1_1[i] - x + 60 ) and cy <= 30:
                    cy = 50
                    jump = 0
                    jump_count = 0
                elif cx >= (60 * i * brick1_2[i] - x - 30) and cx <= (60 * i * brick1_2[i] - x + 60 - 30) and cy >= 160 and cy <= 200:
                    cy = 190
                    jump = 0
                    jump_count = 0
                elif cx >= (60 * i * brick1_3[i] - x - 30) and cx <= (60 * i * brick1_3[i] - x + 60 - 30) and cy >= 310 and cy <= 360:
                    cy = 340
                    jump = 0
                    jump_count = 0

        # 추락 -> 체력 게이지 깎이게 구현해야 함
        if cy <= 0:
            cy = 50
            cx = 400
            jump = 9
            jump_count = 0
            x = 5
            y = 0

    # if dir != 0 or cdir != 0:
    #     Mario.update()
    Mario.update()

    # game draw
    clear_canvas()
    backGround.draw()
    if stage == 1:
        object.Brick_draw1()
    Mario.draw()
    update_canvas()

    delay(0.001)



# finalization code
close_canvas()