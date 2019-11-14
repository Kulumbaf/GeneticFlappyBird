from sprites import Sprites
from base import Base
from bird import Bird
import pygame

WINDOWWIDTH = 288
WINDOWHEIGHT = 512
GAMENAME = 'Flappy Bird'
FPS = 60

def draw(window, s, base, bird, tick):
    window.blit(s.background, (0, 0))
    window.blit(s.message, (52, 50))
    base.draw(window)
    bird.draw(window, tick)
    pygame.display.update()

def mainLoop(clock, window, s):
    run = True
    tick = 0
    base = Base(sprites.base)
    bird = Bird(sprites.bird)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
        
        draw(window, s, base, bird, tick)

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
