from Drawing import *
import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror
class UserInput:
    ''' this is a class for user input 
    '''
    def __init__(self,L):
        self.mouseX, self.mouseY, self.oldMouseDown, self.mouseDown, self.keysDown,self.keysPressed =L


def main(G):
    # Initialize the game engine
    pygame.init()

    # Initialization of the game
    frameRate=20
    windowDimensions = (800,600)
    G.init()

    # set the screen and clock
    Screen = pygame.display.set_mode(windowDimensions)    
    clock = pygame.time.Clock()
    #mouseDown is true iff the left mouse button is down
    mouseDown = False

    HALT = False
    # the main loop
    while not HALT:
        # draw the images from the output to the screen
        images = G.output()
        drawImages(Screen,images,windowDimensions)
        pygame.display.flip()

        # This limits the while loop to a max of frameRate times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(frameRate)

        # set the input variables 

        # get the mouse position; mouseX and mouseY are the horizontal and vertical  position of the mouse in the window
        mouseX,mouseY = pygame.mouse.get_pos()
        # make the (0,0) the center of the screen
        mouseX = mouseX - windowDimensions[0]/2
        mouseY = windowDimensions[1]/2 -mouseY

        # oldMouseDown is False in the first frame, and in each subsequent frame is the previous value of mouseDown from the previous frame. It is set to False initially.
        oldMouseDown = mouseDown

        # mouseDown is true iff the left mouse button is down
        mouseDown=pygame.mouse.get_pressed()[0]

        # keysDown stores the value of pygame.key.get_pressed()
        keysDown = pygame.key.get_pressed()
        
        #keysPressed is a set of the keys that went from up to down
        keysPressed = []
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
                    keysPressed.append(chr(event.key))
        # update the game with user input
        IN = UserInput([mouseX,mouseY,oldMouseDown,mouseDown,keysDown,keysPressed])
        G.update(IN)
    # Be IDLE friendly
    pygame.quit()

def play(game):
    # import the game file
    G = __import__(game)
    # call the game engine to play the game using the functions defined in the game file
    main(G)
play("boxClick")
