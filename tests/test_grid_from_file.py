import swap_puzzle as sp
import unittest


class Test_GridLoading(unittest.TestCase):
    def test_grid1(self):
        g = sp.Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.m, 4)
        self.assertEqual(g.n, 2)
        self.assertEqual(g.state, [[1, 2], [3, 4], [5, 6], [8, 7]])


if __name__ == '__main__':
    unittest.main()
