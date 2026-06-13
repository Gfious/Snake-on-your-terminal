# Configuration file for the Snake game
WIDTH = 40
HEIGHT = 40

TICK_RATE = 10                                                                          # Moves per second

INITIAL_SNAKE_LENGTH = 3

MAX_ROCK_SIZE = 3

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)


KEY_BINDINGS = {
    "w": UP,
    "W": UP,

    "s": DOWN,
    "S": DOWN,

    "a": LEFT,
    "A": LEFT,

    "d": RIGHT,
    "D": RIGHT,
}

RUINS = {
    "line": [(0, 0), (1, 0), (2, 0), (3, 0)],
    "cross": [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    "T": [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],
    "L": [(0, 0), (0, 1), (0, 2), (1, 2)]
}

RUNNING = "RUNNING"
GAME_OVER = "GAME_OVER"
EXIT = "EXIT"
