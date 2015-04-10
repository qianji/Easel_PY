"""-------------------------------------------------------------------

Program: Ball droping, bouncing and rolling
This is a sample program illustrating how to load a image from a file and a sound from a file and play the sound
by Qianji Zheng
Texas Tech Dept. of Computer Science

-------------------------------------------------------------------"""


from EaselLib import *
######################################################################
# windowDimensions: >> tuple
#
# set the window of game 800 pixel wide and 600 pixel high

def windowDimensions():
    return (800,600)

######################################################################
def init():
    global Ball_Location, Ball_Img,Velocity_Y,Velocity_X,Hit_Sound,Ground,Button_Img, Button_Location
    # load the ball image and button image from "pingpong.png" and "start_button.png" respectively
    # The image files must be in the folder called "media" in the game engine, where this program is in
    # You need to remember the size of your image file.

    # the size of the pingpong image is 50 x 50
    Ball_Img = loadImageFile("pingpong.png")
    # the size of the start button is 64 x 64
    Button_Img = loadImageFile("start_button.png")

    # set the initial location of the ball. The ball image's left-top point is (-350,100)
    Ball_Location = (-350,100)
    # set the location of the restart button. The button image's left-top point is (150,150)
    Button_Location = (150,150)
    # load the sound from a file. The file pingpong.wav must be put in the folder called media, where this program is in
    Hit_Sound = loadSoundFile("pingpong.wav")
    # set the initial velocity of the ball
    Velocity_Y = -15
    Velocity_X = 5
    # make the ground
    Ground = (-350,-250)

######################################################################
def update():
    # ball movement
    if ball_is_in_the_air():
        drop_ball()
    if ball_hits_ground():
        bounce_ball()
    if ball_is_on_ground():
        roll_ball()
    # clicking the button
    if start_button_clicked():
        init()
######################################################################
# when the ball is droppring, assume that it has acceleration of gravity
# and no air resistance
#
def drop_ball():
    global Velocity_Y,Velocity_X, Ball_Location
    x,y = Ball_Location
    # assume that there is no air resistance 
    next_x = x + Velocity_X
    # mimic acceleration of gravity
    acceleration = -0.98
    Velocity_Y = Velocity_Y+acceleration
    next_y = y+(Velocity_Y + 0.5*acceleration)
    if next_y<Ground[1]:
        next_y=Ground[1]
    Ball_Location = (next_x,next_y)
######################################################################
def bounce_ball():
    global Velocity_Y, Ball_Location
    x,y = Ball_Location
    # update ball location
    # reverse the dicrection of the velocity of y and slow it down to bounce to air
    Velocity_Y = -Velocity_Y -10
    if Velocity_Y <0:
        Velocity_Y = 0
    acceleration = -0.98
    next_y = y+(Velocity_Y + 0.5*acceleration)
    next_x = x + Velocity_X
    if next_y<Ground[1]:
        next_y=Ground[1]
    Ball_Location = (next_x,next_y)
    # play the sound
    playSound(Hit_Sound)
######################################################################
def roll_ball():
    global Velocity_X
    # slow down the ball
    Velocity_X = Velocity_X -0.5
    if Velocity_X <0:
        Velocity_X = 0

######################################################################
# ball_hits_ground: tuple -> Bool
# the ball hits the ground if its y-axis is less than or equal to the y-axis
# of the ground and the velocity of y-axis of the ball is not equal to 0

def ball_hits_ground():
    return Ball_Location[1]<=Ground[1] and Velocity_Y !=0

######################################################################
def ball_is_on_ground():
    return Ball_Location[1]==Ground[1]
######################################################################
def ball_is_in_the_air():
    return not ball_is_on_ground()

######################################################################
# ball_in_game: >> Sprite
#
def ball_in_game():
    return [fileImg(Ball_Img,Ball_Location)]
######################################################################
# click: >> Bool
#
# click() means the left mouse button has gone from up to down.

def click(): 
    return mouseDown and not oldMouseDown

######################################################################
def start_button_clicked():
    x,y = Button_Location
    return click() and x<mouseX<x+64 and y-64<mouseY<y
######################################################################

def start_button():
    return [fileImg(Button_Img,Button_Location)]
######################################################################
def display():
    return ball_in_game()+start_button()

