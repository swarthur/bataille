from bataille.classes.carte import Carte
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

    def get_cartes(self, dernier_index: int=None)->list:
        """Retourne la liste des cartes du paquet d'index compris: 
         - entre 0 et dernier_index inclus si ce dernier est positif ou nul
         - entre -1 et dernier_index inclus si de dernier est négatif
        

        Args:
            dernier_index (int, optional): index "borne". Defaults to None.

        Raises:
            RuntimeError: Si l'index est hors-liste

        Returns:
            list: Liste des cartes
        """
        list_return = []
        if dernier_index == None:
            dernier_index = len(self)-1
        if abs(dernier_index)> len(self.cartes) or self.est_vide():
            raise RuntimeError("Index hors-liste")
        elif dernier_index<0:
            for carte in range(1, abs(dernier_index)+1):
                list_return.append(self.cartes[carte*-1])
        elif dernier_index>=0:
            for carte in range(0, dernier_index+1):
                list_return.append(self.cartes[carte])
        return list_return


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
        if en_haut:
            self.cartes = self.cartes + paquet.get_cartes()
        else:
            self.cartes = paquet.get_cartes() + self.cartes
            pass

    def retirer(self, index:int)-> Carte:
        if self.est_vide():
            raise RuntimeError("Paquet vide")
        return self.pop(index)

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
