class AStarNoPathException(Exception):
    """
    Raised when the A* Algorithm failed due to no path existing between the node
    """

    def __init__(self, src, dst) -> None:
        """
        Parameters
        ----------
        src
            Start node
        end
            End node
        """
        super().__init__(f"No path found between {src} and {dst} !")
        pass
