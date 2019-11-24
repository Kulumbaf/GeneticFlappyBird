from status import Status

class HitBoxe:

    def __init__(self):
        pass

    def birdHitBase(self, bird, base):
        if bird.y + bird.height > base.y:
            return Status.gameOver
        return Status.inGame

    def birdPassPipe(self, bird, pipes, score):
        for pipe in pipes:
            if pipe.passed == False and bird.x > pipe.x + pipe.width / 2:
                score.score += 1
                pipe.passed = True
