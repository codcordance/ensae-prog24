from swap_puzzle import *
import unittest


class TestNaiveSolver(unittest.TestCase):

    def test_grid0(self):
        g = Grid.grid_from_file("input/grid1.in")
        NaiveSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        NaiveSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid2(self):
        g = Grid.grid_from_file("input/grid2.in")
        NaiveSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid3(self):
        g = Grid.grid_from_file("input/grid3.in")
        NaiveSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid4(self):
        g = Grid.grid_from_file("input/grid4.in")
        NaiveSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)


if __name__ == '__main__':
    unittest.main()
