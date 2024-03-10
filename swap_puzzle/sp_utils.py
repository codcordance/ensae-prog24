"""
Swap puzzle utils module.
"""

from swap_puzzle import *


class SPUtils:
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
        mn = m * n
        states = SPUtils.permutations(list(range(1, n * m + 1)))
        states = [[s[i:i + n] for i in range(0, m * n, n)] for s in states]
        return {SPUtils.state_to_str(s): s for s in states}

    @staticmethod
    def get_swap_between_states(s1: state, s2: state) -> tuple[cell, cell]:
        m, n = len(s1), len(s1[0])
        diff = []
        for i in range(len(s1)):
            for j in range(len(s1[0])):
                if s1[i][j] != s2[i][j]:
                    diff.append((i, j))
        return diff[0], diff[1]

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
