from settings import *

import pygame
from random import randint

PIPEWIDTH = 52
PIPEHEIGHT = 320
FIRSTPIPESPACE = WINDOWWIDTH + (WINDOWWIDTH / 2)
PIPEGAPSPACE = 100
MINRANDOMPIPETOP = 90
MAXRANDOMPIPETOP = 210

class PairPipe:

    def __init__(self, sprite, reversedSprite, x):
        self.sprite = sprite
        self.reversedSprite = reversedSprite
        self.x = x
        self.ySprite = 0
        self.yReversedSprite = 0
        self.getRandomYPosition()
        self.width = 52
        self.height = 320
        self.passed = False

    def getRandomYPosition(self):
        r = randint(MINRANDOMPIPETOP, MAXRANDOMPIPETOP)
        self.yReversedSprite = -PIPEHEIGHT + r
        self.ySprite = r + PIPEGAPSPACE

class Pipes:

    def __init__(self, sprite):
        self.sprite = sprite
        self.reversedSprite = pygame.transform.rotate(sprite, 180)
        self.pipes = [
            PairPipe(self.sprite, self.reversedSprite, FIRSTPIPESPACE),
            PairPipe(self.sprite, self.reversedSprite, FIRSTPIPESPACE + WINDOWWIDTH / 2),
            PairPipe(self.sprite, self.reversedSprite, FIRSTPIPESPACE + WINDOWWIDTH),
            PairPipe(self.sprite, self.reversedSprite, FIRSTPIPESPACE + WINDOWWIDTH + WINDOWWIDTH / 2)
        ]

    def draw(self, window):
        for pipe in self.pipes:
            window.blit(pipe.sprite, (pipe.x, pipe.ySprite))
            window.blit(pipe.reversedSprite, (pipe.x, pipe.yReversedSprite))

            if pipe.x > -PIPEWIDTH:
                pipe.x -= 2
            else:
                pipe.x = WINDOWWIDTH * 2 - PIPEWIDTH
                pipe.getRandomYPosition()
                pipe.passed = False
