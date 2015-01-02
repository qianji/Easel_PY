'''
Qianji Zheng
July 2014

'''
def displaySize(width,height):
    return (width,height)

def color(r,g,b):
    return (r,g,b)
Black = color(0, 0, 0)
Red = color(255, 0, 0)
Orange = color(255, 128, 0)
Yellow = color(255, 255, 0)
Green = color(0, 255, 0)
Blue = color(0, 0, 255)
Indigo = color(70, 0, 130)
Violet = color(148, 0, 211)

def initialState():
    return {}

def triangle(p,q,r):
    return ("`fTri",p,q,r,Orange)

def disc(p,r,c):
    return ("`disc",p,r,c)

def paddle():
    return rectangle((350,125),(450,75))

def ball():
    return disc((400,135),5,Red)
def rectangle(tl,br):
    p=tl
    q=br
    r1=(tl[0],br[1])
    r2=(br[0],tl[1])
    upper = triangle(p,q,r2)
    lower = triangle(p,q,r1)
    return (upper,lower)

def images(S):
    return {paddle()[0],paddle()[1],ball()}

def transition(I,S):
    return S

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

    # Set the height and width of the screen
    size = [1000, 800]
    global screen, S
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    try:
        # initialize the initial state in LED program memory
        # set the global variable state named "GAMMA" in LED memory
        S = initialState()
    except :
        print("initialState is not defined in your program")
        return
    imgs = images(S)
    # draw the initial images before play
    drawImages(screen,imgs)
    done = False
    clock = pygame.time.Clock()
    while not done:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        # 60 frame per second
        clock.tick(60)
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
                    keys.append(event.key);
            elif event.type == MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                # update click in Program
                click = (click[0],size[1]-click[1])
        I = (click,keys)
        S= transition(I,S)
        imgs = images(S)
        drawImages(screen,imgs)
        #if ~drawSreeen(screen,inputAST):
        #    return
        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

# Be IDLE friendly
    pygame.quit()

play()
