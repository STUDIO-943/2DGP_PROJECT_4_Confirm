from pico2d import *

def handle_events():
    global running # dir은 다이랙션 
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

def draw (bottom): 

    global x, y
    global dir_x, dir_y
    global anim_frame

    clear_canvas()
    background.draw(1600,900)
    char.clip_draw(anim_frame * 64, bottom, 64, 64, x, y)
    update_canvas()

    handle_events()

    anim_frame = (anim_frame + 1) % 8

    x += dir_x * 5
    y += dir_y * 5

    delay(0.05)

open_canvas()
background = load_image('background.png')
char = load_image('anim_sheet_1.png')

running = True
x = 800 // 2
y = 90
anim_frame = 0
dir_x = 0
dir_y = 0
dir_check = 0


while running:
    if dir_check == 1:
        dir_check = 300
    elif dir_check == -1:
        dir_check = 200
        
    if dir_x == 1:
        dir_check = 1
        draw(100)
    elif dir_x == -1:
        dir_check = -1
        draw(0)
    elif dir_y != 0:
        draw(dir_check)
    elif dir_x == 0:
        draw(dir_check)
    elif dir_y == 0:
        draw(dir_check)

close_canvas()
















    
