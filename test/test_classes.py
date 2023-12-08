import unittest
from classes.carte import Carte
from classes.paquet import Paquet

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
        
class TestPaquet(unittest.TestCase):
    def test_recup(self):
        paquet_t1 = Paquet()
        paquet_t2 = Paquet()
        paquet_t1.ajouter(Carte(2, "trèfle"))
        paquet_t1.ajouter(Carte(5, "coeur"))
        paquet_t2.ajouter(Carte(6,"carreau"))
        paquet_t2.ajouter(Carte(7, "pique"))
        paquet_t1.recup(paquet_t2)
        self.assertTrue(paquet_t1.cartes[0].valeur == 7)
