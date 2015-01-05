############################################################################
# MY SILLY GAME
#
# You can move the diagonal line from one box to another by clicking 
# inside the boxes.


# States of this program are the integers 1 and 2

# The game starts in state 1

def initialState(): return 1

# displayImages(S) is a list of images to display on the screen in state S.
# For this game it consists of the background plus a line in one of the boxes.

def images(S):
    return background() + line(S)

def segment(x1,y1,x2,y2):
    p=(x1,y1)
    r=(x2,y2)
    c=(0,0,0)
    return ("seg",p,r,c)

# background() consists of two boxes side by side in the center
# of the screen.

def displaySize():
    return (1000,800)
def background():
    W,H = displaySize()
    L1 = segment(200,200,200,300)
    L2 = segment(400,200,400,300)
    L3 = segment(200,300,400,300)
    L4 = segment(200,200,400,200)
    L5 = segment(300,200,300,300)
    L6 = segment(-W//2,0,W//2,0)
    L7= segment(0,H//2,0,-H//2)
    return [L1,L2,L3,L4,L5,L6,L7]


# Line(S) is a diagonal line which is in the left background box
# if S=1, and the right backgroundbox if S=2.

def line(S):
    if S==2: return [segment(300,300,400,200)]
    if S==1: return [segment(200,300,300,200)]



# If S is a state and p is a point (x,y) on the screen, then successor(S,c) is
# the state resulting from clicking point p in state S.
#
# In this case, the game goes to state 1 if you click the left box, and state 2 if
# you click the right box. Laissez les bon temps rouler!

def transition(I,S):
    p = I[0]
    if p==None: return S
    if inLeftBox(p): return 1
    elif inRightBox(p): return 2
    else: return S

def inLeftBox(p):
    (x,y) = p
    return x<300 and x>200 and y<300 and y>200

def inRightBox(p):
    (x,y) = p
    return x>300 and x<400 and y<300 and y>200


#================================================================================================
# Easel LED game Engine
#================================================================================================
from EaselLED import *

import sys, os, pygame
from pygame.locals import *
from pygame.compat import geterror

def play():
    # Initialize the game engine
    pygame.init()
    global Screen, State, Size
    # Set the height and width of the screen
    try:
        Size = displaySize()
    except:
        print("displaySize is not defined in your program")
        return
    Screen = pygame.display.set_mode(Size)
    pygame.display.set_caption("My Game")
    try:
        # initialize the initial state in LED program memory
        # set the global variable state named "GAMMA" in LED memory
        State = initialState()
    except :
        print("initialState is not defined in your program")
        return
    imgs = images(State)
    # draw the initial images before play
    drawImages(Screen,imgs,Size)
    done = False
    clock = pygame.time.Clock()
    while not done:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        # 60 frame per second
        clock.tick(10)
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
                click = (click[0]-Size[0]/2,Size[1]/2-click[1])
                #print(click)
        #print(keys)
        I = (click,keys)
        State= transition(I,State)
        imgs = images(State)
        drawImages(Screen,imgs,Size)
        pygame.display.flip()
# Be IDLE friendly
    pygame.quit()

play()
