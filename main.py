from bataille.fonctions.jeu import creation_paquet_0, affrontement
from bataille.classes.paquet import Paquet

def main(nb_cartes: int = 52, affichage_comment: bool = True):
    paquet_0 = creation_paquet_0(nb_cartes)
    paquet_0.melanger()
    paquet_1, paquet_2 = paquet_0.split()
    del paquet_0
    paquet_1bis = Paquet([])
    paquet_2bis =  Paquet([])
    vainqueur = None
    manche = 0
    while not (paquet_1.est_vide() or paquet_2.est_vide()):
        paquet_1bis.recup(paquet_1, en_haut=True)
        paquet_2bis.recup(paquet_2, en_haut=True)
        vainqueur = affrontement(paquet_1, paquet_1bis, paquet_2, paquet_2bis, affichage_comment)
        if affichage_comment:
            print(f"Vainqueur de la manche: {vainqueur}")
            print(f"\nManche {manche}")
        manche += 1
    if affichage_comment:
        print("\nVAINQUEUR DE LA PARTIE: ", vainqueur)

main(52, True)
