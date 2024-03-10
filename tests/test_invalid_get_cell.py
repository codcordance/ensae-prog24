from swap_puzzle import *
import unittest


class TestGetCell(unittest.TestCase):

    def test_invalid_position(self):
        g = Grid.grid_from_file("input/grid1.in")
        with self.assertRaises(InvalidPositionException):
            g.get_cell(10, 12)


if __name__ == '__main__':
    unittest.main()
