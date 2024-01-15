import swap_puzzle as sp
import unittest


class Test_Swap(unittest.TestCase):
    def test_grid1(self):
        grid = sp.Grid.grid_from_file("input/grid1.in")
        grid.swap((3, 0), (3, 1))
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [7, 8]])

    def test_grid1_seq(self):
        grid = sp.Grid.grid_from_file("input/grid1.in")
        grid.swap_seq([((3, 0), (3, 1)), ((3, 0), (3, 1))])
        self.assertEqual(grid.state, [[1, 2], [3, 4], [5, 6], [8, 7]])


if __name__ == '__main__':
    unittest.main()
