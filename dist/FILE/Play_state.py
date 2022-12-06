from pico2d import *
import game_framework
import title_state
import random
import json
import os
import winsound
from zombie import Zombie
import game_world
from BehaviorTree import BehaviorTree, Selector, Sequence, Leaf




class Grass:
    def __init__(self):
        self.image = load_image('background2.png')

    class MUSIC:
        def __init__(self):
            self.bgm = load_music('MUSIC.mp3')
            self.bgm.set_volume(32)
            self.bgm.repeat_play()

    def draw(self):
        self.image.draw(800, 600)

class Boy:
    def __init__(self):
        self.x, self.y = 650, 1050
        self.frame = 0
        self.image = load_image('anim_sheet_3.png')
        self.image2 = load_image('anim_sheet_attack.png')

        self.dir_x = 0
        self.dir_y = 0
        self.dir_check = 0
        global dir_x
        global dir_y


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += dir_x * 5
        self.y += dir_y * 5

        if self.dir_check == 1:
            self.dir_check = 200
        elif self.dir_check == -1:
            self.dir_check = 100
        elif self.dir_check == 2:
            self.dir_check = 300
        elif self.dir_check == -2:
            self.dir_check = 0


    def draw(self):

        global dir_x
        global dir_y
        global attack



        if dir_x == 1:
            self.dir_check = 1
            delay(0.02)
            self.image.clip_draw(self.frame*64, 600, 64, 100, self.x, self.y)

        elif dir_x == -1:
            self.dir_check = -1
            delay(0.02)
            self.image.clip_draw(self.frame*64, 500, 64, 100, self.x, self.y)

        elif dir_y > 0:
            self.dir_check = 2
            delay(0.02)
            self.image.clip_draw(self.frame*64, 700, 64, 100, self.x, self.y)

        elif dir_y < 0:
            self.dir_check = -2
            delay(0.02)
            self.image.clip_draw(self.frame*64, 400, 64, 100, self.x, self.y)

        elif dir_x == 0:
            if attack > 0:
                self.image2.clip_draw(self.frame * 64, self.dir_check, 64, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 64, self.dir_check, 64, 100, self.x, self.y)

        elif dir_y == 0:
            if attack > 0:
                self.image2.clip_draw(self.frame * 64, self.dir_check, 64, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 64, self.dir_check, 64, 100, self.x, self.y)




def handle_events():

    global running  # dir은 다이랙션
    global dir_x
    global dir_y
    global attack

    dir_check = 0

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_d:
                dir_x += 1
            elif event.key == SDLK_a:
                dir_x -= 1
            elif event.key == SDLK_w:
                dir_y += 1
            elif event.key == SDLK_s:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_SPACE:
                attack += 1


        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                dir_x -= 1
            elif event.key == SDLK_a:
                dir_x += 1
            elif event.key == SDLK_w:
                dir_y -= 1
            elif event.key == SDLK_s:
                dir_y += 1
            elif event.key == SDLK_SPACE:
                attack -= 1

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


boy = None
grass = None
running = None

# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

    global dir_x
    global dir_y
    global attack

    dir_x = 0
    dir_y = 0
    attack = 0

    zombie_list = [Zombie() for i in range(5)]
    game_world.add_objects(zombie_list, 1)

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


