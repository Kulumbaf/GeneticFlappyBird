from status import Status

import pygame

class HitBoxe:

    def __init__(self, hitSound, dieSound, pointSound):
        self.hitSound = hitSound
        self.dieSound = dieSound
        self.pointSound = pointSound

    def birdHitBase(self, bird, base):
        if bird.y + bird.sprites[0].height >= base.sprite.y:
            self.hitSound.play()
            self.dieSound.play()
            return True
        return False

    def birdPassPipe(self, bird, pipes, score):
        for pairPipe in pipes:
            if pairPipe.passed == False and bird.x > pairPipe.x + pairPipe.sprite.width / 2:
                self.pointSound.play()
                score.incrementScore()
                pairPipe.passed = True

    def birdHitPipes(self, bird, pipes):
        birdHitBoxe = pygame.Rect(bird.x, bird.y, bird.sprites[0].width, bird.sprites[0].height)
        for pairPipe in pipes.pipes:
            upPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.yDown, pairPipe.sprite.width, pairPipe.sprite.height)
            bottomPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.yUp, pairPipe.sprite.width, pairPipe.sprite.height)
            if birdHitBoxe.colliderect(upPipeHitBoxe) or birdHitBoxe.colliderect(bottomPipeHitBoxe):
                self.hitSound.play()
                self.dieSound.play()
                return True
        return False
