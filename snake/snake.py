from config import INITIAL_SNAKE_LENGTH

class Snake:

    def __init__(self, start_position=(5, 5)):
        """
        body: list of (x, y)
        direction: current movement vector
        """
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)                                                         # Moving right initially
        self.growth = 0 # number of segments to grow
    def set_direction(self, new_direction):
        """
        Change snake direction
        IMPORTANT: prevent snake from reversing into itself
        """

        self.direction = new_direction

    def move(self):
        # Compute new head from current direction
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Insert new head at front of body
        self.body.insert(0, new_head)
        if(self.growth > 1):
            self.growth -= 1;
        else:
            #pop last segment
            self.body.pop()

    def grow(self):
        """
        Called when snake eats food.
        Usually don't remove tail segment on next move.
        """
        self.growth += 1;
        pass

    def head(self):
        return self.body[0]

    def hits_self(self):
        """
        Return True if head collides with body.
        """
        return self.head() in self.body[1:]
    
    def set_direction(self, new_direction):
        dx, dy = self.direction
        ndx, ndy = new_direction

        # prevent 180 turns
        if (dx, dy) == (-ndx, -ndy):
            return
        
        self.direction = new_direction