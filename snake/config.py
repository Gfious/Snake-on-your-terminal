# Configuration file for the Snake game

WIDTH = 20
HEIGHT = 20

TICK_RATE = 10                                                                          # Moves per second

INITIAL_SNAKE_LENGTH = 3


UP = (0, -1),
DOWN = (0, 1),
RIGHT = (1, 0),
LEFT = (-1, 0),


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


RUNNING = "RUNNING"
GAME_OVER = "GAME_OVER"
EXIT = "EXIT"
