import random

from pygame import Vector2

import core


class Player:
    def __init__(self):
        self.bot=True
        self.name="Bob"
        self.uuid=random.randint(100000,99999999999)
        self.mass=10
        self.vMax=10
        self.accMax=5
        self.position = Vector2(random.randint(0,core.WINDOW_SIZE[0]),random.randint(0,core.WINDOW_SIZE[1]))
        self.acc = Vector2(0,0)
        self.vitesse = Vector2(0,0)
        self.couleur = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def deplacement(self):
        if self.bot==False:
            k = (0.001, 10)
            u = 1
            la = 0.001
            l = core.getMouseLeftClick()
            Fa = k * u * (l - la)

            self.acc = Fa
            self.vitesse = self.vitesse = self.acc
            self.position = self.position + self.vitesse


    def grandir(self):
        pass

    def evaporation(self):
        pass

    def show(self):
        core.Draw.circle(self.couleur,self.position,self.mass)

