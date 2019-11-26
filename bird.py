from settings import FPS

import pygame

YMAXINMENU = 240
YMININMENU = 230

FLAPPERSECOND = 5
RAISEPERSECOND = 2

GRAVITATIONALACCELERATION = 9.80665  #((1 / 2) * GRAVITATIONALACCELERATION * pow(self.time / FPS, 2) + self.y) * 1.02

class Bird:

    def __init__(self, sprites):
        self.sprites = sprites
        self.x = self.sprites[0].x
        self.y = self.sprites[0].y

        self.flapCount = 0
        self.yRaise = 1

        self.time = 0
        self.flapped = False
        self.space = False
        self.vy = 4
        self.rotate = 0

    def _flap(self, tick):
        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0

    def _raise(self, tick):
        if tick != 0 and tick % RAISEPERSECOND == 0:
            self.y += self.yRaise
        if self.y == YMAXINMENU:
            self.yRaise = -1
        elif self.y == YMININMENU:
            self.yRaise = 1

    def drawInMenu(self, window, tick):
        window.blit(self.sprites[self.flapCount].image, (self.x, self.y))
        self._flap(tick)
        self._raise(tick)

    def drawInGame(self, window, tick):
        window.blit(pygame.transform.rotate(self.sprites[self.flapCount], self.rotate), (self.x, self.y))

        self._flap()

        self.time += 1
        if self.y + self.height < 400:
            if self.flapped == False:
                self.y = self.y + 3
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