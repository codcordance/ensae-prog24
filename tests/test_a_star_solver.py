from swap_puzzle import *
import unittest


class TestAStarSolver(unittest.TestCase):

    def test_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        AStarSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        AStarSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid2(self):
        g = Grid.grid_from_file("input/grid2.in")
        AStarSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)

    def test_grid5(self):
        g = Grid.grid_from_file("input/grid5.in")
        AStarSolver().solve(g, None)
        self.assertEqual(g.is_sorted(), True)


if __name__ == '__main__':
    unittest.main()
