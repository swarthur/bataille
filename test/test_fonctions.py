import unittest
from bataille.fonctions.jeu import creation_paquet_0, affrontement, bataille

class TestFonctions(unittest.TestCase):
    def test_creation_paquet_0(self):
        paquet_0 = creation_paquet_0()
        self.assertEqual(len(paquet_0), 52)

    def test_affrontement(self):
        pass    
    
    def test_bataille(self):
        pass

