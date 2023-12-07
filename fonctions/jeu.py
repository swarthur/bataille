from classes.carte import Carte, SYMBOLES
from classes.paquet import Paquet

def creation_paquet_0()->Paquet:
    """Créer et retourne le paquet de départ (0)

    Returns:
        Paquet: Paquet de départ
    """
    paquet_0 = Paquet()
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            paquet_0.ajouter(Carte(symbole, valeur))
    return paquet_0


