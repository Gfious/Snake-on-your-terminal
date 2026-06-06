

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_inside(self, position):
        """
        Returns True if (x, y) is inside the board boundaries.
        """

        x, y = position

        # TODO: implement boundary check
        pass

    def wrap_position(self, position):
        """
        OPTIONAL
        If snake goes out of bounds, wrap around.
        """
        pass