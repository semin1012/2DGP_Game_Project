from pico2d import *
import game_framework
import main_state
from background import Background
from main_state import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER )


JUMP_PIXEL_PER_METER = 10.0 / 0.3
JUMP_SPEED_KMPH = 50
JUMP_SPEED_MPM = JUMP_SPEED_KMPH * 1000.0 / 60.0
JUMP_SPEED_MPS = JUMP_SPEED_MPM / 60.0
JUMP_SPEED_PPS = JUMP_SPEED_MPS * JUMP_PIXEL_PER_METER

# Character Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2
FRAMES_PER_JUMP = 5
FRAMES_PER_STOP = 9

# Character Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, JUMP_TIMER, DEBUG_KEY = range(7)

event_name = [ 'RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SPACE', 'JUMP_TIMER', 'DEBUG_KEY']
# background = Background()

history = []

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): DEBUG_KEY,   # 디버그 키(d): 히스토리를 볼 수 있다.

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
}

class Character:    # 마리오
    x, y = 400, 50
    def __init__(self):
        # self.cx, self.cy = 50, 0
        self.dir, self.cdir = 0, 0
        self.jump, self.jump_count = 0, 0

        self.image_org = load_image('mario_character.png')
        self.image_left = load_image('mario_left.png')
        self.image_right = load_image('mario_right.png')
        self.image_jump_left = load_image('mario_jump_left.png')
        self.image_jump_right = load_image('mario_jump_right.png')
        self.frame = 0
        self.jump_timer = 0

        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:        # 오류를 발견하려고 쓰는 코드
                history.append((self.cur_state.__name__, event_name[event]))    # 튜플로 넣어야 한다.
                self.cur_state = next_state_table[self.cur_state][event]
            except:     # 오류가 발생했다면 이 뒷 코드를 수행하는 것이 try - except 문법
                print('cur state:', self.cur_state.__name__, ' event:', event_name[event])
                # 오류가 나는 상태와 이벤트 값이 무엇인지 확인하고 next_state_table에 추가하면 됨
                exit(-1)    # 프로그램 종료
            self.cur_state.enter(self, event)

    def draw(self):         # 보는 방향에 대해 다른 sprite 적용
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        # debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir) + ' State: ' + str(self.cur_state))

    def character_jump(self):
        print('jump')

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if (DEBUG_KEY == key_event):
                print(history[-4:])
            else:
                self.add_event(key_event)

    def get_bb(self):
        # fill here
       return Character.x - 23, Character.y - 30, Character.x + 23, Character.y + 30

class JumpState:
    jump_num = 0
    jump_high = 100

    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        character.dir = clamp(-1, character.velocity, 1)
        if JumpState.jump_num == 0:
            print('ENTER JUMP')
            character.jump_timer = 400
            JumpState.jump_num += 1
            JumpState.jump_high = 75

    def exit(character, event):
        print('EXIT JUMP')  # 대쉬 상태 잘 나가는지 확인
        pass

    def do(character):
        if JumpState.jump_num == 1:
            character.frame = (character.frame + FRAMES_PER_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 5
            character.jump_timer -= 1

            Character.y += JumpState.jump_high * 13 * game_framework.frame_time

            if Background.backgroundX <= 0 or Background.backgroundX >= 4000:
                Character.x += character.velocity * game_framework.frame_time

            elif Character.x >= 395 and Character.x <= 405:
                Background.backgroundX += int(character.dir)

            Character.x = clamp(25, Character.x, 800 - 25)

            for brick in main_state.Brick1:
                if JumpState.jump_high <= 0:
                    if main_state.collide(main_state.mario, brick):
                        character.jump_timer = 0
                        Character.y = 15 + 40

            for brick in main_state.Brick2:
                if JumpState.jump_high <= 0:
                    if main_state.collide(main_state.mario, brick):
                        character.jump_timer = 0
                        Character.y = 150 + 40
                    else:
                        pass


            if character.jump_timer == 0:
                character.add_event(JUMP_TIMER)
                JumpState.jump_num = 0


            JumpState.jump_high -= 1
            Character.y = clamp(25, Character.y, 600 - 25)

    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.image_jump_right.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
        else:
            character.image_jump_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)


class IdleState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_STOP * ACTION_PER_TIME * game_framework.frame_time) % 9

    def draw(character):
        if character.dir == 1:
            character.image_org.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
        else:
            character.image_org.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)


class RunState:
    def enter(character, event):
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        character.dir = clamp(-1, character.velocity, 1)

    def exit(character, event):
        pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        if Character.x >= 395 and Character.x <= 405:
            Background.backgroundX += int(character.dir)

        if Background.backgroundX <= 0 or Background.backgroundX >= 4000:
            Character.x += character.velocity * game_framework.frame_time

        Character.x = clamp(25, Character.x, 800 - 25)

    @staticmethod
    def draw(character):
        if character.dir == 1:
            character.image_right.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
        else:
            character.image_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)



next_state_table = {
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, SPACE: JumpState, JUMP_TIMER: RunState},
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP_TIMER: RunState, SPACE: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, JUMP_TIMER: IdleState, SPACE: JumpState}
}
