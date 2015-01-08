from Drawing import *
import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror
class UserInput:
    ''' this is a class for user input 
    '''
    def __init__(self,L):
        if L[0]==None:
            (self.mouseX, self.mouseY), self.keysPressed = (None,None),L[1]
        else:
            (self.mouseX, self.mouseY), self.keysPressed =L


def main(G):
    # Initialize the game engine
    pygame.init()

    # Initialization of the game
    global frameRate, windowDimensions    
    frameRate=20
    windowDimensions = (800,600)
    G.init()

    # set the screen and clock
    Screen = pygame.display.set_mode(windowDimensions)    
    clock = pygame.time.Clock()
    HALT = False

    # the main loop
    while not HALT:
        # draw the images from the output to the screen
        images = G.output()
        drawImages(Screen,images,windowDimensions)
        pygame.display.flip()

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        # 60 frame per second
        clock.tick(frameRate)
        click=None
        keyboard = []
        keys=[]

        # get user input within one frame
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
        # update the game with user input
        IN = UserInput([click,keys])
        G.update(IN)

def play(game):
    # import the game file
    G = __import__(game)
    # call the game engine to play the game using the functions defined in the game file
    main(G)
play("boxClick")
