import pygame

FLAPPERSECOND = 5
SWINGPERSECOND = 5

class Bird:

    def __init__(self, sprites):
        self.sprites = sprites
        self.flapCount = 0
        self.x = 65
        self.y = 235
    
    def drawBird(self, window, tick):
        window.blit(self.sprites[self.flapCount], (self.x, self.y))

        if tick != 0 and tick % FLAPPERSECOND == 0 and self.flapCount < 3:
            self.flapCount += 1
        elif tick != 0 and tick % FLAPPERSECOND == 0:
            self.flapCount = 0
