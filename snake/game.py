from snake import Snake
from food import Food
from board import Board
from config import WIDTH, HEIGHT, RUNNING, GAME_OVER, EXIT
from input_handler import get_direction
from walls import *
from mapgenerator import *


class Game:

    def __init__(self):
        self.board = Board(WIDTH, HEIGHT)
        self.snake = Snake()
        self.food = Food()
        self.walls = Walls()
        self.generator = MapGenerator()
        self.generator.generate(self.walls)

        self.score = 0
        self.state = RUNNING
        
        self.food.spawn(self.walls, self.snake.body)

    def handle_input(self):
        """
        Later:
        - read keyboard input
        - update snake direction
        """
        direction = get_direction()

        if direction is not None:
            self.snake.set_direction(direction)
        

    def update(self):
        """
        One game tick:
        1. move snake
        2. check collision
        3. check food
        """
        self.snake.move()
        self.check_collisions()
        if self.snake.head() == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food.spawn(self.walls, self.snake.body)
        

    def check_collisions(self):
        head_x, head_y = self.snake.head()
        # wall collision causes death
        if self.walls.is_wall(self.snake.head()):
            self.game_over()

        if self.snake.hits_self():
            self.game_over()


    def game_over(self):
        self.state = GAME_OVER
    
    def render(self):
        
        # clear screen
        print("\033[H\033[J", end="")
        
        grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
        
        # draw food
        fx, fy = self.food.position
        grid[fy][fx] = "*"

        # draw snake
        for i, (x, y) in enumerate(self.snake.body):
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                grid[y][x] = "@" if i == 0 else "o"

        for (x, y) in self.walls.tiles:
            grid[y][x] = "#"

        for row in grid:
            print("".join(row))

        # UI Info
        print(f"Score: {self.score}")

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
