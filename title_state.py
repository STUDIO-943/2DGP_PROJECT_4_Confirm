from pico2d import *

import game_framework
import Char_move

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)
image = None

def enter():
    # fill here
    pass

def exit():
    # fill here
    pass

def handle_events():



def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






