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

def draw (bottom):  #에니메이션 시트 삽입, 그리고 프레임 설정, 가로 길이 64픽셀 세로 100픽셀, 8x8 동작

    global x, y
    global dir_x, dir_y
    global anim_frame

    clear_canvas()
    background.draw(400,300)
    char.clip_draw(anim_frame * 64, bottom, 64, 100, x, y)
    update_canvas()

    handle_events()

    anim_frame = (anim_frame + 1) % 8

    x += dir_x * 5
    y += dir_y * 5

    delay(0.03)

open_canvas() #이미지 넣기

background = load_image('background.png')
char = load_image('anim_sheet_3.png')

running = True
x = 800 // 2
y = 300
anim_frame = 0
dir_x = 0
dir_y = 0
dir_check = 0


while running: #방향에 따른 idle 에니메이션 구성
    if dir_check == 1:
        dir_check = 200
    elif dir_check == -1:
        dir_check = 100
    elif dir_check == 2:
        dir_check = 300
    elif dir_check == -2:
        dir_check = 0
        
    if dir_x == 1:
        dir_check = 1
        draw(600)
    elif dir_x == -1:
        dir_check = -1
        draw(500)
    elif dir_y > 0:
        dir_check = 2
        draw(700)
    elif dir_y < 0:
        dir_check = -2
        draw(400)
    elif dir_x == 0:
        draw(dir_check)
    elif dir_y == 0:
        draw(dir_check)

close_canvas()

# while running:
#
#     global bottom
#
#     if dir_check == 1:
#         dir_check = 200
#     elif dir_check == -1:
#         dir_check = 100
#     elif dir_check == 2:
#         dir_check = 300
#     elif dir_check == -2:
#         dir_check = 0
#
#     if dir_x == 1:
#         dir_check = 1
#         bottom = 600
#     elif dir_x == -1:
#         dir_check = -1
#         bottom = 500
#     elif dir_y > 0:
#         dir_check = 2
#         bottom = 700
#     elif dir_y < 0:
#         dir_check = -2
#         bottom = 400
#     elif dir_x == 0:
#         bottom = dir_check
#     elif dir_y == 0:
#         bottom = dir_check














    
