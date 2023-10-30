import game_framework
from pico2d import *
import play_mode, game_world
from pannel import Pannel
import boy
def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel,3)
def finish():
    game_world.remove_object(pannel)
def update():
    game_world.update
    
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()
    
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()            
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_mode()
                case pico2d.SDLK_SPACE:
                    game_framework.change_mode(play_mode)
                case pico2d.SDLK_0:
                    play_mode.boy.item = None
                    game_framework.pop_mode()
                case pico2d.SDLK_1:
                    play_mode.boy.item = 'Ball'
                    game_framework.pop_mode()
                case pico2d.SDLK_2:
                    play_mode.boy.item = 'BigBall'
                    game_framework.pop_mode()
                    
                    
                
