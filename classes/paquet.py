from carte import Carte
from random import randint

class Paquet():
    def __init__(self) -> None:
        self.cartes = []

    def ajouter(self, carte: Carte):
        self.cartes.append(carte)

    def melanger(self):
        paquet_melange = []
        for i in range (0,len(self.cartes)):
            k=randint(0,len(self.cartes)-1)
            paquet_melange.append(self.cartes.pop(k))
        self.cartes = paquet_melange

    def split(self):
        paquet_1 = Paquet()
        paquet_2 = Paquet()     
        for i in range(0,len(self.cartes)):
            if i<=25:
                paquet_1.ajouter(carte)
            else:
                paquet_2.ajouter(carte)
        return paquet_1, paquet_2
        

liste= [Carte(4, "trèfle"),Carte(1, "pique"), Carte(10,"coeur"), Carte(1,"carreau")]
paquet_test = Paquet()
for carte in liste:
    paquet_test.ajouter(carte)
print(paquet_test.cartes)
paquet_test.melanger()
print(paquet_test.cartes)
paquet_1, paquet_2 = paquet_test.split()
print(paquet_1)
print(paquet_2)