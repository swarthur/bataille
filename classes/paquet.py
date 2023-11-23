from carte import Carte

class Paquet():
    def __init__(self) -> None:
        self.cartes = []

    def ajouter(self, carte: Carte):
        self.cartes.append(carte)