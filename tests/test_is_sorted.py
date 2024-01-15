import swap_puzzle as sp
import unittest


class Test_IsSorted(unittest.TestCase):
    def test_grid1(self):
        grid = sp.Grid.grid_from_file("input/grid1.in")
        self.assertEqual(grid.is_sorted(), False)
        grid.swap((3, 0), (3, 1))
        self.assertEqual(grid.is_sorted(), True)


if __name__ == '__main__':
    unittest.main()
