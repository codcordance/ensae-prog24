class InvalidGridException(Exception):
    """
        Raised when the grid is invalid (wrong dimensions, ...)
    """
    def __init__(self, message):
        self.message = message