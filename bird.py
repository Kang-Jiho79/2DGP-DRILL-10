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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * BIRD_FLY_SPEED_PPS * game_framework.frame_time
        if self.x < 0:
            self.x = 0
            self.dir = 1
            self.face_dir = 1
        elif self.x > 1600:
            self.x = 1600
            self.dir = -1
            self.face_dir = -1

    def draw(self):
        if self.face_dir == 1: # right
            self.image.clip_draw(int(self.frame) * 140, 0, 140, 140, self.x, self.y)
        else: # face_dir == -1: # left
            self.image.clip_composite_draw(int(self.frame) * 140, 0, 140, 140, 0, 'h', self.x, self.y, 140, 140)


    def handle_events(self):
        pass