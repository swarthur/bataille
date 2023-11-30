SYMBOLES = ["trèfle", "pique", "carreau", "coeur"]

class Carte():
    """Classe de cartes
    Attributs :
        valeur(int): Valeur de la carte
        symbole(str): Symbole de la carte
        couleur(str): Couleur du symbole de la carte
    """
    def __init__(self, valeur, symbole: SYMBOLES) -> None:
        if symbole not in SYMBOLES:
            raise RuntimeError("Symbole invalide")
        elif valeur > 13 or valeur < 0:
            raise RuntimeError("Valeur invalide")
        self.valeur = valeur
        self.symbole = symbole
        if symbole in ["trèfle", "pique"]:
            self.couleur = "noire"
        else:
            self.couleur = "rouge"

    def __lt__(self, carte)-> bool:
        """Compare deux cartes

        Args:
            carte (Carte): Seconde carte à comparer

        Returns:
            bool: Résultat de la comparaison
        """
        if self.valeur == carte.valeur:
            return None
        elif self.valeur == 1:
            return False
        elif carte.valeur == 1:
            return True
        elif self.valeur < carte.valeur:
            return True
        else: 
            return False
        
    def __str__(self) -> str:
        """Affiche la carte sous forme de chaine de caractères.

        Returns:
            str: Contient les infos de la carte
        """
        return f"| {self.valeur} {self.symbole} |"
