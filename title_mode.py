import game_framework
from pico2d import load_image, delay, clear_canvas, update_canvas, get_events, get_time,SDL_KEYDOWN,SDLK_ESCAPE,SDLK_SPACE
import play_mode
def init():
    global image
    
    image = load_image('title.png')
    logo_start_time = get_time()
def finish():
    global image
    del image
def update():
    pass
def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
