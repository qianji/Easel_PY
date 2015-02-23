# This is a simple game run on Easel Python Game Engine. It is served as a tutorial of how to creat a game using Easel_PY
# Author: Qianji Zheng, Texas Tech Univeristy
# Date Created: 2/21/2015
# Date Last Modified: 2/21/2015
#

# This is a simpified version of breakout game. The game is played on a 800*600 window. There are a ball, a ball and an empty wall in the game.
# When the game starts, the bar is placed 200 pixel above the botton of the wall and the ball is placed on the ball. The ball bounces off to the right 
# with speed (7,7). When the ball hits the right of the wall, it bonces to the left-up, in otherwords, the speed is (-7,7). If the ball hits the top of the wall,
# its speed is (-7,-7).


# EaselLib must be imported before writing any user defined functions
from EaselLib import *

def windowDimensions():
    return(1000,700)
def frameRate():
    return 20
def init():
    global BALL,BAT,BALL_IMG,BAT_IMG,BALL_POS, BAT_POS,BAT_SPEED,BALL_SPEED,RED, WALL
    # define the color red
    RED = (255,0,0)

    # load the bat in the sub_folder in "media". The bat is a 80*12 image file
    BAT_IMG = loadImageFile("bat.png")
    # define the initial position of the bar. 
    BAT_POS = (-40,-200)
    # define the speed of the bat. Whenever the player move the bat, the position of the bat is based on the speed of the bar and its previous position
    BAT_SPEED = 20
    BAT = fileImg(BAT_IMG,BAT_POS)

    # load the ball image, which is 17 * 17 pixel
    BALL_IMG =loadImageFile("ball.png")
    # define the initial position of the ball. The ball is placed 1 pixel above the top of the bat
    BALL_POS = (0,-200+17+1)
    # define the speed of the ball, the 1st coordinate is x speed and 2nd is y speed
    BALL_SPEED = (7,7)
    BALL = fileImg(BALL_IMG,BALL_POS)

    # Draw the wall using segments
    WALL = wall();

    # play the background music infinitly
    playBackGroundMusic("house_lo.wav")

# wall() is a list of segments [left,top,right,bottom] in red, which are the left, top, right and bottom segment of the wall respetively
def wall():
    lt = (-400,300)
    rt = (400,300)
    lb = (-400,-300)
    rb = (400,-300)
    left = seg(lt,lb,RED)
    top = seg(lt,rt,RED)
    right = seg(rt,rb,RED)
    bottom = seg(lb,rb,RED)
    return [left,top,right,bottom]

def display():
    if gameOver():
        playSound(BOING)
        init()
    return [BALL,BAT] + WALL

def update():
    global BALL, BAT, BALL_POS,BALL_SPEED,BALL_IMG,BAT_POS
    pos_x,pos_y = BALL_POS
    speed_x, speed_y = BALL_SPEED

    # check if the ball hits the left or right boundary of the wall
    if pos_x >400-17 or pos_x < -400+3:
        # reverse the x speed
        speed_x = -speed_x
    # check if the ball hits the top or bottom boundary of the wall
    if pos_y > 300-4 or pos_y <-300+17:
        #reverse the y speed
        speed_y = -speed_y
    # bounce the wall and update speed
    BALL_SPEED = speed_x,speed_y

    # update bat
    bat_pos_x, bat_pos_y = BAT_POS
    # if "d" is down then move the bat to the right
    if K_d in keysDown:
        bat_pos_x += BAT_SPEED
    # if "a" is down then move the bat to the left
    if K_a in keysDown:
        bat_pos_x -=BAT_SPEED
    # prevent the bat from moving throught the wall when it hits the right of the wall
    if bat_pos_x >=400-80:
        bat_pos_x = 400-80
    # prevent the bat from moving throught the wall when it hits the left of the wall
    if bat_pos_x <=-400:
        bat_pos_x = -400
    # update bat position
    BAT_POS = bat_pos_x,bat_pos_y
    BAT = fileImg(BAT_IMG,BAT_POS)

    # if the ball collides with the bat then bounce the ball and update the ball speed and postion
    # whenever the ball hits the bat, both x speed and y speed increase by 2 and play the collission sound DING
    if isCollided():
        # reverse y speed
        speed_y = -speed_y
        # increase x speed by 2
        if speed_x >0:
            speed_x+=2
        else:
            speed_x-=2
        # increase y speed by 2
        if speed_y>0:
            speed_y+=2
        else:
            speed_y-=2

        playSound(DING)
    BALL_SPEED = speed_x,speed_y

    # bounce and update ball position
    pos_x += BALL_SPEED[0]
    pos_y += BALL_SPEED[1]
    # update ball position
    BALL_POS = (pos_x,pos_y)
    BALL = fileImg(BALL_IMG,BALL_POS)

# isCollided() iff the ball collides with the bat in the current game
def isCollided():
    return BAT_POS[1]-12<BALL_POS[1]<BAT_POS[1] + 17 and BAT_POS[0]-17<BALL_POS[0]<BAT_POS[0]+80

# gameOver() iff the ball is below the bat
def gameOver():
    return BALL_POS[1] < BAT_POS[1]-24
