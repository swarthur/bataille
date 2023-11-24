import unittest
from classes.carte import Carte

class TestCarte(unittest.TestCase):
    def test_comparaison(self):
        self.assertIsNone(Carte(5,"carreau") > Carte(5, "pique"))
        self.assertFalse(Carte(1,"trèfle") < Carte(6, "pique"))
        self.assertTrue(Carte(1,"trèfle") > Carte(4,"coeur"))
        self.assertTrue(Carte(4, "coeur") > Carte(2, "carreau"))
        self.assertFalse(Carte(4, "coeur") < Carte(2, "carreau"))

    def test_init(self):
        carte_test = Carte(5, "coeur")
        self.assertEqual(carte_test.couleur, "rouge")
        self.assertEqual(carte_test.valeur, 5)
        self.assertEqual(carte_test.symbole, "coeur")
        self.assertRaises(RuntimeError, Carte, 5, "pomme")
        self.assertRaises(RuntimeError, Carte, 14, "trèfle")
        