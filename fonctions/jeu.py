from classes.carte import Carte, SYMBOLES
from classes.paquet import Paquet

def creation_paquet_0(max_paquet: int=52):
    paquet_0 = Paquet()
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            if max_paquet > len(paquet_0.cartes):
                paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

def affrontement(paquet_1: Paquet, paquet_2:Paquet):
    if paquet_1.tete()>paquet_2.tete():
        paquet_1.recup(paquet_2)
        paquet_1.recup(paquet_1)
    elif paquet_2.tete()>paquet_1.tete():
        paquet_2.recup(paquet_1)
        paquet_2.recup(paquet_2)
    else:
        bataille(paquet_1, paquet_2)

def bataille(paquet_1: Paquet, paquet_2: Paquet):
    paquet_3 = Paquet()
    paquet_4 = Paquet()
    if len(paquet_1)>=3:
        for i in range(3):
            paquet_3.recup(paquet_1, True)
    if len(paquet_1)==2:
        for i in range(2):
            paquet_3.recup(paquet_1, True)
    if len(paquet_1)==1:
        paquet_3.recup(paquet_1, True)
    if len(paquet_2)>=3:
        for i in range(3):
            paquet_4.recup(paquet_2, True)
    if len(paquet_2)==2:
        for i in range(2):
            paquet_4.recup(paquet_2, True)
    if len(paquet_2)==1:
        paquet_4.recup(paquet_2, True)
    affrontement(paquet_3,paquet_4)

    



