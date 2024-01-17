from bataille.classes.carte import Carte, SYMBOLES
from bataille.classes.paquet import Paquet
from bataille.classes.exceptions import NbCartesInvalideException

def creation_paquet_0(nb_cartes:int = 52)-> Paquet:
    """Crée un paquet de nb_cartes cartes

    Args:
        nb_cartes (int, optional): Nombre de cartes dans le paquet à retourner.

    Returns:
        Paquet: Paquet contenant les cartes créées

    Raises:
        NbCartesInvalideException: Si nb_cartes est différent de 32 ou 52.

    Contributeur :
        Arthur Ch.
    """
    if (nb_cartes != 52) and (nb_cartes != 32):
        raise NbCartesInvalideException("Impossible de créer un jeu de cartes un nombre de cartes différent de 32 ou 52")
    paquet_0 = Paquet([])
    for symbole in SYMBOLES:
        for valeur in range(1,nb_cartes//4+1):
            paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

def affrontement(paquet_1: Paquet, paquet_1bis: Paquet, paquet_2: Paquet, paquet_2bis:Paquet, affichage_comment: bool= True)-> int:
    """Déclenche l'affrontement entre les paquets des deux joueurs

    Args:
        paquet_1 (Paquet): Paquet du premier joueur. Paquet "caché".
        paquet_1bis (Paquet): Paquet du premier joueur. Paquet "visible".
        paquet_2 (Paquet): Paquet du second joueur. Paquet "caché".
        paquet_2bis (Paquet): Paquet du second joueur. Paquet "visible".
        affichage_comment(bool, optional): Définit si les batailles doivent être affichées en console. Defaults to True


    Returns:
        int: numéro du joueur gagnant

    Contributeurs:
        Pierre
    """
    if affichage_comment:
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
        return bataille(paquet_1, paquet_1bis, paquet_2, paquet_2bis, affichage_comment)

def bataille(paquet_1: Paquet, paquet_1bis: Paquet, paquet_2: Paquet, paquet_2bis: Paquet, affichage_comment: bool = True)-> int:
    """Bataille

    Args:
        paquet_1 (Paquet): Paquet du premier joueur. Paquet "caché".
        paquet_1bis (Paquet): Paquet du premier joueur. Paquet "visible".
        paquet_2 (Paquet): Paquet du second joueur. Paquet "caché".
        paquet_2bis (Paquet): Paquet du second joueur. Paquet "visible".
        affichage_comment(bool, optional): Définit si les batailles doivent être affichées en console. Defaults to True

    Returns:
        int: numéro du joueur gagnant
    
    Contributeurs:
        Pierre
        Arthur Co.
    """
    if affichage_comment:
        print("BATAILLE")
    for i in range(2):
        if not paquet_1.est_vide():
            paquet_1bis.recup(paquet_1, en_haut= True)
        if not paquet_2.est_vide():
            paquet_2bis.recup(paquet_2, en_haut=True)
    vainqueur = affrontement(paquet_1, paquet_1bis, paquet_2, paquet_2bis, affichage_comment)
    if affichage_comment:
        print("FIN BATAILLE")
    return vainqueur