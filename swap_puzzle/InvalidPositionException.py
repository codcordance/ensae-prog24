class InvalidPositionException(Exception):
    """
        Raised when a position is invalid
    """
    def __init__(self, message):
        self.message = f"Invalid position : {message}"
