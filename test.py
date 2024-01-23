from bataille.fonctions.jeu import creation_paquet_0
from gbataille.classes.gcarte import GCarte
from gbataille.classes.gpaquet import GPaquet

paquet0 = creation_paquet_0()
gpaquet0 = GPaquet(paquet0.cartes)
gpaquet0.convert_carte()
print(gpaquet0)
for carte in gpaquet0.get_cartes():
    print(carte.img)