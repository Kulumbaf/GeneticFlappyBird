from settings import *
from sprites import Sprites
from base import Base
from bird import Bird
from pipes import Pipes
from score import Score
from status import Status
from hitBoxe import HitBoxe

import pygame

def drawMenu(window, sprites, base, bird, tick):
    window.blit(sprites.background, (0, 0))
    window.blit(sprites.message, (52, 50))
    base.draw(window)
    bird.drawInMenu(window, tick)
    pygame.display.update()

def drawGame(window, sprites, base, bird, tick, pipes, score):
    window.blit(sprites.background, (0, 0))
    pipes.draw(window)
    base.draw(window)
    score.draw(window)
    bird.drawInGame(window, tick)
    pygame.display.update()

def drawGameOver(window, sprites):
    window.blit(sprites.gameOver, (50, 180))
    pygame.display.update()

def mainLoop(clock, window, sprites):
    run = True
    status = Status.inMenu
    tick = 0
    base = Base(sprites.base)
    bird = Bird(sprites.bird)
    pipes = Pipes(sprites.pipe)
    score = Score(sprites.numbers)
    hitBoxe = HitBoxe()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if status == Status.inMenu and event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                status = Status.inGame
            if status == Status.gameOver and event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                status = Status.inMenu

        if status == Status.inMenu:
            drawMenu(window, sprites, base, bird, tick)
        elif status == Status.inGame:
            drawGame(window, sprites, base, bird, tick, pipes, score)
        else:
            drawGameOver(window, sprites)

        if status == Status.inGame:
            status = hitBoxe.birdHitBase(bird, base)
            hitBoxe.birdPassPipe(bird, pipes.pipes, score)
            if status == Status.gameOver:
                tick = 0
                base = Base(sprites.base)
                bird = Bird(sprites.bird)
                pipes = Pipes(sprites.pipe)
                score = Score(sprites.numbers)
                hitBoxe = HitBoxe()

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

    mainLoop(clock, window, sprites)

    pygame.quit()
