from swap_puzzle import *
import unittest


class TestGridLoading(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])

    def test_grid2(self):
        g = Grid.grid_from_file("input/grid2.in")
        self.assertEqual(g.m, 3)
        self.assertEqual(g.n, 3)
        self.assertEqual(g.state, [[7, 5, 3], [1, 8, 6], [4, 2, 9]])


if __name__ == '__main__':
    unittest.main()
