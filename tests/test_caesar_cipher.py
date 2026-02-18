import unittest
from coe_number.caesar_cipher import caesar_cipher

class CaesarCipherTest(unittest.TestCase):
    def test_give_Always_Look_k2_should_be_Cnycau_Nqqm(self):
        s, k = "Always-Look", 2
        result = caesar_cipher(s, k)
        self.assertEqual(result, "Cnycau-Nqqm")

    def test_give_159357l_k2_should_be_159357n(self):
        self.assertEqual(caesar_cipher("159357l", 2), "159357n")