class Walls:
    def __init__(self):
        self.tiles = set()

    def is_wall(self, pos):
        return pos in self.tiles
    
    def add_wall(self, pos):
        self.tiles.add(pos)
    
    def remove_wall(self, pos):
        self.tiles.discard(pos)

    def generate_border(self, width, height):
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