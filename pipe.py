import pygame

class Pipe:

    def __init__(self, sprite):
        self.sprite = sprite
        self.x = 200
        self.y = 192
        self.xShift = -52

    def draw(self, window):
        window.blit(self.sprite, (self.x, self.y))

        if self.x > self.xShift:
            self.x -= 2
        else:
            self.x = 200
