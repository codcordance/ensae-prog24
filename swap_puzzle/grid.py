"""
This is the grid module. It contains the Grid class and its associated methods.
"""

from swap_puzzle import *


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
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the
        i-th line and j-th column.
        Note: lines are numbered from 0 to m and columns are numbered from 0 to n.
    """

    # changed initial_state=[] to =None to avoid mutable default argument
    def __init__(self, m: int, n: int, initial_state: list[list[int]] = None) -> None:
        """
        Initializes the grid.

        Parameters:
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]], optional
            The initial state of the grid. Default is empty (then the grid is created sorted).

        Raises
        ------
        InvalidGridException
            Raised if the given dimensions are invalid
        """

        if not (isinstance(m, int) and isinstance(n, int) and m >= 1 and n >= 1):
            raise InvalidGridException("Wrong dimensions")

        self.m: int = m
        self.n: int = n
        if not initial_state:
            # changed list(range(...)) to use the argument unpacking operator *range
            initial_state = [[*range(i * n + 1, (i + 1) * n + 1)] for i in range(m)]
        self.state: list[list[int]] = initial_state

    def __str__(self):
        """
        Prints the state of the grid as text.
        """
        output: str = f"The grid is in the following state:\n"
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

        Returns
        -------
        bool
            True if the grid is sorted (false otherwise)
        """
        # changed ==list(range) to use the argument unpacking operator *range
        return sum(self.state, []) == [*range(1, self.m * self.n + 1)]

    def is_coord_2tuple(self, obj: object) -> bool:
        """
        Check if an object is a 2-tuple representing (the coordinates of) a cell in the grid.

        Parameters
        ----------
            obj:
                Object to check

        Returns
        -------
        bool
            True if the object is a 2-tuple (i, j) with 0 <= i < m and 0 <= j < n (false otherwise)
        """
        return (isinstance(obj, tuple) and len(obj) == 2
                and obj[0] in range(self.m) and obj[1] in range(self.n))

    def swap(self, cell1: (int, int), cell2: (int, int)) -> None:
        """
        Swap (the values of) two cells.

        Raises an exception if the swap is not allowed. The cells must be in the format (i, j)
        where i is the line and j the column number of the cell and be adjacent.

        Parameters
        ----------
            cell1: (int, int)
                First cell to swap
            cell2: (int, int)
                Second cell to swap

        Raises
        ------
        InvalidPositionException
            If one of the given parameters corresponds to an invalid cell coordinates
        SwapNotAllowedException
            Raised if the swap is not allowed.
        """
        if not self.is_coord_2tuple(cell1):
            raise InvalidPositionException(f"{cell1}")

        if not self.is_coord_2tuple(cell2):
            raise InvalidPositionException(f"{cell2}")

        if cell1 == cell2:
            raise SwapNotAllowedException("The two given cells are identical, something is probably going wrong...")

        i, j, k, l = cell1 + cell2

        if i == k:
            if l - j not in (1, -1):
                raise SwapNotAllowedException("the cells are on the same line but are not one column apart !")
        elif k == l:
            if k - i not in (1, -1):
                raise SwapNotAllowedException("the cells are on the same column but are not one line apart !")
        else:
            raise SwapNotAllowedException("the cells are neither on the same line nor on the same column !")
        self.state[i][j], self.state[k][l] = self.state[k][l], self.state[i][j]

    def swap_seq(self, cell_pair_list: list[tuple[tuple[int, int], tuple[int, int]]]) -> None:
        """
        Executes a sequence of swaps.

        Parameters
        ----------
        cell_pair_list: list[tuple[tuple[int, int], tuple[int, int]]]
            The list of swaps, each swap being a tuple of two cells (each
            cell being a tuple of integers).

        Raises
        ------
        InvalidPositionException
            Raised by the swap method. If one of the given parameters corresponds to an invalid cell coordinates.
        SwapNotAllowedException
            Raised if the given list of swaps is not a valid list of 2-tuples, or if a swap is not allowed.
        """
        if not isinstance(cell_pair_list, list):
            raise SwapNotAllowedException("The given \"list of swaps\" is not a list !")
        for e in cell_pair_list:
            if not (isinstance(e, tuple) and len(e) == 2):
                raise SwapNotAllowedException("An element of the given \"list of swaps\" is not a 2-tuple !")

            self.swap(*e)

    def get_cell(self, i: int, j: int) -> int:
        """
        Get the value in the cell (i, j)

        Parameters
        ----------
        i: int
            First coordinate of the cell
        j: int
            Second coordinate of the cell

        Returns
        -------
            Value of the given cell

        Raises
        ------
        InvalidPositionException
            Raised if the given cell is invalid
        """
        t: (int, int) = (i, j)
        if not self.is_coord_2tuple(t):
            raise InvalidPositionException(f"{(i, j)}")
        return self.state[i][j]

    @classmethod
    def grid_from_file(cls, file_name):
        """
        Creates a grid object initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid loaded from the file
        """
        if not os.path.exists(file_name):
            raise InvalidGridException(f"the file {file_name} does not exists !")
        with open(file_name, "r") as file:
            try:
                m, n = map(int, file.readline().split())
            except Exception as _:
                raise InvalidGridException("Can't load grid from file due to incorrect format !")
            initial_state = [[] for _ in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n:
                    raise InvalidGridException("Can't load grid from file due to incorrect format !")
                initial_state[i_line] = line_state
            g = Grid(m, n, initial_state)
        return g
