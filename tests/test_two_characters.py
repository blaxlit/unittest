import unittest
from coe_number.two_characters import two_characters

class TwoCharactersTest(unittest.TestCase):
    def test_give_abaacdabd_should_be_4(self):
        self.assertEqual(two_characters("abaacdabd"), 4)