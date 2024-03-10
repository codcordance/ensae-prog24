class SwapNotAllowedException(Exception):
    """
    Raised when the swap is not allowed
    """

    def __init__(self, message: str) -> None:
        """
        Parameters
        ----------
        message: str
            String parameter passed to Exception constructor
        """
        super().__init__(f"The swap is not allowed : {message}")
        pass
