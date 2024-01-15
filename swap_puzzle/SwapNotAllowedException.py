class SwapNotAllowedException(Exception):
    """
        Raised when the swap is not allowed
    """
    def __init__(self, message):
        self.message = f"The swap is not allowed : {message}"
