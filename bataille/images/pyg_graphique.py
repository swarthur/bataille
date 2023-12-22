import pygame as pyg

def main_graph():
    pyg.init()
    screen = pyg.display.set_mode((1280, 720))
    clock = pyg.time.Clock()
    running = True

    while running:


        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False

main_graph()