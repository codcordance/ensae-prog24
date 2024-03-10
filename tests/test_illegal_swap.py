from swap_puzzle import *
import unittest


class TestIllegalSwap(unittest.TestCase):

    def test_invalid_position(self):
        g = Grid.grid_from_file("source/grid1.in")
        with self.assertRaises(InvalidPositionException):
            g.swap((3, 0), (3, -10))

    def test_same_line_too_far(self):
        g = Grid.grid_from_file("source/grid2.in")
        with self.assertRaises(SwapNotAllowedException):
            g.swap((1, 0), (1, 2))

    def test_same_column_too_far(self):
        g = Grid.grid_from_file("source/grid1.in")
        with self.assertRaises(SwapNotAllowedException):
            g.swap((3, 0), (1, 0))

    def test_same_cell(self):
        g = Grid.grid_from_file("source/grid1.in")
        with self.assertRaises(SwapNotAllowedException):
            g.swap((3, 0), (3, 0))

    def test_too_far(self):
        g = Grid.grid_from_file("source/grid1.in")
        with self.assertRaises(SwapNotAllowedException):
            g.swap((0, 0), (3, 1))

    def test_illegal_swap_sequence(self):
        g = Grid.grid_from_file("source/grid1.in")
        with self.assertRaises(SwapNotAllowedException):
            g.swap_seq("test")


if __name__ == '__main__':
    unittest.main()
