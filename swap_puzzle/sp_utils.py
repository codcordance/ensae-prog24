"""
Swap puzzle utils module.
"""

from swap_puzzle import *


class SPUtils:

    @staticmethod
    def adjacent(i: int, j: int, k: int, l: int, raiser: bool = False) -> bool:
        """
        Check if two cells are adjacent to each other (on the same line or the same column)

        Parameters
        ----------
        i: int
            First cell line
        j: int
            First cell column
        k: int
            Second cell line
        l: int
            Second cell column
        raiser:
            If True, then if the cells are not adjacent an exception will be raised. Il False, then it returns
            if the cells are adjacent.
        Returns
        -------
        bool
            When raiser is False, equals to True if the cells are adjacent (false otherwise).

        Raises
        ------
        SwapNotAllowedException
            if two cells are not adjacent and raiser is True
        """
        if i == k:
            if l - j not in (1, -1):
                if raiser:
                    raise SwapNotAllowedException("the cells are on the same line but are not one column apart !")
                return False
            return True
        elif j == l:
            if k - i not in (1, -1):
                if raiser:
                    raise SwapNotAllowedException("the cells are on the same column but are not one line apart !")
                return False
            return True
        if raiser:
            raise SwapNotAllowedException("the cells are neither on the same line nor on the same column !")
        return False

    @staticmethod
    def cell_difference(s1: state, s2: state) -> list[cell]:
        """
        Check the cell differences between two states.

        Parameters
        ----------
        s1: state
            The first state
        s2: state
            The second state

        Returns
        -------
        list[cell]
            The list of differences
        """
        diff = []
        for i in range(len(s1)):
            for j in range(len(s1[0])):
                if s1[i][j] != s2[i][j]:
                    diff.append((i, j))
        return diff

    @staticmethod
    def neighbour_states(s1: state, s2: state) -> bool:
        """
        Check if two states are neighbours, i.e. if you can go from one to the other with one permitted swap.

        Parameters
        ----------
        s1: state
            First state
        s2: state
            Second state

        Returns
        -------
        bool
            True if the states are neighbours (false otherwise).
        """
        diff = SPUtils.cell_difference(s1, s2)
        if len(diff) != 2: return False
        for i in diff:
            for j in diff:
                if i != j and SPUtils.adjacent(*i, *j):
                    return True
        return False

    @staticmethod
    def swap_between_states(s1: state, s2: state) -> tuple[cell, cell]:
        """
        Get the swap to go from a state to a neighboor state. The two states must be neighbours.

        Parameters
        ----------
        s1: state
            First state
        s2: state
            Second state

        Returns
        -------
        tuple[cell, cell]
            The swap between the two states.
        """
        diff = SPUtils.cell_difference(s1, s2)
        return diff[0], diff[1]

    @staticmethod
    def permutations(l: list) -> list[list]:
        """
        Recursive function to generate permutations of a given list.

        Parameters
        ----------
        l: list
            List to generate the permutations of

        Returns
        -------
        list[list]
            List of permutations of list l
        """
        if len(l) == 0:
            return [[]]

        p = []
        for i in range(len(l)):
            r = l[:i] + l[i + 1:]
            for perm in SPUtils.permutations(r):
                p.append([l[i]] + perm)
        return p

    @staticmethod
    def dict_possible_states(m: int, n: int) -> dict[str, state]:
        """
        Get a dictionary of the possible states of a grid of m x n. The keys are the states converted to string.

        Parameters
        ----------
         m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid

        Returns
        -------
        dict[str, state]
            Dictionary of the possible states.
        """
        mn = m * n
        states = SPUtils.permutations(list(range(1, mn + 1)))
        states = [[s[i:i + n] for i in range(0, mn, n)] for s in states]
        return {SPUtils.state_to_str(s): s for s in states}

    @staticmethod
    def state_to_str(s: state) -> str:
        """
        Converts a state into a string. The elements on a line are separated by a comma and the lines by a semicolon.
        For instance, the state [[1, 2, 3], [4, 5, 6], [7, 8, 9]] is converted into '1,2,3;4,5,6;7,8,9'

        Parameters
        ----------
        state: state
            State to convert

        Returns
        -------
        str
            Converted state
        """
        return ';'.join(map(lambda i: ','.join(map(str, i)), s))

    @staticmethod
    def str_to_state(s: str) -> state:
        """
        Converts a string into a state. The elements on a line are separated by a comma and the lines by a semicolon.
        For instance, '1,2,3;4,5,6;7,8,9' is converted into [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        Parameters
        ----------
        state: str
            State to convert

        Returns
        -------
        state
            Converted state
        """
        return list(map(lambda i: [int(j) for j in i.split(',')], s.split(';')))
# %%
