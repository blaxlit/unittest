import unittest
from coe_number.alternating_characters import alternating_characters

class AlternatingCharactersTest(unittest.TestCase):
    def test_give_AAAA_should_be_3(self):
        self.assertEqual(alternating_characters("AAAA"), 3) 

    def test_give_ABCDE_should_be_0(self):
        self.assertEqual(alternating_characters("ABCDE"), 0)