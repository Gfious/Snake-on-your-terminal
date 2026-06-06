import random
from config import WIDTH, HEIGHT
from walls import *

class Food:

    def __init__(self):
        self.position = (0, 0)

    def spawn(self, walls, snake_body):
        """
        Place food in a random location NOT occupied by the snake.
        """
        # 1. generate random position
        # 2. check it's not inside snake_body
        while True:
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)

            if (x, y) not in snake_body and (x, y) not in walls.tiles:
                self.position = (x, y)
                break