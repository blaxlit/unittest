import unittest
from coe_number.grid_challenge import grid_challenge

class GridChallengeTest(unittest.TestCase):
    def test_give_grid_should_be_yes(self):
        grid = ["eabcd", "fghij", "olkmn", "trpqs", "xywuv"]
        result = grid_challenge(grid)
        self.assertEqual(result, "YES")

    def test_give_grid_not_sorted_should_be_no(self):
        grid = ["mpxz", "abcd", "wlmf"] 
        result = grid_challenge(grid)
        self.assertEqual(result, "NO")