import random
from config import *


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

    def has_line_of_sight(self, target, walls):
        x0, y0 = self.position
        x1, y1 = target

        dx = x1 - x0
        dy = y1 - y0

        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return True
        
        for i in range(1, steps):
            x = x0 + round(dx * i / steps)
            y = y0 + round(dy * i / steps)

            if(x, y) in walls.tiles:
                return False
        return True
    
    def can_see_snake(self, snake_head, walls):
        mx, my = self.position
        sx, sy = snake_head

        dist = abs(mx - sx) + abs(my - sy)

        if dist > VISION_RANGE:
            return False
        
        return self.has_line_of_sight(snake_head, walls)
    

    def move(self, walls, snake_head, food_pos):
        x, y = self.position
        snake_visible = self.can_see_snake(snake_head, walls)

        best_score = float("-inf")
        best_pos = self.position

        options = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        random.shuffle(options)

        for nx, ny in options:
            if not (0 <= nx < WIDTH and 0 <= ny < HEIGHT):
                continue
            if(nx, ny) in walls.tiles:
                continue
        
            food_dist = abs(nx - food_pos[0]) + abs(ny - food_pos[1])
            score = -food_dist

            if snake_visible:
                snake_dist = abs(nx - snake_head[0]) + abs(ny - snake_head[1])
                score += snake_dist * 3

            if score > best_score:
                best_score = score
                best_pos = (nx, ny)

        self.position = best_pos