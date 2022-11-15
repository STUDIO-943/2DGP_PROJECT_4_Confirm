from pico2d import *
import game_framework
import title_state
class Grass:
    def __init__(self):
        self.image = load_image('background2.png')

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
            delay(0.05)
            self.image.clip_draw(self.frame*64, 600, 64, 100, self.x, self.y)

        elif dir_x == -1:
            self.dir_check = -1
            delay(0.05)
            self.image.clip_draw(self.frame*64, 500, 64, 100, self.x, self.y)

        elif dir_y > 0:
            self.dir_check = 2
            delay(0.05)
            self.image.clip_draw(self.frame*64, 700, 64, 100, self.x, self.y)

        elif dir_y < 0:
            self.dir_check = -2
            delay(0.05)
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

# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()
def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


