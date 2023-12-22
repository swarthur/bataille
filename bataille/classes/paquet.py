from bataille.classes.carte import Carte
from random import randint

class Paquet():
    """Paquet de cartes
    Attributs:
        cartes(list): liste de cartes

    Contributeurs:
        Arthur.Ch 
        Arthur.Co
        Pierre
    """
    def __init__(self, cartes:list[Carte]) -> None:
        self.cartes = cartes

    def ajouter(self, carte: Carte):
        self.cartes.append(carte)

    def melanger(self):
        """
        Mélange le paquet initial en mettant le résultat dans une boucle

        Contributeurs:
            Pierre
            Arthur Co.
            Arthur Ch.
        """
        paquet_melange = []
        for i in range (0,len(self.cartes)):
            k=randint(0,len(self.cartes)-1)
            paquet_melange.append(self.cartes.pop(k))
        self.cartes = paquet_melange

    def tete(self):
        if not self.est_vide():
            return self.cartes[-1]

    def recup(self, paquet_adv):
        carte_recup = paquet_adv.cartes.pop(-1)
        self.cartes.insert(0, carte_recup)

    def est_vide(self):
        if len(self) == 0:
            return True
        else:
            return False

    def split(self):
        """Divise le paquet de X cartes en 2 paquets de X/2 cartes chacuns

        Returns:
            tuple: Renvoie un tuple contenant les 2 nouveaux paquets créés.

        Contributeurs:
        Pierre
        """
        if len(self.cartes)%2 != 0:
            raise RuntimeError("Nombre de cartes impair")
        elif self.est_vide():
            raise RuntimeError("Paquet vide")
        paquet_1 = Paquet([])
        paquet_2 = Paquet([])     
        for i in range(0,len(self.cartes)):
            if i<=(len(self.cartes)//2)-1:
                paquet_1.ajouter(self.cartes[i])
            else:
                paquet_2.ajouter(self.cartes[i])
        return paquet_1, paquet_2

    def __str__(self) -> str:
        """Affichage des cartes dans le paquet

        Returns:
            str: Affiche les cartes
        
        Contributeur:
            Arthur. Co
        """
        return_str = "(\n"
        for carte in self.cartes:
            return_str += f"{str(carte)}\n"
        return return_str + ")"
    
    def __len__(self):
        return len(self.cartes)