import pico2d
import Play_state

pico2d.open_canvas()

Play_state.enter()

while Play_state.running:
    Play_state.handle_events()
    Play_state.update()
    Play_state.draw()

Play_state.exit()

pico2d.close_canvas()
