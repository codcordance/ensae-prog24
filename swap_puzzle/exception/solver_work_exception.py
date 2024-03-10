class SolverWorkException(Exception):
    """
    Raised when a solver did not successfully solve the puzzle.
    """

    def __init__(self, solver: str, message: str) -> None:
        """
        Parameters
        ----------
        solver: str
            Solver name
        message: str
            String parameter passed to Exception constructor
        """
        super().__init__(f"Solver {solver} failed : {message}")
        pass
