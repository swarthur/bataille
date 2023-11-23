from constantes import SYMBOLES

class Carte():
    def __init__(self, valeur, symbole) -> None:
        if symbole not in SYMBOLES:
            raise RuntimeError("Symbole invalide")
        self.valeur = valeur
        self.symbole = symbole
        if symbole in ["trèfle", "pique"]:
            self.couleur = "noire"
        else:
            self.couleur = "rouge"

    def __lt__(self):
        pass
