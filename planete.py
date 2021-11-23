import random

import pygame
from pygame.math import Vector2


class Planete:
    def __init__(self,l=400,h=400):
        self.pos = Vector2(random.randint(0,l),random.randint(0,h))
        self.vitesse = Vector2(random.uniform(-1,1),random.uniform(-1,1))
        self.acc = Vector2()
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.rayon = 5
        self.masse = 10
        self.nom="planete"
        self.maxVitesse = 20
        self.accMax = 1

    def applyForce(self,soleil):
        u = soleil.pos - self.pos
        u = u.normalize()

        f = 9 * (self.masse * soleil.masse)/ soleil.pos.distance_squared_to(self.pos) * u

        self.acc = f

        if self.acc.length() > self.accMax:
            self.acc = self.acc.normalize()
            self.acc = self.acc * self.accMax

    def deplacer(self):
        self.vitesse = self.vitesse + self.acc

        if self.vitesse.length() > self.maxVitesse:
            self.vitesse= self.vitesse.normalize()
            self.vitesse = self.vitesse * self.maxVitesse

        self.acc = Vector2()

        self.pos = self.pos + self.vitesse

    def afficher(self,screen):
        pygame.draw.circle(screen, self.color, self.pos, self.rayon)