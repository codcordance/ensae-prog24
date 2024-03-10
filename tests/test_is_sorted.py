from swap_puzzle import *
import unittest


class TestIsSorted(unittest.TestCase):
    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        self.assertEqual(g.is_sorted(), False)
        g.swap((3, 0), (3, 1))
        self.assertEqual(g.is_sorted(), True)


if __name__ == '__main__':
    unittest.main()
