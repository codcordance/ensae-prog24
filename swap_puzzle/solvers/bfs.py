from swap_puzzle import *


class BFSSolver(Solver):
    """
    A naive solver, doing swaps of adjacent cases.
    """

    def _work(self, m: int, n: int, state: state, acc: object) -> (list[tuple[cell, cell]], object):
        """
        Parameters
        ----------
        acc:
            Here the solver give all the swaps in one call to _work, so the accumulator is not used.
        """
        d = SPUtils.dict_possible_states(m, n)
        src, dst = state, next(iter(d.values()))
        g = Graph(d.keys())

        # TODO: add edges

        swaps = [SPUtils.get_swap_between_states(d[e[0]], d[e[1]]) for e in g.bfs(src, dst)]
        return swaps, None

    def __init__(self, callback: Callable[[list[tuple[cell, cell]]], None] = lambda _: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[Coordinates, Coordinates]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("naive", callback=callback)
#%%
