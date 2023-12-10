from bataille.classes.carte import Carte
from bataille.classes.paquet import Paquet

paquet_t1 = Paquet([Carte(4, 'trèfle'), Carte(1, "carreau"), Carte(10, 'coeur'), Carte(2, "pique")])
paquet_t2 = Paquet([])
print(paquet_t2.melanger())
for carte in paquet_t1.get_cartes():
    print(carte)