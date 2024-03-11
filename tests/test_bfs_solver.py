from swap_puzzle import *
import unittest


class TestBFSSolver(unittest.TestCase):

    def test_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        BFSSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid5(self):
        g = Grid.grid_from_file("input/grid5.in")
        BFSSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)


if __name__ == '__main__':
    unittest.main()
