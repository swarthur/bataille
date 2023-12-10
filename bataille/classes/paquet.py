from bataille.classes.carte import Carte
from random import randint
from typing_extensions import Self


class Paquet():
    """Paquet de cartes
    Attributs:
        cartes(list): liste de cartes
    """
    def __init__(self, cartes:list[Carte]) -> None:
        """Constructeur de Paquet

        Args:
            cartes (list[Carte]): Liste de cartes à ajouter
        """
        self.cartes = cartes

    def ajouter(self, carte: Carte):
        """Ajoute une carte au paquet

        Args:
            carte (Carte): Carte à ajouter au paquet
        """
        self.cartes.append(carte)

    def melanger(self)-> None:
        """
        Mélange le paquet initial en mettant le résultat dans une boucle
        """
        paquet_melange = []
        for carte in range (0,len(self.cartes)):
            carte_rand=randint(0,len(self.cartes)-1)
            paquet_melange.append(self.cartes.pop(carte_rand))
        self.cartes = paquet_melange

    def tete(self)-> Carte:
        """Retourne la carte en haut du paquet

        Returns:
            Carte: Carte en haut du paquet
        """
        if not self.est_vide():
            return self.cartes[-1]

    def recup(self, paquet_adv: Self)-> None:
        carte_recup = paquet_adv.cartes.pop(-1)
        self.cartes.insert(0, carte_recup)

    def est_vide(self)-> bool:
        """Teste si le paquet est vide

        Returns:
            bool: Paquet vide ou non
        """
        if len(self) == 0:
            return True
        else:
            return False

    def split(self)-> tuple[Self, Self]:
        """Divise le paquet de X cartes en 2 paquets de X/2 cartes chacuns

        Raises:
            RuntimeError: Erreur si le nombre de cartes est impair
            RuntimeError: Erreur si le paquet est vide

        Returns:
            tuple[Self, Self]: Renvoie un tuple contenant les 2 nouveaux paquets créés.
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
            str: Chaine de caractère des cartes du paquet
        """
        return_str = "(\n"
        for carte in self.cartes:
            return_str += f"{str(carte)}\n"
        return return_str + ")"
    
    def __len__(self)-> int:
        """Retourne le nombre de cartes du paquet

        Returns:
            int: Nombre de cartes du paquet
        """
        return len(self.cartes)