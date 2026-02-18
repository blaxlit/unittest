import unittest
from coe_number.funny_string import funny_string

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_is_funny(self):
        s = "acxz"
        result = funny_string(s)
        self.assertEqual(result, "Funny")

    def test_give_bcxz_is_not_funny(self):
        s = "bcxz"
        result = funny_string(s)
        self.assertEqual(result, "Not Funny")