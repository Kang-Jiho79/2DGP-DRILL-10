from pico2d import *
import game_world
import game_framework
import random

PIXEL_PER_METER = (140.0 / 0.18) # 140 pixel 18 cm
BIRD_FLY_SPEED_KMPH = 38.0 # Km / Hour
BIRD_FLY_SPEED_MPM = (BIRD_FLY_SPEED_KMPH * 1000.0 / 60.0)
BIRD_FLY_SPEED_MPS = (BIRD_FLY_SPEED_MPM / 60.0)
BIRD_FLY_SPEED_PPS = (BIRD_FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 10.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None
    def __init__(self):
        self.x = random.randint(0, 1600)
        self.y = random.randint(300, 600)
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

    def update(self):
        pass

    def draw(self):
        pass

    def handle_events(self):
        pass