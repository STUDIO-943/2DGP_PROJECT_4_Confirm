import pico2d
import Char_move
import logo_state


pico2d.open_canvas()

Char_move.enter()

while Char_move.running:
    Char_move.handle_events()
    Char_move.update()
    Char_move.draw()

Char_move.exit()

pico2d.close_canvas()
