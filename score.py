from settings import WINDOWWIDTH

import pygame

class Score:

    def __init__(self, sprites):
        self.sprites = sprites
        self.score = 0

    def incrementScore(self):
        if score < 9999:
            score += 1

    def draw(self, window):
        digits = [int(digit) for digit in list(str(self.score))]
        totalDigitsWidth = sum([self.sprites[digit].width for digit in digits])
        xShift = (WINDOWWIDTH - totalDigitsWidth) / 2

        for digit in digits:
            window.blit(self.sprites[digit].image, (xShift, self.sprites[0].y))
            xShift += self.sprites[digit].width
