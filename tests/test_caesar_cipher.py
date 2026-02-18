import unittest
from coe_number.caesar_cipher import caesar_cipher

class CaesarCipherTest(unittest.TestCase):
    def test_give_Always_Look_k2_should_be_Cnycau_Nqqm(self):
        self.assertEqual(caesar_cipher("Always-Look", 2), "Cnways-Nqqm")