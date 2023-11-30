from carte import Carte
from random import randint

class Paquet():
   '''Classe de paquet
   Attributs :
        cartes(list): Liste de cartes crées dans la méthode Carte''' 
    def __init__(self) -> None:
        self.cartes = []

    def ajouter(self, carte: Carte):
        self.cartes.append(carte)

    def melanger(self):
        """Mélange le paquet initial en mettant le résultat dans une boucle
        """
        paquet_melange = []
        for i in range (0,len(self.cartes)):
            k=randint(0,len(self.cartes)-1)
            paquet_melange.append(self.cartes.pop(k))
        self.cartes = paquet_melange

    def split(self):
        """Divise le paquet de 52 cartes mélangé en 2 paquets de 26 cartes chacuns


        Returns:
            Lists: Renvoie les listes des 2 nouveaux paquets créés.
        """
        paquet_1 = Paquet()
        paquet_2 = Paquet()     
        for i in range(0,len(self.cartes)):
            if i<=25:
                paquet_1.ajouter(self.cartes[i])
            else:
                paquet_2.ajouter(self.cartes[i])
        return paquet_1, paquet_2

    def __str__(self) -> str:
        """Affichage des cartes dans le paquet

        Returns:
            str: Affiche les cartes
        """
        return_str = "(\n"
        for carte in self.cartes:
            return_str += f"{str(carte)}\n"
        return return_str + ")"

if __name__ == "__main__":
    liste = []
    for i in range(1, 53):
        liste.append(Carte(i, "trèfle"))
    #liste= [Carte(4, "trèfle"),Carte(1, "pique"), Carte(10,"coeur"), Carte(1,"carreau")]
    paquet_test = Paquet()
    for carte in liste:
        paquet_test.ajouter(carte)
    #print(paquet_test.cartes)
    #paquet_test.melanger()
    #print(paquet_test.cartes)
    paquet_1, paquet_2 = paquet_test.split()
    print(paquet_1)
    print(paquet_2)
    paquet_2.melanger()
    print(paquet_2)