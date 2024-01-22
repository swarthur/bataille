import pygame as pyg
from bataille.fonctions.jeu import creation_paquet_0, affrontement
from bataille.classes.paquet import Paquet

def main_graph():
    pyg.init()
    pyg.display.set_caption("BATAILLE")
    pyg.display.set_icon(pyg.image.load("./gbataille/images/back.png"))
    fond = pyg.image.load("./bataille/images/fond_poker_new.png")
    screen = pyg.display.set_mode((900, 676), flags=pyg.SCALED)
    clock = pyg.time.Clock()
    running = True
    paquet_0 = creation_paquet_0()
    paquet_0.melanger()
    paquet_1, paquet_2 = paquet_0.split()
    del paquet_0
    paquet_1bis = Paquet([])
    paquet_2bis =  Paquet([])
    vainqueur = None
    manche = 0
    while running and not (paquet_1.est_vide() or paquet_2.est_vide()):
        screen.blit(fond, (0,0))
        screen
        pyg.display.update()
        print(f"\nManche {manche}")
        paquet_1bis.recup(paquet_1, en_haut=True)
        paquet_2bis.recup(paquet_2, en_haut=True)
        vainqueur = affrontement(paquet_1, paquet_1bis, paquet_2, paquet_2bis)
        print(f"Vainqueur de la manche: {vainqueur}")
        manche += 1
    print("\nVAINQUEUR DE LA PARTIE: ", vainqueur)
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

main_graph()