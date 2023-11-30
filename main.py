from fonctions.jeu import paquet_dep

def main():
    paquet_0 = paquet_dep()
    print(paquet_0)
    paquet_0.melanger()
    print(paquet_0)
    paquet_1, paquet_2 = paquet_0.split()
    print(paquet_1)
    print(paquet_2)
