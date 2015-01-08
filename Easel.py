from EaselLED import *
import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror
def main(G):
    # Initialize the game engine
    global frameRate, windowDimensions
    pygame.init()
    frameRate=20
    windowDimensions = (800,600)
    G.init()
    print(windowDimensions)
    Screen = pygame.display.set_mode(windowDimensions)    
    clock = pygame.time.Clock()
    HALT = False
    while not HALT:
        images = G.output()
        drawImages(Screen,images,windowDimensions)
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        # 60 frame per second
        clock.tick(frameRate)
        click=None
        keyboard = []
        keys=[]
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done=True
                    sys.exit()
                else:
                    keys.append(chr(event.key))
            elif event.type == MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                # update click in Program
                click = (click[0]-windowDimensions[0]/2,windowDimensions[1]/2-click[1])
                #print(click)
        #print(keys)
        I = (click,keys)
        G.update(I)
        pygame.display.flip()        

def play(game):
    G = __import__(game)
    main(G)
play("TTT")
