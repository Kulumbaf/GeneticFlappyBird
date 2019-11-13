import pygame
from random import randint

class Sprites(object):

    def __init__(self):
        self.backgrounds = {
            'backgroundDay': pygame.image.load('assets/sprites/background-day.png'),
            'backgroundNight': pygame.image.load('assets/sprites/background-night.png')
        }
        self.background = self.setBackground()

    def setBackground(self):
        r = randint(0, 1)
        if r == 0:
            return self.backgrounds['backgroundDay']
        elif r == 1:
            return self.backgrounds['backgroundNight']
