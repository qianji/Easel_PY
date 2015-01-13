from Drawing import *
import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror
from Sounds import *
class UserInput:
    ''' this is a class for user input 
    '''
    def __init__(self,L):
        self.mouseX, self.mouseY, self.oldMouseDown, self.mouseDown,self.oldKeysDown,self.keysDown,self.keysPressed =L

def main(G):
    # Initialize the game engine
    pygame.init()

    # Initialize the frameRate
    FR=20
    if "frameRate" in dir(G):
        FR = G.frameRate()

    # If windowDimensions() is not defined, set the window dimensions to  (800,600).
    # otherwise set it to the return value of windowDimensions().
    WD = (800,600)
    if "windowDimensions" in dir(G):
        WD = G.windowDimensions()

    #if init() is defined, call it
    if "init" in dir(G):
        G.init()

    # set the screen and clock
    Screen = pygame.display.set_mode(WD)    
    clock = pygame.time.Clock()
    #mouseDown is true iff the left mouse button is down
    mouseDown = False
    keysDown = []
    HALT = False
    # the main loop
    while not HALT:
        # if display() is defined,display all the images in the list returned by display()
        if "display" in dir(G):
            images = G.display()
            drawImages(Screen,images,WD)
            pygame.display.flip()

        # This limits the while loop to a max of frameRate times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(FR)

        # set the input variables 

        # get the mouse position; mouseX and mouseY are the horizontal and vertical  position of the mouse in the window
        mouseX,mouseY = pygame.mouse.get_pos()
        # make the (0,0) the center of the screen
        mouseX = mouseX - WD[0]/2
        mouseY = WD[1]/2 -mouseY

        # oldMouseDown is False in the first frame, and in each subsequent frame is the previous value of mouseDown from the previous frame. It is set to False initially.
        oldMouseDown = mouseDown

        # oldKeysDown  is a set of the keys that were down in the previous frame. It begins as empty.
        oldKeysDown = keysDown
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
        IN = UserInput([mouseX,mouseY,oldMouseDown,mouseDown,oldKeysDown,keysDown,keysPressed])
        # if sounds() is defined, play the sounds in the list returned by sounds()
        if "sounds" in dir(G):
            playSounds(G.sounds(IN))
        if "update" in dir(G):
            G.update(IN)
    # Be IDLE friendly
    pygame.quit()

def play(game):
    # import the game file
    G = __import__(game)
    # call the game engine to play the game using the functions defined in the game file
    main(G)
play("boxClick")
#play("breakout")
