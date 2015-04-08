import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror
from EaselLib import *
import traceback
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
    G.mouseDown = False
    G.keysDown = []
    HALT = False
    # the main loop
    while not HALT:
        # if display() is defined,display all the images in the list returned by display()
        if "display" in dir(G):
            images = G.display()
            drawImages(Screen,images)
            pygame.display.flip()

        # This limits the while loop to a max of frameRate times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(FR)

        # set the input variables 

        # get the mouse position; mouseX and mouseY are the horizontal and vertical  position of the mouse in the window
        G.mouseX,G.mouseY = pygame.mouse.get_pos()
        # make the (0,0) the center of the screen
        G.mouseX = G.mouseX - WD[0]/2
        G.mouseY = WD[1]/2 -G.mouseY

        # oldMouseDown is False in the first frame, and in each subsequent frame is the previous value of mouseDown from the previous frame. It is set to False initially.
        G.oldMouseDown = G.mouseDown

        # oldKeysDown  is a set of the keys that were down in the previous frame. It begins as empty.
        G.oldKeysDown = G.keysDown
        # mouseDown is true iff the left mouse button is down
        G.mouseDown=pygame.mouse.get_pressed()[0]

        # A key is an integer. Keys are named by global variables which are imported with EaselLib.py, given in the first column of the following table:
        G.keysDown = [i for i in range(0,len(pygame.key.get_pressed())) if pygame.key.get_pressed()[i]]
        pygame.key.set_repeat (500, 30)
        #keysPressed is a set of the keys that went from up to down
        G.keysPressed = []
        # get user input within one frame
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                HALT=True # Flag that we are done so we exit this loop
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    HALT=True
                else:
                    G.keysPressed.append(chr(event.key))

        # update the game with user input
        #IN = UserInput([mouseX,mouseY,oldMouseDown,mouseDown,oldKeysDown,keysDown,keysPressed])
        # if sounds() is defined, play the sounds in the list returned by sounds()
        if "sounds" in dir(G):
            playSounds(G.sounds())
        if "update" in dir(G):
            G.update()
    # Be IDLE friendly
    pygame.quit()

def play(game):
    # clear imported module cache
    if game in sys.modules:
        del sys.modules[game]
    # import the game file
    G = __import__(game)
    # call the game engine to play the game using the functions defined in the game file
    try:
        main(G)
    except:
        # print out the error message if there is an error in the game file
        print(traceback.format_exc())
        pygame.quit()
        return
#play("boxClick")
#play("spaceChase")
#play("rpg")
#play("tutorial")
#play("breakout")
