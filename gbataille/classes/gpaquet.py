import pygame as pyg
from bataille.classes.carte import Carte
from bataille.classes.paquet import Paquet
from gbataille.classes.gcarte import GCarte
class GPaquet(Paquet):

    def __init__(self, cartes: list[Carte]) -> None:
        super().__init__(cartes)

    def convert_carte(self):
        while type(self.cartes[-1]) != GCarte:
            carte = self.cartes.pop(-1)
            self.ajouter(GCarte(carte.valeur, carte.symbole))

    def ajouter(self, carte: GCarte, en_tete: bool = False):
        if type(carte) not in [Carte, GCarte]:
            raise TypeError
        if en_tete:
            self.cartes.append(carte)
        else:
            self.cartes.insert(0, carte)