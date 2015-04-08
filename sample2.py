"""===================================================================
Program Box Click
by Dr. Nelson Rushton
Texas Tech Dept. of Computer Science

This is a sample game for the Easel_PY game engine, illustrating the
use of the init() and update() functions, and mouse polling using
the Easel_PY environment variables mouseDown, oldMouseDown, mouseX,
and mouseY.

The "play area" consists of two 100 x 100 boxes, outlined in black,
side by side in the center of the screen. There is a green dot of
radius 20 which starts in the left hand box, and can be moved from one
box to another by left clicking inside the box where you want the dot
to go. Laissez les bon temps rouler!

==================================================================="""

from EaselLib import *


# The states of the game are 'L' and 'R', which are short for left and
# right.  The game begins in state 'L'

def init():
    global state
    state = 'L'

# When the left box is clicked, the state becomes (or remains) 'L'.
# When the right box is clicked, the state becomes (or remains) 'R'.

def update():
    global state
    if LeftBoxClicked() : state = 'L'
    if RightBoxClicked(): state = 'R'


######################################################################
# Click: >> Bool
#
# Click() means the left mouse button has gone from up to down.

def Click(): 
    return mouseDown and not oldMouseDown


######################################################################
# LeftBoxClicked: >> Bool
#
# LeftBoxClicked() means a left down-click is being detected and
# the mouse pointer is inside the left hand box.
        
def LeftBoxClicked():
    return Click() and -100 < mouseX <0 and -50 < mouseY < 50


######################################################################
# RightBoxClicked: >> Bool
#
# RightBoxClicked() means a left down-click is being detected and
# the mouse pointer is inside the right hand box.

def RightBoxClicked():
    return Click() and 0 < mouseX < 100 and -50 < mouseY < 50


# black is the color black
black = (0,0,0)

# green is the color green
green = (0,255,0)


######################################################################
# boxes(): Sprite
#
# boxex() is a sprite consisting of two black-outlined boxes, 100 by
# 100 pixels, in the center of the screen.

def boxes():
    top = seg((-100,50),(100,50),black)
    bottom = seg((-100,-50),(100,-50),black)
    left = seg((-100,50),(-100,-50),black)
    right = seg((100,50),(100,-50),black)
    center = seg((0,50),(0,-50),black)
    return [top,bottom,left,right,center]


######################################################################
# dot: >> Sprite
#
# dot() is a green disc of radius 20, located in the center of the
# left box in state 'L', and the center of the right box in state 'R'.

def dot():
    D1 = disc((-50,0),20,green)
    D2 = disc((+50,0),20,green)
    return [D1] if state=='L' else [D2]


# The display consists of the boxes and the dot.

def display():
    return boxes() + dot()
      
