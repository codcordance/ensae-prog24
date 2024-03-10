from swap_puzzle import *
import unittest


class TestSwap(unittest.TestCase):
    def test_naive_solver(self):
        g = Grid.grid_from_file("input/grid2.in")
        NaiveSolver().solve(g)
        # s.get_solution()


if __name__ == '__main__':
    unittest.main()
