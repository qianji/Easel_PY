# Easel_PY
Easel is an engine for creating real time games.This version, EaselPY, allows the programmer to create games by writing Python code, and runs on Windows or Mac OS. 

# The Tiny Python Game Engine
The tiny Python game engine (TPGE) is a simple piece of Python code which, when combined with Peter Zelle's graphics library and code supplied by a student-developer, creates an interactive GUI program (typically a simple game, hence the name) that runs in a 600 by 500 pixel window. 

While Python is (unfortunately) an untyped langauge, the use of TPGE requires the programmer to use the following data model. This is not Python code, but specifies an understanding of how certain Python data structures are to  be intuitively interpreted: 

- A point is a pair (x,y) of integers where 0 ≤ x ≤ 600 and 0≤ y ≤ 500. 
- A line segment is a 4-tuple (x1,y1,x2,y2) of integers where 0 ≤ x1, x2 ≤ 600 and 0≤ y1, y2≤ 500. Intuitively, it is the line segment   connecting the points (x1,y1) and (x2,y2) in the coordinate system whose origin is the lower left corner of the display screen. 
- A Circle is a triple (x,y,R) where (x,y) is a point and R is an integer. It is thought of as the circle whose center is (x,y) and whose radius is R, in the coordinate system whose origin is the lower left corner of the display screen. 
- A displayText is 4-tuple (c,x,y,s) where c is a string, x and y are nonnegative integers, and s is an integer in the interval [5,37). Intuitively, displayText (c,x,y,s) is the image of a text string, centered at point (x,y) of height s in pixels.
- An image is a line segment, a circle, or a displayText. 
- An imageList is a list of images.
- A state is whatever sort of Python data structure the student-developer wants it to be -- but they should be clear in their mind about it.

The student-supplied functions consist of the following three functions, along with any helpers necessary to implement them:
- initialState : state --InitialState() is the initial state of the program.
- successor: state x point  → state -- successor(S,p) is the state resulting from clicking point p in state S
- displayImages: state  → imageList -- displayImages(S) is a list containing the images to be displayed on the screen in program state S. Images occurring later in the list overwrite images that occur earlier if they overlap. 

Below is an example of a trivial game created using the engine, followed by code for the game engine itself. It should run if you have Python 3.x and  graphics.py installed. 

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

def displayImages(S):
    return background() + line(S)

# background() consists of two boxes side by side in the center
# of the screen.

def background():
    L1 = (200,200,200,300)
    L2 = (400,200,400,300)
    L3 = (200,300,400,300)
    L4 = (200,200,400,200)
    L5 = (300,200,300,300)
    return [L1,L2,L3,L4,L5]


# Line(S) is a diagonal line which is in the left background box
# if S=1, and the right backgroundbox if S=2.

def line(S):
    if S==2: return [(300,300,400,200)]
    if S==1: return [(200,300,300,200)]



# If S is a state and p is a point (x,y) on the screen, then successor(S,c) is
# the state resulting from clicking point p in state S.
#
# In this case, the game goes to state 1 if you click the left box, and state 2 if
# you click the right box. Laissez les bon temps rouler!

def successor(S,p):
    if inLeftBox(p): return 1
    elif inRightBox(p): return 2
    else: return S

def inLeftBox(p):
    (x,y) = p
    return x<300 and x>200 and y<300 and y>200

def inRightBox(p):
    (x,y) = p
    return x>300 and x<400 and y<300 and y>200



######################################################################
######################################################################
# TPGE GAME ENGINE
#
# Student code is linked with this code to create a game.

# displaySize() is the size of the display window, (width, height)

def displaySize() : return (600,500)
from graphics import *

# If x is an image, imageKind(x) is the type of image x is:
# 'circle', 'text', or 'lineSegment'

def imageKind(x):
    if len(x)==3 : return 'circle'
    elif type(x[0])== str :return 'text'
    else : return 'lineSegment'

    
# If x is an image, convert(x) is the corresponding image in the
# graphics.py library. We turn the screen upside down so that the origin
# is in the lower left corner, so it matches what they learn in algebra
# class.

def convert(x):
    if imageKind(x)=='circle': return convertCircle(x)
    elif imageKind(x)=='lineSegment': return convertLine(x)
    elif imageKind(x)=='text' : return convertText(x)


def convertLine(x):
    (W,H) = displaySize()
    P1 = Point(x[0],H - x[1])
    P2 = Point(x[2],H - x[3])
    return Line(P1,P2)

def convertText(x):
    (W,H) = displaySize()
    center = Point(x[1],H-x[2])
    string = x[0]
    size = x[3]
    T = Text(center,string)
    T.setSize(size)
    return T

def convertCircle(x):
    (W,H) = displaySize()
    center = Point(x[0],H-x[1])
    radius = x[2]
    return Circle(center,radius)

# Create a window to play in
display = GraphWin("My game", displaySize()[0], displaySize()[1])


# The main loop
#
# Set the state, draw the display, get a mouse click, set the new state,
# and repeat until the user closes the window.

S = initialState()
images = [convert(x) for x in displayImages(S)]

while(True):
    for x in images: x.draw(display)
    c = display.getMouse()
    click = (c.getX(),displaySize()[1] - c.getY())
    S = successor(S,click)
    for I in images: I.undraw()
    images = [convert(x) for x in displayImages(S)]
  
