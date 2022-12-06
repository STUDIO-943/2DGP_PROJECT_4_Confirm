from pico2d import *

import game_framework
import Play_state
import Select_state
import Select_state_3


image = None

def enter():
    # fill here
    global image
    image = load_image('S2.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
                game_framework.change_state(Select_state_3)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.change_state(Select_state)
    pass

def draw():
    clear_canvas()
    image.draw(800,600)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






