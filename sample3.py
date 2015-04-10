"""-------------------------------------------------------------------

Program Pingpong Bouncing
by Qianji Zheng
Texas Tech Dept. of Computer Science

-------------------------------------------------------------------"""


from EaselLib import *

def init():
    global Ball_Position, Ball_Img,Ball,V_Y,V_X,Hit_Sound,Boundary
    # "ball.png" must be in the folder called media
    Boundary = (-350,-250)
    Ball_Img = loadImageFile("pingpong.png")
    # set the initial position of the ball
    Ball_Position = (-350,-250)
    Ball = fileImg(Ball_Img,Ball_Position)
    Hit_Sound = loadSoundFile("pingpong.wav")
    V_Y = 15
    V_X = 5

def update():
    global Ball_Position,Ball
    Ball_Position = next_ball_position(Ball_Position)
    #Ball_Position = (Ball_Position[0] +10,Ball_Position[1])
    Ball = fileImg(Ball_Img,Ball_Position)

def next_ball_position(pos):
    global V_Y,V_X
    x,y = pos
    a = -0.98
    ax = -0.2
    next_x = x + V_X
    V_Y = V_Y+a
    V_X = V_X
    next_y = y+(V_Y + 0.5*a)
    if next_y < Boundary[1]:
        next_y = Boundary[1]
        V_Y = -V_Y

    if next_y==Boundary[1]:
        V_X =V_X-0.5
        if V_X<0:
            V_X=0
            V_Y=0
    # play the sound when the ball hits the ground
    if next_y<=Boundary[1] and (V_Y>0 or V_X>0):
        playSound(Hit_Sound)
    return (next_x,next_y)

def display():
    return [Ball]

