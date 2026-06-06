

class Snake:

    def __init__(self, start_position=(5, 5)):
        """
        body: list of (x, y)
        direction: current movement vector
        """
        self.body = [start_position]
        self.direction = (1, 0)                                                         # Moving right initially

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
        #pop last segment
        self.body.pop()

    def grow(self):
        """
        Called when snake eats food.
        Usually don't remove tail segment on next move.
        """

        # TODO
        pass

    def head(self):
        return self.body[0]

    def hits_self(self):
        """
        Return True if head collides with body.
        """

        # TODO
        pass