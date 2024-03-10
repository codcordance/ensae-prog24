from grid import Grid
from solver import Solver


class NaiveSolver(Solver):
    """
    A naive solver, doing swaps of adjacent cases.
    """

    def __init__(self, grid: Grid):
        super().__init__(grid)
        self.m = self.grid.m # light syntax
        self.n = self.grid.n # light syntax

    def get_solution(self) -> None:
        mn = self.m * self.n
        while not self.grid.is_sorted():
            for i in range(mn-1):
                cell_i, cell_ii = self.snake(i), self.snake(i + 1)
                if self.grid.get_cell(*cell_i) > self.grid.get_cell(*cell_ii):
                    self.grid.swap(cell_i, cell_ii)
                    print("swapped!", self.grid.is_sorted(), self.grid)
                    break

    def snake(self, p: int) -> (int, int):
        """
        Return the coordinates of the p-th case if we iterate the case
        in a "snake" way. For instance on a 3x3 grid, the cases would be :

        1 2 3
        6 5 4
        7 8 9

        Args:
            p: an integer for the p-th case

        Returns:
            The p-th case (i, j) coordinates
        """
        i, j = p // self.m, p % self.m
        j = self.n - 1 - j if i % 2 else j
        return i, j

    # def _insertion_sort(self, l: list) -> list:
    #     arr = list(l)
    #     length = len(arr)
    #     for i in range(1, length):
    #         curr = i
    #         while curr > 0 and arr[curr] < arr[curr - 1]:
    #             arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
    #             curr -= 1
    #
    #     return arr
    #
    #
    # def _grid_to_arr(self, g: Grid) -> list[int]:
    #     """
    #     Returns a flattened grid with correct junctions between lines
    #     [[1,2,3],[4,5,6]] -> [1,2,3,6,5,4]
    #     """
    #     grid = list(g.state)
    #
    #     for i in range(g.m):
    #         if i % 2 == 1: self._reverse_arr(grid[i])
    #
    #     flat_grid = sum(grid, [])
    #     return flat_grid
    #
    #
    #
    # def _reverse_arr(self, arr: list):
    #     """
    #     Reverses the elements of a list, modifies the list directly.
    #     """
    #     length = len(arr)
    #     for i in range(length // 2):
    #         arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]
