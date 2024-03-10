from swap_puzzle import *
import unittest


class Test_Swap(unittest.TestCase):
    def test_naive_solver(self):
        g = Grid.grid_from_file("input/grid2.in")
        s = NaiveSolver2(g)
        # s.get_solution()


if __name__ == '__main__':
    unittest.main()
