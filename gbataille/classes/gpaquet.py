import pygame as pyg
from bataille.classes.carte import Carte
from bataille.classes.paquet import Paquet

class Gpaquet(Paquet):

    def __init__(self, cartes: list[Carte]) -> None:
        super().__init__(cartes)
        for carte in cartes:
            if carte is Carte:
                index = carte