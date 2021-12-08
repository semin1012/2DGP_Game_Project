
import main_state
from main_state import *
from fire_ball import Fire_ball

import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0   # km / hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0 )
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER )

JUMP_PIXEL_PER_METER = 10.0 / 0.3
JUMP_SPEED_KMPH = 1.5
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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, JUMP_TIMER, DEBUG_KEY, ATTACK = range(8)

event_name = [ 'RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP', 'SPACE', 'JUMP_TIMER', 'DEBUG_KEY', 'ATTACK']
# background = Background()

history = []

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): DEBUG_KEY,   # 디버그 키(d): 히스토리를 볼 수 있다.

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_LCTRL): SPACE,
    (SDL_KEYDOWN, SDLK_z): ATTACK,
}



class Character:    # 마리오
    x, y = 400, 50
    item1 = 0
    item2 = 0
    next_state_table = 0
    ball = None
    def __init__(self):
        self.jump_sound = load_wav('jump.wav')
        self.jump_sound.set_volume(30)

        self.monsters_sound = load_wav('monster.wav')
        self.monsters_sound.set_volume(30)

        self.damages_sound = load_wav('damage.wav')
        self.damages_sound.set_volume(30)

        self.fires_sound = load_wav('fire.wav')
        self.fires_sound.set_volume(30)

        self.coins_sound = load_wav('coin.wav')
        self.coins_sound.set_volume(20)

        # self.cx, self.cy = 50, 0
        self.dir, self.cdir = 0, 0
        self.jump, self.jump_count = 0, 0

        self.image_org = load_image('mario_character.png')
        self.image_left = load_image('mario_left.png')
        self.image_right = load_image('mario_right.png')
        self.image_jump_left = load_image('mario_jump_left.png')
        self.image_jump_right = load_image('mario_jump_right.png')

        self.image_org_fire = load_image('mario_character_fire.png')
        self.image_left_fire = load_image('mario_left_fire.png')
        self.image_right_fire = load_image('mario_right_fire.png')
        self.image_jump_left_fire = load_image('mario_jump_left_fire.png')
        self.image_jump_right_fire = load_image('mario_jump_right_fire.png')

        self.frame = 0
        self.jump_timer = 0

        self.velocity = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.jump_num = 0
        self.jump_high = 100
        self.stop = 0

    def coin_sound(self):
        self.coins_sound.play()

    def monster_sound(self):
        self.monsters_sound.play()

    def damage_sound(self):
        self.damages_sound.play()

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

        if Character.next_state_table == 1:
            if Character.y >= 55:
                Character.y -= RUN_SPEED_PPS * game_framework.frame_time

            else:
                Character.next_state_table = 0
                main_state.stage = 2
                print(main_state.stage)

    def draw(self):         # 보는 방향에 대해 다른 sprite 적용
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())
        # debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir) + ' State: ' + str(self.cur_state))

    def fire_ball(self):
        # print('fire_ball')
        self.fires_sound.play()
        Character.ball = Fire_ball(Character.x, Character.y, self.dir)
        game_world.add_object(Character.ball, 1)
        pass

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            self.jump_sound.play()


        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if (DEBUG_KEY == key_event):
                print(history[-4:])
            else:
                self.add_event(key_event)


    def get_bb(self):
        # fill here
        if Character.item1 == 1:
            return Character.x - 17.25, Character.y - 22.5 - 10, Character.x + 17.25, Character.y + 22.5 - 10

        return Character.x - 23, Character.y - 30, Character.x + 23, Character.y + 30

class JumpState:
    jump_num = 0
    jump_high = 100
    stop = 0
    jump = 0
    jump_check = 0

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
            # print('ENTER JUMP')
            character.jump_timer = 1000
            JumpState.jump_num += 1
            JumpState.jump_high = 75
            JumpState.jump = 0
            main_state.damage = 0
        JumpState.stop = 0

    def exit(character, event):
        if event == SPACE and JumpState.jump == 1:
            JumpState.jump_num = 0
            Character.y += 1
            character.jump_timer = 1000

        if event == ATTACK:
            if Character.item2 == 1:
                character.fire_ball()

            else : pass
            # character.fire_ball()
            pass
        pass

    def do(character):
        if JumpState.stop != 1:
            if JumpState.jump_num == 1:
                character.frame = (character.frame + FRAMES_PER_JUMP * ACTION_PER_TIME * game_framework.frame_time) % 2
                character.jump_timer -= 1

                Character.y += JumpState.jump_high * JUMP_SPEED_PPS * game_framework.frame_time

                # print(RUN_SPEED_PPS)

                if main_state.stage <= 3:
                    if Character.x >= 390 and Character.x <= 410:
                        Background.backgroundX += int(character.velocity * game_framework.frame_time)

                    if Background.backgroundX <= 0 or Background.backgroundX >= 6700:
                        Character.x += character.velocity * game_framework.frame_time

                else:
                    Character.x += character.velocity * game_framework.frame_time
                Character.x = clamp(25, Character.x, 800 - 25)

                if character.jump_timer == 0:
                    character.add_event(JUMP_TIMER)
                    main_state.damage = 0
                    JumpState.jump_num = 0

                if Character.y > 15 + 40:
                    JumpState.jump_high -= 1
                Character.y = clamp(25, Character.y, 600 - 25)




    @staticmethod
    def draw(character):
        if character.dir == 1:
            if Character.item1 == 1:
                character.image_right.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_right_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y, 46, 60)
            else:
                character.image_right.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
            # character.image_jump_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)

        elif character.dir == 0 and Character.item2 == 1:
            character.image_org_fire.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)

        elif character.dir == 0 and Character.item1 == 1:
            character.image_org.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)

        elif character.dir == 0:
            character.image_org.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)


        else:
            if Character.item1 == 1:
                character.image_left.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_left_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y, 46, 60)
            else:
                character.image_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
            # character.image_jump_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)


class IdleState:
    def enter(character, event):
        global item2
        if event == RIGHT_DOWN:
            character.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            character.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            character.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            character.velocity += RUN_SPEED_PPS
        # item2 = 1

    def exit(character, event):
        if event == ATTACK:
            if Character.item2 == 1:
                character.fire_ball()
            else: pass

    def do(character):
        character.frame = (character.frame + FRAMES_PER_STOP * ACTION_PER_TIME * game_framework.frame_time) % 9


    def draw(character):
        if character.dir == 1:
            if Character.item1 == 1:
                character.image_org.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_org_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y, 46, 60)
            else:
                character.image_org.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)
        else:
            if Character.item1 == 1:
                character.image_org.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, 'h', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_org_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, 'h', Character.x, Character.y, 46, 60)
            else:
                character.image_org.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, 'h', Character.x, Character.y, 46, 60)


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
        if event == ATTACK:
            if Character.item2 == 1:
                character.fire_ball()
            else: pass


    def do(character):
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if main_state.stage != 4 and main_state != 5:
            if Character.x >= 390 and Character.x <= 410:
                Background.backgroundX += int(character.velocity * game_framework.frame_time)

            if Background.backgroundX <= 0 or Background.backgroundX >= 6700:
                Character.x += character.velocity * game_framework.frame_time
        else:
            Character.x += character.velocity * game_framework.frame_time
        Character.x = clamp(25, Character.x, 800 - 25)
        JumpState.stop = 0

    @staticmethod
    def draw(character):
        if character.dir == 1:
            # character.image.clip_composite_draw(character.frame * 100, 200, 100, 100, 0, '', Character.x + 25, Character.y - 25, 100, 100)
            if Character.item1 == 1:
                character.image_right.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_right_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y, 46, 60)
            else:
                character.image_right.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)

        else:
            if Character.item1 == 1:
                character.image_left.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y - 10, 34.5, 45)
            elif Character.item2 == 1:
                character.image_left_fire.clip_composite_draw(int(character.frame) * 46, 0, 46, 60, 0, '', Character.x, Character.y, 46, 60)
            else:
                character.image_left.clip_draw(int(character.frame) * 46, 0, 46, 60, Character.x, Character.y)



next_state_table = {
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, SPACE: JumpState, JUMP_TIMER: IdleState, ATTACK: JumpState},
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP_TIMER: RunState, SPACE: JumpState, ATTACK: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, JUMP_TIMER: IdleState, SPACE: JumpState, ATTACK: RunState}
}