import random
from config import WIDTH, HEIGHT, RUINS
from collections import deque

"""
Planned Structures:
    Room:
        #####
        #   #
            #
            #
        #   #
        #####
        need to guarantee possible escape (2 or more "squares" for "doorway")

    Ruins:
        #######
           #
           # 

        or

            #
            #
        #########
            #
            #
        any combination of these

    Cave:
        ################
        #              #

        ################
        any sort of tunnel that has an entry and exit without turning back

    Rock:
        #
    
        or

        ##
        ##
        probably should cap the size to width=3 and height=3 so it won't generate rocks too big
"""

class MapGenerator:

    def add_border(self, walls):
        # top and bottom walls
        for x in range(WIDTH):
            walls.tiles.add((x, 0))
            walls.add((x, HEIGHT-1))

        # left and right walls
        for y in range(HEIGHT):
            walls.tiles.add((0, y))
            walls.tiles.add((WIDTH-1, y))
    def generate_rock_pattern(self):
        pattern = []

        for y in range(2):
            row = []
            for x in range(2):
                row.append(random.randint(0, 2))
            pattern.append(row)

        return pattern
    
    def build_rock(self, x, y):
        pattern = self.generate_rock_pattern()

        tiles = set()

        for dy in range(2):
            for dx in range(2):
                if pattern[dy][dx] == 0:
                    continue
                tiles.add((x + dx, y + dy))

        return tiles

    def add_rocks(self, walls):
        for _ in range(10):

            x = random.randint(1, WIDTH - 4)
            y = random.randint(1, HEIGHT - 4)

            tiles = self.build_rock(x, y)

            if not self.can_place_structure(walls, tiles):
                continue

            for t in tiles:
                walls.add(t)

    def rotate(self, tile, direction):
        x, y = tile
        
        if direction == 0:
            return (x, y)
        if direction == 1:
            return (y, -x)
        if direction == 2:
            return (-x, -y)
        if direction == 3:
            return (-y, x)
        
    def build_ruins(self, shape_name, x, y, rotation):
        base = RUINS[shape_name]

        tiles = set()

        for tile in base:
            rx, ry = self.rotate(tile, rotation)
            tiles.add((x + rx, y + ry))

        return tiles
    
    def add_ruins(self, walls):
        for _ in range(5):
            shape = random.choice(list(RUINS.keys()))
            rotation = random.randint(0, 3)

            x = random.randint(2, WIDTH - 6)
            y = random.randint(2, HEIGHT - 6)

            tiles = self.build_ruins(shape, x, y, rotation)

            if not self.can_place_structure(walls, tiles):
                continue

            for t in tiles:
                walls.add(t)

    def get_room_tiles(self, x, y, width, height):
        tiles = set()

        for rx in range(x, x + width):
            tiles.add((rx, y))
            tiles.add((rx, y + height - 1))

        for ry in range(y, y + height):
            tiles.add((x, ry))
            tiles.add((x + width - 1, ry))

        return tiles
        
    def add_room(self, walls):
        
        for _ in range(3):   
            width = random.randint(5, 8)
            height = random.randint(5,8)
            
            x = random.randint(2, WIDTH - width - 2)
            y = random.randint(2, HEIGHT - height - 2)

            tiles = self.get_room_tiles(x, y, width, height)

            if not self.can_place_structure(walls, tiles):
                continue

            for t in tiles:
                walls.add(t)
            
            door1 = (random.randint(x + 1, x + width - 2), y)
            door2 = (random.randint(x + 1, x + width - 2), y + height - 1)

            walls.remove(door1)
            walls.remove(door2)

        return
    
    def can_place_structure(self, walls, tiles):
        for tile in tiles:
            if tile in walls.tiles:
                return False
            #if tile in self.reserved:
            #    return False
        return True
    
    def is_walkable(self, pos, walls):
        return pos not in walls.tiles
    
    def flood_fill(self, start, walls, snake_body = None):
        visited = set()
        queue = deque([start])

        while queue:
            x, y = queue.popleft()

            if (x, y) in visited:
                continue

            if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
                continue

            if(x, y) in walls.tiles:
                continue

            if snake_body and (x, y) in snake_body:
                continue

            visited.add((x, y))

            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))

        return visited
    
    def is_valid_map(self, walls, snake_head, food_pos, snake_body):
        reachable = self.flood_fill(snake_head, walls, snake_body)
        if food_pos is not None:
            return food_pos in reachable and len(reachable) > (WIDTH * HEIGHT * 0.4)

    def generate(self, walls, snake_head, food_pos = None, snake_body = None):
        for _ in range(50):
            # generate walls
            walls.tiles.clear()
            self.add_border(walls)
            self.add_room(walls)
            self.add_ruins(walls)
            self.add_rocks(walls)

            if self.is_valid_map(walls, snake_head, food_pos, snake_body):
                return

        print("Fallback Map")
    