class NbCartesInsuffisantException(Exception):
    """Levée lorsqu'il n'y a pas assez de cartes pour réaliser l'opération demandée.
    Contributeur:
        Arthur. Co"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)