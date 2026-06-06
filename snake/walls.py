import random
from config import WIDTH, HEIGHT

class Walls:
    def __init__(self):
        self.tiles = set()

    def is_wall(self, pos):
        return pos in self.tiles
    
    def add_wall(self, pos):
        self.tiles.add(pos)
    
    def remove_wall(self, pos):
        self.tiles.discard(pos)

    def generate(self, width, height):
        # TODO:
        # generate walls
        self.tiles.clear()

        # top and bottom walls
        for x in range(width):
            self.tiles.add((x, 0))
            self.tiles.add((x, height-1))

        # left and right walls
        for y in range(height):
            self.tiles.add((0, y))
            self.tiles.add((width-1, y))

        i = 0
        while(i<10):
            x = random.randint(0, WIDTH - 1)
            y = random.randint(0, HEIGHT - 1)
            if (x != 0 or x != width-1) and (y != 0 or y != height-1):
                if(x,y) not in [(5, 5), (4, 5), (3, 5)]:
                    self.tiles.add((x,y))
            i+=1
            