from swap_puzzle import *
import unittest


class TestSwap(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        g.swap((3, 0), (3, 1))
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [7, 8]])

    def test_grid1_seq(self):
        g = Grid.grid_from_file("input/grid1.in")
        g.swap_seq([((3, 0), (3, 1)), ((3, 0), (3, 1))])
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])


if __name__ == '__main__':
    unittest.main()
