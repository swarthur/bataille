from carte import Carte, SYMBOLES
from paquet import Paquet

def paquet_dep():
    paquet_depart=Paquet()
    for i in SYMBOLES:
        for y in range(1,14):
            paquet_depart.ajouter(Carte(y,i))


    return paquet_depart
