class InvalidGridException(Exception):
    """
    Raised when the grid is invalid (wrong dimensions, ...)
    """

    def __init__(self, message: str) -> None:
        """
        Parameters
        ----------
        message: str
            String parameter passed to Exception constructor
        """
        super().__init__(message)
        pass
