from swap_puzzle import *


class BFSSolver(Solver):
    """
    A naive solver, doing swaps of adjacent cases.
    """

    def _work(self, m: int, n: int, state: state, acc: any) -> (list[tuple[cell, cell]], any):
        """
        Parameters
        ----------
        acc:
            Here the accumulator is
        """
        return [], ()

    def __init__(self, callback: Callable[[list[tuple[cell, cell]]], None] = lambda _: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[Coordinates, Coordinates]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("naive", callback=callback)