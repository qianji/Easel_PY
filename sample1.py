
"""-------------------------------------------------------------------

Program TTTBoard
by Dr. Nelson Rushton
Texas Tech Dept. of Computer Science

This is a sample game for the Eeasel_PY  game programming environment.
This sample illustrates the use of colors, segments, circles, text
images, and sprites, all of which are defined in the Easel_PY document-
ation. Though this program runs in the Easel_PY game engine, this
program isn't a "game" in the usual sense; it just draws a picture. 

When "played", this game creates an 800 x 600 window containing a black
tic tac toe board, with a black 'x' in the upper left square and a
black 'o' in the center square, and a heading in orange saying "Tic Tac
Toe" abover the board. It looks like a game of tic tac toe in progress.

The tic tac toe grid is 300 x 300 pixels, centered in the window. The
x's and o's are each 90 pixesls high and 90 pixels wide, centered in
their respective squares. The heading is in 40 point font. 

-------------------------------------------------------------------"""


from EaselLib import *

# black is the color black
black = (0,0,0)

# orange is the color orange
orange = (250,100,0) 


######################################################################
# grid(): Sprite
#
# grid() is a black 300 x 300 tic tac toe board
# in the center of the screen.

def grid():
    L1 = seg((-50,150), (-50,-150),black)
    L2 = seg((50,150), (50,-150),black)
    L3 = seg((-150,50), (150,50),black)
    L4 = seg((-150,-50), (150,-50),black)
    return [L1,L2,L3,L4]


######################################################################
# upperLeftX(): Sprite
#
# upperLeftX() an image of an 'x' in the upper left corner
# of grid()

def upperLeftX():
    L1 = seg((-145,145), (-55,55),black)
    L2 = seg((-145,55), (-55,145), black)
    return [L1,L2]


######################################################################
# centerO(): Sprite
#
# centerO(): an image of an 'o' in the center square of grid()

def centerO():
    return [circ((0,0),45,black)]

######################################################################
# heading(): Sprite
#
# heading() is an orange text image saying "Tic Tac Toe", centered
# near the top of the screen.

def heading():
    msg = "Tic Tac Toe"
    return [txt(msg,(0,250), 40,orange)]


                
def display():
    return heading() + grid() + upperLeftX() + centerO() 
