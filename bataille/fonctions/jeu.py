from bataille.classes.carte import Carte, SYMBOLES
from bataille.classes.paquet import Paquet

def creation_paquet_0()-> Paquet:
    """Crée un paquet de 52 cartes

    Returns:
        Paquet: Paquet contenant les 52 cartes créées
    """
    paquet_0 = Paquet([])
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

def affrontement(paquet_1: Paquet, paquet_2:Paquet):
    """Compare la valeur de la tête des paquets et déclenche éventuellement une bataille.

    Args:
        paquet_1 (Paquet): Premier paquet de l'affrontement
        paquet_2 (Paquet): Second paquet de l'affrontement
    """
    if paquet_1.tete()>paquet_2.tete():
        paquet_1.recup(paquet_2)
        paquet_1.recup(paquet_1)
    elif paquet_2.tete()>paquet_1.tete():
        paquet_2.recup(paquet_1)
        paquet_2.recup(paquet_2)
    else:
        bataille(paquet_1, paquet_2)

def bataille(paquet_1: Paquet, paquet_2: Paquet):
    """Bataille

    Args:
        paquet_1 (Paquet): Premier paquet de la bataille
        paquet_2 (Paquet): Second paquet de la bataille
    """
    paquet_3 = Paquet([])
    paquet_3.recup(paquet_1)
    paquet_3.recup(paquet_2)
