"""
Swap puzzle utils module.
"""

from swap_puzzle import *


class SPUtils:
    def state_to_str(state: state) -> str:
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
        return ';'.join(map(lambda i: ','.join(map(str, i)), state))

    def str_to_state(state: str) -> state:
        """
        Converts a state into a string. The elements on a line are separated by a comma and the lines by a semicolon.
        For instance, the state is converted into [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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
