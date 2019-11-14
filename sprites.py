import pygame
from random import randint

class Sprites(object):

    def __init__(self):
        self.backgrounds = {
            'backgroundDay': pygame.image.load('assets/sprites/background-day.png'),
            'backgroundNight': pygame.image.load('assets/sprites/background-night.png')
        }
        self.birds = {
            'yellowBird': [
                pygame.image.load('assets/sprites/yellowbird-midflap.png'),
                pygame.image.load('assets/sprites/yellowbird-downflap.png'),
                pygame.image.load('assets/sprites/yellowbird-midflap.png'),
                pygame.image.load('assets/sprites/yellowbird-upflap.png')
            ],
            'redBird': [
                pygame.image.load('assets/sprites/redbird-midflap.png'),
                pygame.image.load('assets/sprites/redbird-downflap.png'),
                pygame.image.load('assets/sprites/redbird-midflap.png'),
                pygame.image.load('assets/sprites/redbird-upflap.png')
            ],
            'blueBird': [
                pygame.image.load('assets/sprites/bluebird-midflap.png'),
                pygame.image.load('assets/sprites/bluebird-downflap.png'),
                pygame.image.load('assets/sprites/bluebird-midflap.png'),
                pygame.image.load('assets/sprites/bluebird-upflap.png')
            ]
        }
        
        self.background = self.setBackground()
        self.message = pygame.image.load('assets/sprites/message.png')
        self.bird = self.setBird()

    def setBackground(self):
        r = randint(0, 1)
        if r == 0:
            return self.backgrounds['backgroundDay']
        else:
            return self.backgrounds['backgroundNight']
    
    def setBird(self):
        r = randint(0, 2)
        if r == 0:
            return self.birds['yellowBird']
        elif r == 1:
            return self.birds['redBird']
        else:
            return self.birds['blueBird']
