from fonctions.jeu import creation_paquet_0, affrontement

def main():
    paquet_0 = creation_paquet_0()
    paquet_0.melanger()
    paquet_1, paquet_2 = paquet_0.split()
    while not (paquet_1.est_vide() or paquet_2.est_vide()):
        affrontement(paquet_1, paquet_2)
    print(paquet_1, paquet_2)

main()
