import pygame
from pygame.math import Vector2


class Soleil:
    def __init__(self):
        self.pos = Vector2(200,200)
        self.color = (255, 255, 255)
        self.rayon = 15
        self.masse = 10

    def afficher(self, screen):
        pygame.draw.circle(screen,self.color,self.pos,self.rayon)