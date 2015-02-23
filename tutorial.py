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
    global BALL,BAT,BALL_POS, BAT_POS,BAT_SPEED,BALL_SPEED,RED, WALL
    RED = (255,0,0)
    # position is a point and speed is a pair 
    BALL_POS = [0,-200]
    BALL_SPEED = [7,7]
    BALL =loadImageFile("ball.png",BALL_POS[0],BALL_POS[1])
    BAT = loadImageFile("bat.png",-30,-215)
    WALL = wall();

def wall():
    # wall is a 4-tupels, where 1st coordinate is the boundary of the left of the wall
    lt = (-400,300)
    rt = (400,300)
    lb = (-400,-300)
    rb = (400,-300)
    left = seg(lt,lb,RED)
    top = seg(lt,rt,RED)
    right = seg(rt,rb,RED)
    bottom = seg(lb,rb,RED)
    return [left,top,right,bottom]

def speedZone():
    return circ((100,200),50,RED)
def isDead():
    ball,wall = S
    
def display():
    zone = speedZone()
    return [BALL,BAT,zone] + WALL

def update():
    global BALL, BAT, BALL_POS,BALL_SPEED
    pos_x,pos_y = BALL_POS
    speed_x, speed_y = BALL_SPEED
    #if pos_x >0 and pos_y>0:
        #speed_x +=1
    if pos_x >400-17 or pos_x < -400+3:
        speed_x = -speed_x
    if pos_y > 300-4 or pos_y <-300+17:
        speed_y = -speed_y
    # bounce and update speed
    BALL_SPEED = speed_x,speed_y
    # bounce and update ball position
    BALL_POS[0] += BALL_SPEED[0]
    BALL_POS[1] +=BALL_SPEED[1]
    # update ball
    BALL =loadImageFile("ball.png",BALL_POS[0],BALL_POS[1])




