from settings import *
from sprites import Sprites
from base import Base
from bird import Bird
from pipes import Pipes
from score import Score
from status import Status
from hitBoxe import HitBoxe
from audio import Audio

import pygame

def drawInMenu(window, background, message, base, bird, tick):
    window.blit(background.image, (background.x, background.y))
    window.blit(message.image, (message.x, message.y))
    base.drawInGame(window)
    bird.drawInMenu(window, tick)
    pygame.display.update()

def drawInGame(window, background, base, bird, pipes, score, tick):
    window.blit(background.image, (background.x, background.y))
    pipes.drawInGame(window)
    base.drawInGame(window)
    # score.draw(window)
    # bird.drawInGame(window, tick)
    pygame.display.update()

def drawGameOver(window, sprites, base, bird, tick, pipes, score):
    window.blit(sprites.background, (0, 0))
    pipes.drawInGameOver(window)
    base.drawInGameOver(window)
    score.draw(window)
    window.blit(sprites.gameOver, (50, 180))
    bird.drawInGame(window, tick)
    pygame.display.update()

def mainLoop(clock, window, sprites, audio):
    run = True
    status = Status.inMenu
    tick = 0

    base = Base(sprites.base)
    bird = Bird(sprites.bird)
    pipes = Pipes(sprites.pipe)
    # score = Score(sprites.numbers)
    score = 0

    # hitBoxe = HitBoxe(audio.hitSound, audio.dieSound, audio.pointSound)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if status == Status.inMenu and event.type == pygame.KEYUP and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                status = Status.inGame
        #     if status == Status.inGame and event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
        #         audio.wingSound.play()
        #         bird.time = 0
        #         bird.flapped = True
        #         bird.space = True
        #     if status == Status.gameOver and event.type == pygame.KEYUP and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
        #         status = Status.inMenu
        #         tick = 0
        #         base = Base(sprites.base)
        #         bird = Bird(sprites.bird)
        #         pipes = Pipes(sprites.pipe)
        #         score = Score(sprites.numbers)
        #         hitBoxe = HitBoxe(audio.hitSound, audio.dieSound, audio.pointSound)

        if status == Status.inMenu:
            drawInMenu(window, sprites.background, sprites.message, base, bird, tick)
        elif status == Status.inGame:
            drawInGame(window, sprites.background, base, bird, pipes, score, tick)
        # else:
        #     drawGameOver(window, sprites, base, bird, tick, pipes, score)

        # if status == Status.inGame:
        #     status1 = hitBoxe.birdHitBase(bird, base)
        #     status2 = hitBoxe.birdHitPipes(bird, pipes)
        #     hitBoxe.birdPassPipe(bird, pipes.pipes, score)
        #     if status1 == Status.gameOver or status2 == Status.gameOver:
        #         status = Status.gameOver

        if tick < FPS:
            tick += 1
        else:
            tick = 0

if __name__ == '__main__':
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(GAMENAME)
    sprites = Sprites()
    audio = Audio()

    mainLoop(clock, window, sprites, audio)

    pygame.quit()
