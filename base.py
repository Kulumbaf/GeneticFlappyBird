import pygame

class Base:

    def __init__(self, sprite):
        self.sprite = sprite
        self.x = 0
        self.y = 400
        self.xShift = -48

    def drawInGame(self, window):
        window.blit(self.sprite, (self.x, self.y))

        if self.x > self.xShift:
            self.x -= 2
        else:
            self.x = 0

    def drawInGameOver(self, window):
        window.blit(self.sprite, (self.x, self.y))
