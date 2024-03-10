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
            Here the solver compute all the swaps in the first call to _work,
            then pass it each step through the accumulator.
        """
        if acc is None:
            d = SPUtils.dict_possible_states(m, n)
            src, dst = SPUtils.state_to_str(state), SPUtils.state_to_str(next(iter(d.values())))
            g = Graph(d.keys())

            i = 0
            for k in d.keys():
                for l in d.keys():
                    if k != l and SPUtils.neighbour_states(d[k], d[l]):
                        g.add_edge(k, l)
                i += 1
            path = g.bfs(src, dst)
            swaps = []
            for i in range(len(path) - 1):
                swaps.append(SPUtils.swap_between_states(d[path[i]], d[path[i + 1]]))
            return swaps[0:1], swaps[1:]
        else:
            return acc[0:1], acc[1:]

    def __init__(self, callback: Callable[[list[tuple[cell, cell]]], None] = lambda _: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[Coordinates, Coordinates]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("BFS", callback=callback)
