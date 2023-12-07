from classes.carte import Carte, SYMBOLES
from classes.paquet import Paquet

def creation_paquet_0()->Paquet:

    """"creer paquet_0
    
    boucle qui creer 13 cartes par symboles avec leur valeurs puis les ajoutes dans paquet_0

    return:
    Lists: Renvoie la liste du paquet_0 de 52 cartes
    """
    paquet_0 = Paquet()
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            paquet_0.ajouter(Carte(symbole, valeur))
    return paquet_0


