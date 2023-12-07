from fonctions.jeu import creation_paquet_0

def main():
    paquet_0 = creation_paquet_0()
    print(paquet_0)
    paquet_0.melanger()
    print(paquet_0)
    paquet_1, paquet_2 = paquet_0.split()
    print(paquet_1)
    print(paquet_2)
