import swap_puzzle as sp
import unittest


class Test_Swap(unittest.TestCase):
    def test_naive_solver(self):
        grid = sp.Grid.grid_from_file("input/grid2.in")
        solver = sp.NaiveSolver2(grid)
        solver.get_solution()



if __name__ == '__main__':
    unittest.main()
