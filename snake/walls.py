import random
from config import WIDTH, HEIGHT

class Walls:
    def __init__(self):
        self.tiles = set()

    def is_wall(self, pos):
        return pos in self.tiles
    
    def add(self, pos):
        self.tiles.add(pos)
    
    def remove(self, pos):
        self.tiles.discard(pos)
