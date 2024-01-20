from bataille.fonctions.jeu import creation_paquet_0, affrontement
from bataille.classes.paquet import Paquet

def main(nb_cartes: int = 52, affichage_comment: bool = True) -> tuple[int, int]:
    """Démarre une partie du jeu de la bataille

    Args:
        nb_cartes (int, optional): Nombre de carte du paquet de départ. Defaults to 52.
        affichage_comment (bool, optional): Affichage ou non des informations de jeu. Defaults to True.

    Returns:
        tuple: Informations de la partie : (vainqueur de la partie, nombre de manches)

    Contributeur:
        Arthur Co.
    """
    paquet_0 = creation_paquet_0(nb_cartes)
    paquet_0.melanger()
    paquet_1, paquet_2 = paquet_0.split()
    del paquet_0
    paquet_1bis = Paquet([])
    paquet_2bis =  Paquet([])
    vainqueur = None
    manche = 0
    while not (paquet_1.est_vide() or paquet_2.est_vide()):
        manche += 1
        if affichage_comment:
            print(f"\nManche {manche}")
        paquet_1bis.recup(paquet_1, en_haut=True)
        paquet_2bis.recup(paquet_2, en_haut=True)
        vainqueur = affrontement(paquet_1, paquet_1bis, paquet_2, paquet_2bis, affichage_comment)
        if affichage_comment:
            print(f"Vainqueur de la manche: {vainqueur}")
    if affichage_comment:
        print("\nVAINQUEUR DE LA PARTIE: ", vainqueur)
    return vainqueur, manche


def main_simulation(nb_iterations: int = 100, nb_cartes: int = 52, affichage_comment: bool = False):
    """Mode simulation: exécute des parties le nombre désiré de fois et retourne les statistiques des parties.

    Args:
        nb_iterations (int, optional): Nombre de parties à jouer. Defaults to 100.
        nb_cartes (int, optional): Nombre de cartes dans le paquet de départ. Defaults to 52.
        affichage_comment (bool, optional): Affichage ou non des informations de jeu. Ralentis fortement l'exécution. Defaults to False.
    
    Contributeur:
        Arthur Co.
    """
    somme_manche = 0
    gagnant = [0,0]
    for i in range(nb_iterations):
        partie = main(nb_cartes, affichage_comment)
        gagnant[partie[0]-1] += 1
        somme_manche += partie[1]
    print(f"Nombre d'itérations de la simulation: {nb_iterations}")
    print(f"Nombre moyen de manches: {somme_manche / nb_iterations}")
    print(f"Nombre de victoires par joueur: Joueur 1 : {gagnant[0]} | Joueur 2 : {gagnant[1]}")

if __name__ == "__main__":
    main()
