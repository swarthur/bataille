from bataille.classes.carte import Carte, SYMBOLES
from bataille.classes.paquet import Paquet

def creation_paquet_0(nb_cartes:int = 52)-> Paquet:
    """Crée un paquet de nb_cartes cartes

    Args:
        nb_cartes (int, optional): Nombre de cartes dans le paquet à retourner.
    Returns:
        Paquet: Paquet contenant les cartes créées
    Contributeur :
        Arthur Chevalier
    """
    paquet_0 = Paquet([])
    for symbole in SYMBOLES:
        for valeur in range(1,nb_cartes//4+1):
            paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

def affrontement(paquet_1: Paquet, paquet_1bis: Paquet, paquet_2: Paquet, paquet_2bis:Paquet)-> int:
    """Déclenche l'affrontement entre les paquets des deux joueurs

    Args:
        paquet_1 (Paquet): Paquet du premier joueur. Paquet "caché".
        paquet_1bis (Paquet): Paquet du premier joueur. Paquet "visible".
        paquet_2 (Paquet): Paquet du second joueur. Paquet "caché".
        paquet_2bis (Paquet): Paquet du second joueur. Paquet "visible".
        
    Returns:
        int: numéro du joueur gagnant
    Contributeurs:
        Pierre
    """
    print(paquet_1bis.get_cartes()[-1], paquet_2bis.get_cartes()[-1])
    if (paquet_1bis.get_cartes()[-1])>(paquet_2bis.get_cartes()[-1]):
        paquet_1bis.assembler(paquet_2bis)
        paquet_1.assembler(paquet_1bis)
        return 1
    elif (paquet_2bis.get_cartes()[-1])>(paquet_1bis.get_cartes()[-1]):
        paquet_2bis.assembler(paquet_1bis)
        paquet_2.assembler(paquet_2bis)
        return 2
    else:
        return bataille(paquet_1, paquet_1bis, paquet_2, paquet_2bis)

def bataille(paquet_1: Paquet, paquet_1bis: Paquet, paquet_2: Paquet, paquet_2bis: Paquet)-> int:
    """Bataille

    Args:
        paquet_1 (Paquet): Paquet du premier joueur. Paquet "caché".
        paquet_1bis (Paquet): Paquet du premier joueur. Paquet "visible".
        paquet_2 (Paquet): Paquet du second joueur. Paquet "caché".
        paquet_2bis (Paquet): Paquet du second joueur. Paquet "visible".

    Returns:
        int: numéro du joueur gagnant
    
    Contributeurs:
        Pierre
        Arthur. Co
    """
    print("BATAILLE")
    for i in range(2):
        if not paquet_1.est_vide():
            paquet_1bis.recup(paquet_1, en_haut= True)
        if not paquet_2.est_vide():
            paquet_2bis.recup(paquet_2, en_haut=True)
    vainqueur = affrontement(paquet_1, paquet_1bis, paquet_2, paquet_2bis)
    print("FIN BATAILLE")
    return vainqueur