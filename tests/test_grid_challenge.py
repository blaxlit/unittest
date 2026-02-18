import unittest
from coe_number.grid_challenge import grid_challenge

class GridChallengeTest(unittest.TestCase):
    def test_give_grid_should_be_yes(self):
        self.assertEqual(grid_challenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")