from typing import Any
import pygame as pyg
from bataille.classes.carte import SYMBOLES, Carte
from os import getcwd
class GCarte(Carte):
    def __init__(self, valeur: int, symbole: SYMBOLES) -> None:
        super().__init__(valeur, symbole)
        self.img = pyg.image.load(f"{getcwd()}\\gbataille\\images\\{self.symbole}_{self.valeur}.png")