from pico2d import *

import game_world


class Ball:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        self.x, self.y, self.velocity = x, y, velocity
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.x += self.velocity
        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)