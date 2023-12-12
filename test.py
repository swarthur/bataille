from bataille.classes.carte import Carte
from bataille.classes.paquet import Paquet

paquet_t1 = Paquet([Carte(4, 'trèfle'), Carte(1, "carreau"), Carte(10, 'coeur'), Carte(2, "pique")])
paquet_t2 = Paquet([Carte(5, "coeur"), Carte(8, "pique")])
print(paquet_t1)
paquet_t1.recup(paquet_t2, 2)
print(paquet_t1, paquet_t2)