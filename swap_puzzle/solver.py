from grid import Grid


class Solver:
    """
    Abstract solver class
    """

    def __init__(self, grid: Grid):
        self.grid = grid

    def get_solution(self) -> None:
        return None
