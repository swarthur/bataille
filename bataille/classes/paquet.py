from bataille.classes.carte import Carte
from bataille.classes.erreur import PaquetVideException, NbCartesInsuffisantException
from random import randint
from typing import Self


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
        if en_tete:
            self.cartes.append(carte)
        else:
            self.cartes.insert(0, carte)
    
    def assembler(self, paquet: Self, en_haut: bool=False):
        nouv_cartes = paquet.get_cartes()
        if en_haut:
            self.cartes = self.cartes + nouv_cartes
        else:
            self.cartes = nouv_cartes + self.cartes
        paquet.retirer(None)

    def retirer(self, indice_range:tuple[int, int]=None)-> list:
        """Retire et retourne la liste des cartes d'indices compris entre les deux éléments de indice_range

        Args:
            indice_range (tuple[int, int], optional): ensembles des indices dont les éléments sont à supprimer. Defaults to None.

        Raises:
            PaquetVideException: Si le paquet est vide

        Returns:
            list: Cartes retirées
        """
        if self.est_vide():
            raise PaquetVideException("Paquet vide")
        elif indice_range == None:
            paquet = self.get_cartes()
            self.cartes = []
            return paquet
        elif indice_range[0] == indice_range[1]:
            return [self.cartes.pop(indice_range[0])]
        else:
            if indice_range[1] > indice_range[0]:
                indice_range = (indice_range[1], indice_range[0])
            paquet = self.get_cartes()[indice_range[0]: indice_range[1]]
            self.cartes = self.cartes[:indice_range[0]] + self.cartes[indice_range[1]:]
            return paquet       
            
    def melanger(self)-> None:
        """
        Mélange le paquet
        """
        if self.est_vide():
            raise PaquetVideException("Paquet vide")
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
        if self.est_vide():
            raise PaquetVideException("Paquet vide")
        return self.cartes[-1]

    def recup(self, paquet: Self, nb_cartes:int = 1)-> None:
        """Récupère le nombre de cartes demandé à partir du haut du second paquet.

        Args:
            paquet (Self): Second paquet
            nb_cartes (int, optional): Nombre de cartes à récuperer. Defaults to 1.

        Raises:
            NbCartesInsuffisantException: Si il n'y as pas assez de cartes
        """
        if len(paquet) < nb_cartes:
            raise NbCartesInsuffisantException(f"Pas assez de cartes dans le paquet: {len(paquet)}")
        cartes_recup = Paquet(paquet.retirer((0-nb_cartes, -1)))
        self.assembler(cartes_recup)

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
            PaquetVideException: Erreur si le paquet est vide

        Returns:
            tuple[Self, Self]: Renvoie un tuple contenant les 2 nouveaux paquets créés.
        """
        if len(self.cartes)%2 != 0:
            raise RuntimeError("Nombre de cartes impair")
        elif self.est_vide():
            raise PaquetVideException("Paquet vide")
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
