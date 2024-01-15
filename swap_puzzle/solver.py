from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """

    def __init__(self, grid: Grid):
        self.grid = grid
        self.solution = []
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        flat_grid = self._grid_to_arr(self.grid)

        self._insertion_sort(flat_grid)
        return self.solution
    
    def _insertion_sort(self, l:list) -> list:
        arr = list(l)
        length = len(arr)
        for i in range(1, length):
            curr = i
            while curr > 0 and arr[curr] < arr[curr - 1]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
                curr -= 1
            
        return arr
    
    def _grid_to_arr(self, g:Grid) -> list[int]:
        """
        Returns a flattened grid with correct junctions between lines
        [[1,2,3],[4,5,6]] -> [1,2,3,6,5,4]
        """
        grid = list(g.state)

        for i in range(g.m):
            if i % 2 == 1: self._reverse_arr(grid[i])

        flat_grid = sum(grid, [])
        return flat_grid

    # TODO: put inside an utils module
    def _reverse_arr(self, arr:list):
        """
        Reverses the elements of a list, modifies the list directly.
        """
        length = len(arr)
        for i in range(length // 2):
            arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]

