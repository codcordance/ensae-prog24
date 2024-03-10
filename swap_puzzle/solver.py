from grid import Grid
from collections.abc import Callable


class Solver:
    """
    Solver class. Helps control the permitted operations on the grid and retrieve the list
    of steps.

    Attributes
    ----------
    max_calls: int, optional
        Maximum number of calls, default is 1000
    callback: Callable[[(int, int), (int, int)], None], optional
        Function called when a swap is operated on the grid. Default does nothing.
    """

    def __init__(self,
                 max_calls: int = 1000,
                 callback: Callable[[(int, int), (int, int)], None] = lambda: None) -> None:
        """
        Constructor. Initializes the solver.

        Parameters
        ----------
        max_calls: int, optional
            Maximum number of calls, default is 1000
        callback: Callable[[(int, int), (int, int)], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        self.max_calls: int = max_calls
        self.callback: Callable[[(int, int), (int, int)], None] = callback

    def _work(self, m: int, n: int, state: list[list[int]]) -> list[((int, int), (int, int))]:
        """


        Parameters
        ----------
        m
        n
        state

        Returns
        -------
        list[((int, int), (int, int))]

        """
        pass

    def get_solution(self, grid: Grid) -> None:
        return None
