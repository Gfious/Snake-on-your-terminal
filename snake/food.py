import random

class Food:

    def __init__(self):
        self.position = (0, 0)

    def spawn(self, board, snake_body):
        """
        Place food in a random location NOT occupied by the snake.
        """

        # TODO:
        # 1. generate random position
        # 2. check it's not inside snake_body
        while True:
            x = random.randint(0, board.width - 1)
            y = random.randint(0, board.height - 1)

            if (x, y) not in snake_body:
                self.position = (x, y)
                break