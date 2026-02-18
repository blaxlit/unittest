import unittest
from coe_number import grid_challenge
from coe_number.caesar_cipher import caesar_cipher

class CaesarCipherTest(unittest.TestCase):
    def test_give_Always_Look_k2_should_be_Cnways_Nqqm(self):
        s = "Always-Look"
        k = 2
        result = caesar_cipher(s, k)
        self.assertEqual(result, "Cnways-Nqqm")
    def test_give_159357l_k2_should_be_159357n(self):
        self.assertEqual(caesar_cipher("159357l", 2), "159357n")
    def test_give_grid_not_sorted_should_be_no(self):
        self.assertEqual(grid_challenge(["cba", "daf", "ghi"]), "NO")