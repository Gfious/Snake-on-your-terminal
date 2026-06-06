from snake import Snake
from food import Food
from board import Board
from config import WIDTH, HEIGHT, RUNNING, GAME_OVER, EXIT

class Game:

    def __init__(self):
        self.board = Board(WIDTH, HEIGHT)
        self.snake = Snake()
        self.food = Food()

        self.score = 0
        self.state = RUNNING
        
        self.food.spawn(self.board, self.snake.body)

    def handle_input(self):
        """
        Later:
        - read keyboard input
        - update snake direction
        """

        pass

    def update(self):
        """
        One game tick:
        1. move snake
        2. check collision
        3. check food
        """
        #TODO
        self.snake.move()
        self.check_collisions()
        if self.snake.head() == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.spawn(self.board, self.snake.body)
        

    def check_collisions(self):
        head_x, head_y = self.snake.head()
        # Map limit collision causes death
        if head_x < 0 or head_x >= WIDTH:
            self.game_over()
        if head_y < 0 or head_y >= HEIGHT:
            self.game_over()
        #TODO: self collision
        

    def game_over(self):
        self.state = GAME_OVER

    def render(self):
        """
        For now: just print coordinates.
        Terminal rendering comes later.
        """
        # KEEP SIMPLE AT FIRST
        print("Snake:", self.snake.body)
        print("Food:", self.food.position)
        print("Score:", self.score)
        if self.state == GAME_OVER:
            print("GAME OVER!")
            print("FINAL SCORE: ", self.score)

    def run(self):
        """
        Main loop:
        while running:
            handle_input()
            update()
            render()
            sleep()
        """
        import time

        while self.state != EXIT:
            if self.state == RUNNING:
                self.handle_input()
                self.update()
            
            self.render()
            if self.state == GAME_OVER:
                time.sleep(2)
                self.state = EXIT
            time.sleep(1 / 10)                                                          # Temporary fixed speed
