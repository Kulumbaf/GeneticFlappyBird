import pygame
from random import randint

class Sprites:

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
        self.pipes = {
            'greenPipe': pygame.image.load('assets/sprites/pipe-green.png'),
            'redPipe': pygame.image.load('assets/sprites/pipe-red.png')
        }
        self.numbers = [
            pygame.image.load('assets/sprites/0.png'),
            pygame.image.load('assets/sprites/1.png'),
            pygame.image.load('assets/sprites/2.png'),
            pygame.image.load('assets/sprites/3.png'),
            pygame.image.load('assets/sprites/4.png'),
            pygame.image.load('assets/sprites/5.png'),
            pygame.image.load('assets/sprites/6.png'),
            pygame.image.load('assets/sprites/7.png'),
            pygame.image.load('assets/sprites/8.png'),
            pygame.image.load('assets/sprites/9.png'),
        ]

        self.background = self.setBackground()
        self.base = pygame.image.load('assets/sprites/base.png')
        self.message = pygame.image.load('assets/sprites/message.png')
        self.gameOver = pygame.image.load('assets/sprites/gameover.png')
        self.bird = self.setBird()
        self.pipe = self.setPipe()

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

    def setPipe(self):
        r = randint(0, 1)
        if r == 0:
            return self.pipes['greenPipe']
        else:
            return self.pipes['redPipe']
