from settings import FPS

import pygame

FLAPPERSECOND = 5
RAISEPERSECOND = 2

GRAVITATIONALACCELERATION = 9.80665

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
        self.time = 0
        self.flapped = False
        self.space = False
        self.vy = 4
        self.rotate = 0

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
        window.blit(pygame.transform.rotate(self.sprites[self.flapCount], self.rotate), (self.x, self.y))

        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0

        self.time += 1
        if self.y + self.height < 400:
            if self.flapped == False:
                self.y = self.y + 3 #((1 / 2) * GRAVITATIONALACCELERATION * pow(self.time / FPS, 2) + self.y) * 1.02
                if self.rotate > -90:
                    self.rotate -= 3
            else:
                self.y += -self.vy
                if self.time % 10 == 0:
                    self.vy -= 1

            if self.flapped == True and self.time >= 15:
                self.time = 0
                self.flapped = False
                self.vy = 4

        if self.space:
            self.space = False
            self.rotate = 30