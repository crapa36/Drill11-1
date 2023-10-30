import game_framework
from pico2d import open_canvas, delay, close_canvas
import play_mode  as start_mode
import logo_mode 
import title_mode

open_canvas()
game_framework.run(start_mode)


close_canvas()