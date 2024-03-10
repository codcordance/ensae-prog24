from swap_puzzle import *


class NaiveSolver(Solver):
    """
    A naive solver, doing swaps of adjacent cases.
    """

    def _work(self, m: int, n: int, state: state, acc: object) -> (list[tuple[cell, cell]], object):
        """
        Parameters
        ----------
        acc:
            Here the accumulator is a list of two elements, the first being the flattened state
            and the second being the custom order
        """
        if acc is None:
            # Most efficient way, only using python generator objects which run in C and are more memory efficient
            # for instance, using reversed(line) instead of line[::-1]
            #
            # this code use two nested for loop (a first for line in state) and a second (for line / reversed line
            # for odd lines) to flatten the state.
            flatten = [c for i, line in enumerate(state) for c in (reversed(line) if i % 2 else line)]

            # order computes the "snake order". For instance, in a 3 by 3 grid, the custom order is
            # 0 < 1 < 2 < 5 < 4 < 3 < 6 < 7 < 8
            order = [i*n + j for i in range(m) for j in (reversed(range(n)) if i%2 else range(n))]
        else:
            flatten, order = acc

        def cell_from_flat(k: int) -> cell:
            """
            Returns a cell coordinates from its index in the flattened state

            Parameters
            ----------
            k: int

            Returns
            -------
            cell
                A cell in the grid
            """
            i, j = k // m, k % m
            j = n - 1 - j if i % 2 else j
            return i, j

        def geq_custom_order(i: int, j: int) -> bool:
            """
            Return if i is greater or equal than j in the custom order

            Parameters
            ----------
            i: int
            j : int

            Returns
            -------
            bool
                True if i >= j in the custom order (false otherwise)
            """
            return order[i-1] >= order[j-1]

        for i in range(m * n - 1):
            if geq_custom_order(flatten[i], flatten[i + 1]):
                flatten[i], flatten[i + 1] = flatten[i + 1], flatten[i]
                return [(cell_from_flat(i), cell_from_flat(i + 1))], (flatten, order)
        return [], ()

    def __init__(self, callback: Callable[[list[tuple[cell, cell]]], None] = lambda _: None) -> None:
        """
        Parameters
        ----------
        callback: Callable[[list[tuple[Coordinates, Coordinates]]], None], optional
            Function called when a swap is operated on the grid. Default does nothing.
        """
        super().__init__("naive", callback=callback)