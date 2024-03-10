from swap_puzzle import *
import unittest


class TestInvalidGridLoading(unittest.TestCase):
    def test_no_file(self):
        with self.assertRaises(InvalidGridException):
            Grid.grid_from_file("input/thisfiledoesnotexists.in")

    def test_invalid_file(self):
        with self.assertRaises(InvalidGridException):
            Grid.grid_from_file("input/invalid.in")



if __name__ == '__main__':
    unittest.main()
