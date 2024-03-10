from swap_puzzle import *


class NaiveSolver(Solver):
    """
    A naive solver, doing swaps of adjacent cases.
    """

    def _work(self, m: int, n: int, state: list[list[int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
        return []

    def __init__(self, callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None] = lambda: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[tuple[int, int], tuple[int, int]]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("naive", callback=callback)
#%%
