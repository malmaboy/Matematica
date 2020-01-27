import pygame, sys
from pygame.locals import *


WINDOWWIDTH = 1000 
WINDOWHEIGHT = 600


#COLORS

GRAY     = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE    = (255, 255, 255)
RED      = (255, 0, 0)
GREEN    = (0, 255, 0)
BLUE     = (0, 0, 255)
YELLOW   = (255, 255, 0)
ORANGE   = (255, 128, 0)
PURPLE   = (255, 0, 255)
CYAN     = (0, 255, 255)
BLACK    = (0, 0, 0)
DARK_BLUE = (0, 0, 20)

BGCOLOR = DARK_BLUE
LIGHTBGCOLOR = GRAY



def main():
    
    global DYSPLAYSURF

    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('Mat')

    DYSPLAYSURF.fill(BGCOLOR)


    while True: 


        DYSPLAYSURF.fill(BGCOLOR)
    
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                exit()
        pygame.display.update()
        pygame.display.flip()
main()
