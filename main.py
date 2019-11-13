from sprites import Sprites
import pygame

WINDOWWIDTH = 288
WINDOWHEIGHT = 512
GAMENAME = 'Flappy Bird'
FPS = 30

def mainLoop(clock, window, s):
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
        
        window.blit(s.background, (0, 0))
        pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(GAMENAME)
    sprites = Sprites()

    mainLoop(clock, window, sprites)

    pygame.quit()
