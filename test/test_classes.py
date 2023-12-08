import unittest
from classes.carte import Carte
from classes.paquet import Paquet
from copy import deepcopy

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
        del carte_test

class TestPaquet(unittest.TestCase):
    def test_init(self):
        carte_t1 = Carte(3, "coeur")
        carte_t2 = Carte(1, "pique")
        paquet_t1 = Paquet([carte_t1, carte_t2])
        paquet_t2 = Paquet()
        paquet_t2.ajouter(carte_t1)
        self.assertEqual(paquet_t1.tete(), carte_t2)
        self.assertEqual(paquet_t2.tete(), carte_t1)
        del paquet_t1, paquet_t2
    
    def test_ajouter(self):
        carte_t1 = Carte(3, "coeur")
        paquet_t1 = Paquet()
        paquet_t1.ajouter(carte_t1)
        self.assertTrue(carte_t1 in paquet_t1.cartes)
        del paquet_t1

    def test_melanger(self):
        paquet_t1 = Paquet([Carte(1, "pique"), Carte(5, "pique"), Carte(9, "coeur") ])
        paquet_t2 = deepcopy(paquet_t1)
        paquet_t2.melanger()
        self.assertFalse(paquet_t1.tete() == paquet_t2.tete())
        del paquet_t1
        del paquet_t2

    def test_tete(self):
        carte_t1 = Carte(7, "carreau")
        paquet_t1 = Paquet([Carte(3, "pique"), Carte(6, "coeur"), carte_t1])
        self.assertEqual(paquet_t1.tete(), carte_t1)
        del paquet_t1

    def test_recup(self):
        paquet_t1 = Paquet([Carte(2, "trèfle"), Carte(5, "coeur")])
        paquet_t2 = Paquet([Carte(6,"carreau"), Carte(7, "pique")])
        paquet_t1.recup(paquet_t2)
        self.assertTrue(paquet_t1.cartes[0].valeur == 7)
        del paquet_t1, paquet_t2

    def test_est_vide(self):
        paquet_t1 = Paquet([Carte(10, "carreau")])
        paquet_t2 = Paquet([])
        self.assertFalse(paquet_t1.est_vide())
        self.assertTrue(paquet_t2.est_vide())
        del paquet_t1, paquet_t2
    
    def test_split(self):
        paquet_t1 = Paquet([Carte(10, "carreau"), Carte(5, "coeur")])
        print(paquet_t1)
        paquet_t2, paquet_t3 = paquet_t1.split()
        print(paquet_t2)
        self.assertTrue(len(paquet_t2) == 1)
        self.assertTrue(len(paquet_t3) == 1)
        paquet_t4 = Paquet()
        with self.assertRaises(RuntimeError):
            paquet_t4.split()
        paquet_t4.ajouter(Carte(1, "trèfle"))
        with self.assertRaises(RuntimeError):
            paquet_t4.split()