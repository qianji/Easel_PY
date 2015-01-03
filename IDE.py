'''
Qianji Zheng
July 2014

'''
def point(x,y):
    return (x,y)
def color(r,g,b):
    return (r,g,b)
def click(cl,p):
    return (cl,p)
def gameInput(cl,k):
    return (cl,k)
def text(s,p,n,c):
    return ("`txt",s,p,n,c)
def brick(tl,tr,bl,br):
    return (tl,tr,bl,br)
def ball(c,r,x,y):
    return (c,r,x,y)

def paddle(tl,tr,bl,br):
    return (tl,tr,bl,br)

def segment(p,r,c):
    return ("`seg",p,r,c)

def buildState(ba,p,br,c,d,u,e,t):
    return (ba,p,br,c,d,u,e,t)

def fTri(p,q,r,c):
    return ("`fTri",p,q,r,c)

def disc(p,r,c):
    return ("`disc",p,r,c)
dBlack = color(0, 0, 0)
dRed = color(255, 0, 0)
dOrange = color(255, 128, 0)
dYellow = color(255, 255, 0)
dGreen = color(0, 255, 0)
dBlue = color(0, 0, 255)
dIndigo = color(70, 0, 130)
dViolet = color(148, 0, 211)

boardTL = point(400, 800)
boardTR = point(1000, 800)
boardBL = point(400, 0)
boardBR = point(1000, 0)
reset = text("RESET GAME", point(100,750), 25, dGreen)

pTL = point(655, 100)
pTR = point(745, 100)
pBL = point(655, 95)
pBR = point(745, 95)

resetTL = point(0, 800)
resetTR = point(200, 800)
resetBL = point(0, 700)
resetBR = point(200, 700)

brick1TL = point(401, 800)
brick1TR = point(499, 800)
brick1BL = point(400, 750)
brick1BR = point(499, 750)
brick1 = brick(brick1TL, brick1TR, brick1BL, brick1BR)

brick2TL = point(501, 800)
brick2TR = point(599, 800)
brick2BL = point(501, 750)
brick2BR = point(599, 750)
brick2 = brick(brick2TL, brick2TR, brick2BL, brick2BR)

brick3TL = point(601, 800)
brick3TR = point(699, 800)
brick3BL = point(601, 750)
brick3BR = point(699, 750)
brick3 = brick(brick3TL, brick3TR, brick3BL, brick3BR)

brick4TL = point(701, 800)
brick4TR = point(799, 800)
brick4BL = point(701, 750)
brick4BR = point(799, 750)
brick4 = brick(brick4TL, brick4TR, brick4BL, brick4BR)

brick5TL = point(801, 800)
brick5TR = point(899, 800)
brick5BL = point(801, 750)
brick5BR = point(899, 750)
brick5 = brick(brick5TL, brick5TR, brick5BL, brick5BR)

brick5tTL = point(901, 800)
brick5tTR = point(999, 800)
brick5tBL = point(901, 750)
brick5tBR = point(999, 750)
brick5t = brick(brick5tTL, brick5tTR, brick5tBL, brick5tBR)

brick6TL = point(401, 750)
brick6TR = point(499, 750)
brick6BL = point(400, 700)
brick6BR = point(499, 700)
brick6 = brick(brick6TL, brick6TR, brick6BL, brick6BR)

brick7TL = point(501, 750)
brick7TR = point(599, 750)
brick7BL = point(501, 700)
brick7BR = point(599, 700)
brick7 = brick(brick7TL, brick7TR, brick7BL, brick7BR)

brick8TL = point(601, 750)
brick8TR = point(699, 750)
brick8BL = point(601, 700)
brick8BR = point(699, 700)
brick8 = brick(brick8TL, brick8TR, brick8BL, brick8BR)

brick9TL = point(701, 750)
brick9TR = point(799, 750)
brick9BL = point(701, 700)
brick9BR = point(799, 700)
brick9 = brick(brick9TL, brick9TR, brick9BL, brick9BR)

brick10TL = point(801, 750)
brick10TR = point(899, 750)
brick10BL = point(801, 700)
brick10BR = point(899, 700)
brick10 = brick(brick10TL, brick10TR, brick10BL, brick10BR)

brick10tTL = point(901, 750)
brick10tTR = point(999, 750)
brick10tBL = point(901, 700)
brick10tBR = point(999, 700)
brick10t = brick(brick10tTL, brick10tTR, brick10tBL, brick10tBR)

brick11TL = point(401, 700)
brick11TR = point(499, 700)
brick11BL = point(400, 650)
brick11BR = point(499, 650)
brick11 = brick(brick11TL, brick11TR, brick11BL, brick11BR)

brick12TL = point(501, 700)
brick12TR = point(599, 700)
brick12BL = point(501, 650)
brick12BR = point(599, 650)
brick12 = brick(brick12TL, brick12TR, brick12BL, brick12BR)

brick13TL = point(601, 700)
brick13TR = point(699, 700)
brick13BL = point(601, 650)
brick13BR = point(699, 650)
brick13 = brick(brick13TL, brick13TR, brick13BL, brick13BR)

brick14TL = point(701, 700)
brick14TR = point(799, 700)
brick14BL = point(701, 650)
brick14BR = point(799, 650)
brick14 = brick(brick14TL, brick14TR, brick14BL, brick14BR)

brick15TL = point(801, 700)
brick15TR = point(899, 700)
brick15BL = point(801, 650)
brick15BR = point(899, 650)
brick15 = brick(brick15TL, brick15TR, brick15BL, brick15BR)

brick15tTL = point(901, 700)
brick15tTR = point(999, 700)
brick15tBL = point(901, 650)
brick15tBR = point(999, 650)
brick15t = brick(brick15tTL, brick15tTR, brick15tBL, brick15tBR)

originPoint = point(-1000,-800)
ballStart = ball(point(700, 200), 7, 20, 16)
ballDead = ball(point(700, 200), 7, 0, 0)
paddleStart = paddle(pTL, pTR, pBL, pBR)
brickStart = {brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9, brick10, brick11, brick12, brick13, brick14, brick15, brick5t, brick15t, brick10t}

topBorder = segment(boardTL, boardTR, dBlack)
leftBorder = segment(boardTL, boardBL, dBlack)
rightBorder = segment(boardTR, boardBR, dBlack)
botBorder = segment(boardBL, boardBR, dBlack)

rtBorder = segment(resetTL, resetTR, dGreen)
rlBorder = segment(resetTL, resetBL, dGreen)
rrBorder = segment(resetTR, resetBR, dGreen)
rbBorder = segment(resetBL, resetBR, dGreen)

staticImgs = {reset, topBorder, leftBorder, rightBorder, botBorder, rtBorder, rlBorder, rrBorder, rbBorder}

def initialState():
    return buildState(ballStart, paddleStart, brickStart,0,0,{},{},0)
def transition(I,S):
    keys=I[1]
    ballMoveState = sClean(sHelper(motionHelper(S))) 
    return paddleHelper(ballMoveState, 1) if equalList(keys, "d") else \
            paddleHelper(ballMoveState, 0) if equalList(keys, "a")  else \
            ballMoveState 

def equalList(keys,char):
    return len(keys)>0 and keys[0]==char

def paddleHelper(S,flag):
    nextPaddle = paddleMove(S[1],flag)
    return buildState(S[0],nextPaddle,S[2],S[3],S[4],S[5],S[6],S[7]) 

def paddleMove(pad,flag):
    TL=nextPaddle(pad[0],flag)
    TR=nextPaddle(pad[1],flag)
    BL = nextPaddle(pad[2],flag)
    BR = nextPaddle(pad[3],flag)
    return paddle(TL,TR,BL,BR) 

def nextPaddle(p,flag):
    nextX = nextPX(p,flag)
    return point(nextX,p[1])

def nextPX(p,flag):
    val=20
    return p[0]+val if flag and not outOfBoundsR(p) else \
    p[0]-val if not flag and not outOfBoundsL(p) else \
    p[0]

def outOfBoundsL(p):
    return p[0]<=400
def outOfBoundsR(p):
    return p[1] >=1000

def ballMove(B):
    return ball(nextCenter(B[0],B[2],B[3]),B[1],B[2],B[3])

def nextCenter(p,xV,yV):
    x=p[0]
    y=p[1]
    nextX=x+xV
    nextY=y+yV
    return point(nextX,nextY)

def nextBall(S):
    B=S[0]
    bricks=S[2]
    sPaddle=S[1]
    char = brickBool(B,bricks)
    return yFlip(xFlip(B)) if vWallCollide(B) and hWallCollide(B) else \
        xFlip(B) if vWallCollide(B) or brickCollide(B,sPaddle)=="h" or char =="h" else \
        yFlip(B) if hWallCollide(B) or brickCollide(B,sPaddle)=="v" or char =="v" else \
        yFlip(xFlip(B)) if brickCollide(B,sPaddle)=="b" or char=="b" else \
        B
def yFlip(B):
    return ball(B[0], B[1], B[2], -1*B[3])

def xFlip(B):
    return ball(B[0], B[1], -1*B[2], B[3])

def vWallCollide(B):
    box=ballBox(B)
    nBox=ballBox(B)
    return (box[0][0] <= 400) or (box[1][0] >= 1000) or \
		(nBox[0][0] < 400) or (nBox[1][0] > 1000)
def hWallCollide(B):
    box=ballBox(B) 
    nBox=ballBox(B)
    return (box[2][1] <= 0) or (box[1][1] >= 800) or \
		(nBox[2][1] < 0) or (nBox[1][1] > 800)

def brickBool(B,bricks):
    collitions = bricksCollitions(B,bricks)
    return "b" if someBrick("b",collitions) or (someBrick("h",collitions) and someBrick("v",collitions)) else \
        "v" if noneBrick("b",collitions) and noneBrick("h",collitions) and someBrick("v",collitions) else \
        "h" if noneBrick("b",collitions) and noneBrick("v",collitions) and someBrick("h",collitions) else \
        "n"
def bricksCollitions(B,bricks):
    return [brickCollide(B,brick) for brick in bricks]
def someBrick(c,collitions):
    return c in collitions
def noneBrick(c,collitions):
    return not someBrick(c,collitions)

def brickCollide(B,brick):
    return "b" if cornerCollision(ballMove(B), brick) or cornerCollision(B, brick) else \
        "v" if (vCollision(ballMove(B), brick) or vCollision(B, brick)) else \
        "h" if (hCollision(ballMove(B), brick) or hCollision(B, brick)) else \
        "n"

def vCollision(B,L):
    box=ballBox(B)
    return ((box[0][1] >= L[3][1] and box[3][1] < L[3][1]) or (box[3][1] <= L[0][1] and box[0][1] > L[0][1])) \
            and between(L[2][0], L[1][0], range(box[2][0],box[1][0]))

def hCollision(B,L):
    box=ballBox(B)
    return ((box[1][0] >= L[2][0] and box[3][1] < L[3][1]) or (box[2][0] <= L[1][0] and box[1][0] > L[1][0])) \
            and between(L[3][1], L[0][1], range(box[3][1],box[0][1]))
def cornerCollision(B,L):
    return vCollision(B,L) and hCollision(B,L)
def between(bot,top,vals):
    return any([x<=top and x>=bot for x in vals])

def ballBox(B):
    return (point(B[0][0]-B[1],B[0][1]+B[1]),point(B[0][0]+B[1],B[0][1]+B[1]), point(B[0][0]-B[1],B[0][1]-B[1]), point(B[0][0]+B[1],B[0][1]-B[1]))

def motionHelper(S):
    return buildState(ballMove(nextBall(S)),S[1],S[2],S[3],S[4],S[5],S[6],S[7])

def sHelper(S):
    return S

def sClean(S):
    return (S[0],S[1],S[2],S[3],S[4],S[5],S[6],S[7]+1)
def images(S):
    return set.union(staticImgs,ballImg(S[0]),padImg(S[1]),brImg(S[2]))

def ballImg(b):
    p=b[0]
    r=b[1]
    c=dViolet
    return {disc(p,r,c)}

def padImg(pad):
    return boxImg(pad,dBlue)

def boxImg(L,c):
    TL=L[0]
    TR=L[1]
    BL=L[2]
    BR=L[3]
    return {segment(TL,TR,dBlack),segment(TL, BL, dBlack), segment(BL, BR, dBlack), segment(TR, BR, dBlack),fTri(TL, BR, BL, c), fTri(TL, TR, BR, c)}
def brImg(B):
    a = set()
    for br in B:
        a= set.union(a,boxImg(br,dOrange))
    return a
def sImg(dust):
    return set() if len(dust)==0 else disc(dust[2],dust[3],dRed)


'''
  staticImgs.union(ballImg(S[1]))padImg(S[2]) U brImg(S[3]) U sImg(S[6]) if S[4]=0 & S[5]=0;

brImg(B):=Union[br in B] boxImg(br,dOrange)
ballImg(b):={disc(p,r,c)} where p=b[1] & r=b[2] & c= dViolet
padImg(pad):=boxImg(pad,dBlue)
sImg(dust):= {} if |dust|=0;
disc(dust[3],dust[4],dRed) otherwise
'''
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
                    keys.append(chr(event.key));
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
