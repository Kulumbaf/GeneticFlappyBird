from sprites import Sprites
from bird import Bird
import pygame

WINDOWWIDTH = 288
WINDOWHEIGHT = 512
GAMENAME = 'Flappy Bird'
FPS = 60

def mainLoop(clock, window, s, bird):
    run = True
    tick = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        window.blit(s.background, (0, 0))
        bird.drawBird(window, tick)
        pygame.display.update()

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
    bird = Bird(sprites.bird)

    mainLoop(clock, window, sprites, bird)

    pygame.quit()
