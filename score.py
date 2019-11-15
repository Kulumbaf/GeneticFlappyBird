from settings import *

import pygame

NUMBERWIDTH = 24

class Score:

    def __init__(self, sprites):
        self.sprites = sprites
        self.score = 0
        self.y = 51

    def incrementScore(self):
        if score < 9999:
            score += 1

    def draw(self, window):
        digits = [int(digit) for digit in list(str(self.score))]
        totalDigitsWidth = 0
        for digit in digits:
            totalDigitsWidth += self.sprites[digit].get_width()
        xShift = (WINDOWWIDTH - totalDigitsWidth) / 2

        for digit in digits:
            window.blit(self.sprites[digit], (xShift, self.y))
            xShift += self.sprites[digit].get_width()
