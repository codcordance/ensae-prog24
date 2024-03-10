from swap_puzzle import *


class Solver(ABC):
    """
    Abstract solver class. Helps control the permitted operations on the grid and retrieve the list
    of steps.

    Attributes
    ----------
    name: str
        Name of the solver implementation
    max_swaps: int, optional
        Maximum number of swaps, default is 1000
    callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None], optional
        Function called when a swap is operated on the grid. Default does nothing.
    """

    def __init__(self, name: str,
                 max_swaps: int = 1000,
                 callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None] = lambda: None) -> None:
        """
        Constructor. Initializes the solver.

        Parameters
        ----------
        name: str
            Name of the solver implementation
        max_swaps: int, optional
            Maximum number of swaps, default is 1000
        callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None], optional
            Function called when a sequence of swap is operated on the grid. Default does nothing.
        """
        self.name: str = name
        self.max_swaps: int = max_swaps
        self.callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None] = callback

    @abstractmethod
    def _work(self, m: int, n: int, state: list[list[int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        """
        Function to be implemented in the solver. Take the information of a grid (not the grid object itself)
        and returns a list of 2-tuple of coordinates representing the swaps to be made on the grid.


        Parameters
        ----------
        m: int
        Number of lines in the grid
        n: int
            Number of columns in the grid
        state: list[list[int]]
            The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the
            i-th line and j-th column.

        Returns
        -------
        list[tuple[tuple[int, int], tuple[int, int]]]
            List of 2-tuple of coordinates representing the swaps to be made on the grid.
        """
        pass

    def solve(self, g: Grid) -> (int, list[tuple[tuple[int, int], tuple[int, int]]]):
        """
        Solve a grid. Call the callback on each swap.

        Parameters
        ----------
        g: Grid
            Grid to be solved.

        Returns
        -------
        int
            Number of swaps made on the grid in order to solve it.
        list[tuple[tuple[int, int], tuple[int, int]]]
            List of the swap operated on the grid in order to solve it.

        Raises
        ------
        SolverWorkException
            Raised if the solver did not successfully solve the puzzle (too many swaps, invalid swap,...)
        """
        swaps: list[tuple[tuple[int, int], tuple[int, int]]] = []
        n: int = 0
        while True:
            if n > self.max_swaps:
                raise SolverWorkException(self.name, f"Maximum number of swaps ({self.max_swaps}) exceeded !")

            if g.is_sorted():
                return n, swaps

            try:
                call_swaps = self._work(g.m, g.n, g.state)
                i = len(call_swaps)
                if i < 1:
                    raise SolverWorkException(self.name, f"Solver did not provide any swap, but the grid is not sorted !")
                try:
                    g.swap_seq(call_swaps)
                    swaps.extend(call_swaps)
                    self.callback(call_swaps)
                    n += i
                except SwapNotAllowedException | InvalidPositionException as e:
                    raise SolverWorkException(self.name, e)
            except SolverWorkException as e:
                raise e
            except Exception as e:
                raise SolverWorkException(self.name, e)