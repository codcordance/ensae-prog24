class InvalidPositionException(Exception):
    """
    Raised when a position is invalid
    """

    def __init__(self, position: str) -> None:
        """
        Parameters
        ----------
        position: str
            Representation of the invalid position
        """
        super().__init__(f"The position {position} is invalid in the grid !")
        pass
