import random
from config import *
from walls import Walls

class Mouse:
    
    def __init__(self, walls):
        self.spawn(walls)

    def spawn(self, walls):
        while True:
            x = random.randint(1, WIDTH - 2)
            y = random.randint(1, HEIGHT - 2)

            if(x, y) not in walls.tiles:
                self.position = (x, y)
                return
                
    def move(self, walls):
        x, y = self.position
        options = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        random.shuffle(options)

        for nx, ny in options:
            if(nx, ny) not in walls.tiles:
                if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                    self.position = (nx, ny)
                    return