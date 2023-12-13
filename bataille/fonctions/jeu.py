from bataille.classes.carte import Carte, SYMBOLES
from bataille.classes.paquet import Paquet

def creation_paquet_0()-> Paquet:
    """Crée un paquet de 52 cartes

    Returns:
        Paquet: Paquet contenant les 52 cartes créées
    """
    paquet_0 = Paquet([])
    for symbole in SYMBOLES:
        for valeur in range(1,14):
            paquet_0.ajouter(Carte(valeur, symbole))
    return paquet_0

def affrontement(paquet_1: Paquet, paquet_2:Paquet):
    """Compare la valeur de la tête des paquets et déclenche éventuellement une bataille.

    Args:
        paquet_1 (Paquet): Premier paquet de l'affrontement
        paquet_2 (Paquet): Second paquet de l'affrontement
        bataille_poss(bool, optional): Contrôle le déclenchement de la bataille
    """
    paquet_1bis = Paquet(paquet_1.retirer())
    paquet_2bis = Paquet(paquet_2.retirer())
    print(paquet_1bis.get_cartes()[-1], paquet_2bis.get_cartes()[-1])
    if (paquet_1bis.get_cartes()[-1])>(paquet_2bis.get_cartes()[-1]):
        paquet_1bis.assembler(paquet_2bis)
        paquet_1.assembler(paquet_1bis)
        return 1
    elif (paquet_2bis.get_cartes()[-1])>(paquet_1bis.get_cartes()[-1]):
        paquet_2bis.assembler(paquet_1bis)
        paquet_2.assembler(paquet_2bis)
        return 2
    else:
        return bataille((paquet_1, paquet_1bis), (paquet_2, paquet_2bis))

def bataille(paquets_1: tuple[Paquet, Paquet], paquets_2: tuple[Paquet, Paquet]):
    """Bataille

    Args:
        paquet_1 (tuple[Paquet, Paquet]): Premier couple de paquets de la bataille
        paquet_2 (tuple[Paquet, Paquet]): Second couple de paquets de la bataille
    """
    print("BATAILLE")
    paquet_1bis = paquets_1[1]
    paquet_2bis = paquets_2[1]
    for i in range(2):
        if not paquets_1[0].est_vide():
            paquet_1bis.recup(paquets_1[0], en_haut= True)
        if not paquets_2[0].est_vide():
            paquet_2bis.recup(paquets_2[0], en_haut=True)
    print(paquet_1bis, paquet_2bis)
    vainqueur = affrontement(paquet_1bis, paquet_2bis)
    print(paquet_1bis, paquet_2bis)
    paquets_1[0].assembler(paquet_1bis)
    paquets_2[0].assembler(paquet_2bis)
    return vainqueur