from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    global x, y
    global dir_x, dir_y
    global anim_frame
    global bottom



    def update(self):
        self.anim_frame = (self.anim_frame + 1) % 8
        x += dir_x * 5
        y += dir_y * 5

    def draw(self):
        self.image.clip_draw(self.anim_frame*64, 0, bottom, 64, x, y)


def handle_events():
    global running  # dir은 다이랙션
    global dir_x
    global dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
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
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_d:
                dir_x -= 1
            elif event.key == SDLK_a:
                dir_x += 1
            elif event.key == SDLK_w:
                dir_y -= 1
            elif event.key == SDLK_s:
                dir_y += 1

open_canvas()


boy = Boy()
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    boy.update()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()

