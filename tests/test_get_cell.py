from swap_puzzle import *
import unittest


class TestGetCell(unittest.TestCase):

    def test_grid1(self):
        g = Grid.grid_from_file("source/grid1.in")
        self.assertEqual(g.get_cell(0, 0), 1)


if __name__ == '__main__':
    unittest.main()
