import pygame

FLAPPERSECOND = 5
RAISEPERSECOND = 2

class Bird:

    def __init__(self, sprites):
        self.sprites = sprites
        self.flapCount = 0
        self.x = 65
        self.y = 235
        self.yMaxMenu = 240
        self.yMinMenu = 230
        self.raising = 1
        self.width = 34
        self.height = 24

    def drawInMenu(self, window, tick):
        window.blit(self.sprites[self.flapCount], (self.x, self.y))

        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0

        if tick != 0 and tick % RAISEPERSECOND == 0:
            self.y += self.raising

        if self.y == self.yMaxMenu:
            self.raising = -1
        elif self.y == self.yMinMenu:
            self.raising = 1

    def drawInGame(self, window, tick):
        window.blit(self.sprites[self.flapCount], (self.x, self.y))

        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0
        self.y += 2
