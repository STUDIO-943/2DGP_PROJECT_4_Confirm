import pico2d
import game_framework

import logo_state

pico2d.open_canvas(1600,1200)
game_framework.run(logo_state)
pico2d.close_canvas()