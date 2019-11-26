from status import Status

import pygame

class HitBoxe:

    def __init__(self, hitSound, dieSound, pointSound):
        self.hitSound = hitSound
        self.dieSound = dieSound
        self.pointSound = pointSound

    def birdHitBase(self, bird, base):
        if bird.y + bird.height >= base.y:
            self.hitSound.play()
            self.dieSound.play()
            return Status.gameOver
        return Status.inGame

    def birdPassPipe(self, bird, pipes, score):
        for pipe in pipes:
            if pipe.passed == False and bird.x > pipe.x + pipe.width / 2:
                self.pointSound.play()
                score.score += 1
                pipe.passed = True

    def birdHitPipes(self, bird, pipes):
        birdHitBoxe = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
        for pairPipe in pipes.pipes:
            upPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.yReversedSprite, pairPipe.width, pairPipe.height)
            bottomPipeHitBoxe = pygame.Rect(pairPipe.x, pairPipe.ySprite, pairPipe.width, pairPipe.height)
            if birdHitBoxe.colliderect(upPipeHitBoxe) or birdHitBoxe.colliderect(bottomPipeHitBoxe):
                self.hitSound.play()
                self.dieSound.play()
                return Status.gameOver
        return Status.inGame
