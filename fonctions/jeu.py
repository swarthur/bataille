from classes.carte import Carte, SYMBOLES
from classes.paquet import Paquet

def creation_paquet_0():
    paquet_0 = Paquet()
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

