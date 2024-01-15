"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import swap_puzzle as sp


class Grid:
    """
        A class representing the grid from the swap puzzle. It supports rectangular grids.

        Attributes:
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        state: list[list[int]]
            The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column.
            Note: lines are numbered 0..m and columns are numbered 0..n.
        """

    def __init__(self, m: int, n: int, initial_state=[]):
        """
        Initializes a grid.

        Args:
            m: the number of lines in the grid
            n: the number of columns in the grid
            initial_state: The initial state of the grid. Default is empty (then the grid is created sorted).
        """
        if not (isinstance(m, int) and isinstance(n, int) and m >= 1 and n >= 1):
            raise sp.InvalidGridException("Wrong dimensions")

        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i * n + 1, (i + 1) * n + 1)) for i in range(m)]
        self.state = initial_state

    def __str__(self):
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m):
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self):
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self) -> bool:
        """
        Checks is the current state of the grid is sorted and returns the answer as a boolean.

        Returns:
            True if the grid is sorted
        """
        return sum(self.state, []) == list(range(1, self.m * self.n + 1))

    def is_coord_2tuple(self, obj) -> bool:
        """
        Check if an object is a 2-tuple representing the coordinate of a cell in the grid.

        Args:
            obj: the object to check

        Returns:
            True if the object is a 2-tuple (i, j) with 0 <= i < m and 0 <= j < n
        """
        return (isinstance(obj, tuple) and len(obj) == 2
                and obj[0] in range(self.m) and obj[1] in range(self.n))

    def swap(self, cell1: (int, int), cell2: (int, int)) -> None:
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.
        The cells must be in the format (i, j) where i is the line and j the column number of the cell.

        Args:
            cell1: the first cell to swap
            cell2: the second cell to swap

        Returns:
            None
        """
        if not (self.is_coord_2tuple(cell1)):
            raise sp.SwapNotAllowedException(f"Invalid cell {cell1}")
        if not (self.is_coord_2tuple(cell2)):
            raise sp.SwapNotAllowedException(f"Invalid cell {cell2}")

        i, j, k, l = cell1 + cell2
        self.state[i][j], self.state[k][l] = self.state[k][l], self.state[i][j]

    def swap_seq(self, cell_pair_list: list) -> None:
        """
        Executes a sequence of swaps.

        Args:
            cell_pair_list: The list of swaps, each swap being
            a tuple of two cells (each cell being a tuple of integers).

        Returns:
            None
        """
        if not (isinstance(cell_pair_list, list)):
            raise ValueError("The given cell_pair_list is not a list !")
        for e in cell_pair_list:
            if not (isinstance(e, tuple) and len(e) == 2):
                raise ValueError("An element of cell_pair_list is not a 2-tuple !")

            self.swap(*e)

    @classmethod
    def grid_from_file(cls, file_name):
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n:
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
