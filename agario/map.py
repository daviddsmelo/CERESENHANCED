import self as self
from pygame import Vector2

import core
from agario.player import Player


class Map:
    def __init__(self):
        self.maxPlayer = 100
        self.maxFood = 100
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []
        self.pieges = []

    def spawn_found(self):
        pass

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()

    def addJoueur(self,p):
        if len(self.joueurs)<self.maxPlayer:
            self.joueurs.append(p)













