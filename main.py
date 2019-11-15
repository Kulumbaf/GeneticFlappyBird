from settings import *
from sprites import Sprites
from base import Base
from bird import Bird
from pipes import Pipes

import pygame

def drawMenu(window, s, base, bird, tick):
    window.blit(s.background, (0, 0))
    window.blit(s.message, (52, 50))
    base.draw(window)
    bird.drawInMenu(window, tick)
    pygame.display.update()

def drawGame(window, s, base, bird, tick, pipes):
    window.blit(s.background, (0, 0))
    pipes.draw(window)
    base.draw(window)
    bird.drawInGame(window, tick)
    pygame.display.update()

def mainLoop(clock, window, s):
    run = True
    runGame = False
    tick = 0
    base = Base(sprites.base)
    bird = Bird(sprites.bird)
    pipes = Pipes(sprites.pipe)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                runGame = True

        if runGame:
            drawGame(window, s, base, bird, tick, pipes)
        else:
            drawMenu(window, s, base, bird, tick)

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
