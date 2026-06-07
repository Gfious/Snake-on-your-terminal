import random
from config import WIDTH, HEIGHT

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
    
    def add_rocks(self, walls):
        snake_start = [(5, 5), (4, 5), (3, 5)]
        snake_direction = (1, 0)
        i = 0
        while(i<7):
            x = random.randint(1, WIDTH - 2)
            y = random.randint(1, HEIGHT - 2)
            if (1 < x <= WIDTH - 2) or (1 < y < HEIGHT - 2):
                if(x,y) not in snake_start and (x,y) not in (6,5):
                    walls.tiles.add((x,y))
            i+=1
    
    def add_ruins():
        pass
    
    def add_room(self, walls, x, y, width, height):
        
        for _ in range(50): 
            width >= 5
            height >=5

            width = random.randint(5, 8)
            height = random.randint(5,8)
            
            x = random.randint(2, WIDTH - width - 2)
            y = random.randint(2, HEIGHT - height - 2)

            if not self.can_place_room(walls, x, y, width, height):
                continue

            for rx in range(x, x + width):
                walls.add((rx, y))
                walls.add((rx, y + height - 1))

            for ry in range(y, y + height):
                walls.add((x, ry))
                walls.add((x + height - 1, ry))
            
            
            # select axis to put the door in (vertical or horizontal)
            door1_x = random.randint(x + 2, x + width - 2)
            door2_x = random.randint(y + 2, y + height - 2)

            walls.remove((door1_x, y))
            
            walls.remove((door2_x, y + height - 1))
            return
        
    def can_place_room(self, walls, x, y, width, height):
        snake_start = [(5, 5), (4, 5), (3, 5)]
        snake_direction = (1, 0)
        for rx in range(x - 2, x + width + 2):
            for ry in range(y - 2, y + height + 2):
                if(rx, ry) in walls.tiles:
                    return False
                elif (rx, ry) in snake_start or (rx, ry)  in (6,5):
                    return False
        return True

    def generate(self, walls):
        # TODO:
        # generate walls
        walls.tiles.clear()
        self.add_border(walls)
        self.add_room(walls, 5, 5, 5, 5)
        self.add_rocks( walls)
        
    