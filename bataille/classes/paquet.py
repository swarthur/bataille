from bataille.classes.carte import Carte
from bataille.classes.erreur import NbCartesInsuffisantException
from random import randint
from typing import Self


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
        """Constructeur de Paquet

        Args:
            cartes (list[Carte]): Liste de cartes à ajouter
        """
        if type(cartes) != list:
            raise TypeError
        for carte in cartes:
            if type(carte) != Carte:
                raise TypeError
        self.cartes = cartes

    def get_cartes(self)-> list:
        """Retourne la liste des cartes du paquet

        Returns:
            list: Cartes du paquet
        """
        return self.cartes

    def ajouter(self, carte: Carte, en_tete: bool=False):
        """Ajoute une carte au paquet

        Args:
            carte (Carte): Carte à ajouter au paquet
            en_haut (bool): Définit si la carte doit être ajoutée en tête du paquet ou à la queue
        """
        if type(carte) != Carte:
            raise TypeError
        if en_tete:
            self.cartes.append(carte)
        else:
            self.cartes.insert(0, carte)
    
    def assembler(self, paquet: Self, en_haut: bool=False):
        nouv_cartes = paquet.retirer(0)
        if en_haut:
            self.cartes = self.cartes + nouv_cartes
        else:
            self.cartes = nouv_cartes + self.cartes

    def retirer(self, nb_cartes: int = 1)-> list:
        """Retire et retourne la liste des nb_cartes cartes du haut du paquet.
        0 retire et renvoie toutes les cartes du paquet.

        Args:
            nb_cartes (int, optional): nombre de cartes à retirer du paquet. Defaults to 1.

        Raises:
            NbCartesInsuffisantException: Si le paquet est vide

        Returns:
            list: Cartes retirées
        """
        if nb_cartes == 0:
            paquet = self.get_cartes()
            self.cartes = [] 
        elif len(self) < nb_cartes:
            raise NbCartesInsuffisantException(f"Pas assez de cartes dans le paquet: {len(self)}")
        else:
            paquet = []
            for i in range(nb_cartes):
                paquet.append(self.cartes.pop(-1))
        return paquet       
            
    def melanger(self)-> None:
        """
        Mélange le paquet
        """
        paquet_melange = []
        for carte in range (0,len(self.cartes)):
            carte_rand=randint(0,len(self.cartes)-1)
            paquet_melange.append(self.cartes.pop(carte_rand))
        self.cartes = paquet_melange

    def recup(self, paquet: Self, nb_cartes:int = 1, en_haut: bool= False)-> None:
        """Récupère le nombre de cartes demandé à partir du haut du second paquet et les ajoute au premier paquet.

        Args:
            paquet (Self): Second paquet
            nb_cartes (int, optional): Nombre de cartes à récuperer. Defaults to 1.
            en_haut (bool, optional): Si les cartes récupérées sont à placer en haut ou en bas du premier paquet

        Raises:
            NbCartesInsuffisantException: Si il n'y as pas assez de cartes
        """
        cartes_recup = Paquet(paquet.retirer(nb_cartes))
        self.assembler(cartes_recup, en_haut)

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
            NbCartesInsuffisantException: Erreur si le paquet est vide

        Returns:
            tuple[Self, Self]: Renvoie un tuple contenant les 2 nouveaux paquets créés.

        Contributeurs:
        Pierre
        """
        if len(self.cartes)%2 != 0:
            raise RuntimeError("Nombre de cartes impair")
        elif self.est_vide():
            raise NbCartesInsuffisantException("Paquet vide")
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
        
        Contributeur:
            Arthur. Co
        """
        return_str = "(b\n"
        for carte in self.cartes:
            return_str += f"{str(carte)}\n"
        return return_str + "h)"
    
    def __len__(self)-> int:
        """Retourne le nombre de cartes du paquet

        Returns:
            int: Nombre de cartes du paquet
        """
        return len(self.cartes)
