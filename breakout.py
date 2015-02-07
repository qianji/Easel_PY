'''
Qianji Zheng
July 2014

'''
from EaselLib import *
def point(x,y):
    return (x,y)
def color(r,g,b):
    return (r,g,b)
def click(cl,p):
    return (cl,p)
def brick(tl,tr,bl,br):
    return (tl,tr,bl,br)
def ball(c,r,x,y):
    return (c,r,x,y)

def paddle(tl,tr,bl,br):
    return (tl,tr,bl,br)

def buildState(ba,p,br,c,d,u,e,t):
    return (ba,p,br,c,d,u,e,t)

dBlack = color(0, 0, 0)
dRed = color(255, 0, 0)
dOrange = color(255, 128, 0)
dYellow = color(255, 255, 0)
dGreen = color(0, 255, 0)
dBlue = color(0, 0, 255)
dIndigo = color(70, 0, 130)
dViolet = color(148, 0, 211)

boardTL = point(-100, 400)
boardTR = point(500, 400)
boardBL = point(-100, -400)
boardBR = point(500, -400)
reset = txt("RESET GAME", point(-400,350), 25, dGreen)

pTL = point(155, -300)
pTR = point(245, -300)
pBL = point(155, -305)
pBR = point(245, -305)

resetTL = point(-500, 400)
resetTR = point(-300, 400)
resetBL = point(-500, 300)
resetBR = point(-300, 300)

brick1TL = point(-99, 400)
brick1TR = point(-1, 400)
brick1BL = point(-100, 350)
brick1BR = point(-1, 350)
brick1 = brick(brick1TL, brick1TR, brick1BL, brick1BR)

brick2TL = point(1, 400)
brick2TR = point(99, 400)
brick2BL = point(1, 350)
brick2BR = point(99, 350)
brick2 = brick(brick2TL, brick2TR, brick2BL, brick2BR)

brick3TL = point(101, 400)
brick3TR = point(199, 400)
brick3BL = point(101, 350)
brick3BR = point(199, 350)
brick3 = brick(brick3TL, brick3TR, brick3BL, brick3BR)

brick4TL = point(201, 400)
brick4TR = point(299, 400)
brick4BL = point(201, 350)
brick4BR = point(299, 350)
brick4 = brick(brick4TL, brick4TR, brick4BL, brick4BR)

brick5TL = point(301, 400)
brick5TR = point(399, 400)
brick5BL = point(301, 350)
brick5BR = point(399, 350)
brick5 = brick(brick5TL, brick5TR, brick5BL, brick5BR)

brick5tTL = point(401, 400)
brick5tTR = point(499, 400)
brick5tBL = point(401, 350)
brick5tBR = point(499, 350)
brick5t = brick(brick5tTL, brick5tTR, brick5tBL, brick5tBR)

brick6TL = point(-99, 350)
brick6TR = point(-1, 350)
brick6BL = point(-100, 300)
brick6BR = point(-1, 300)
brick6 = brick(brick6TL, brick6TR, brick6BL, brick6BR)

brick7TL = point(1, 350)
brick7TR = point(99, 350)
brick7BL = point(1, 300)
brick7BR = point(99, 300)
brick7 = brick(brick7TL, brick7TR, brick7BL, brick7BR)

brick8TL = point(101, 350)
brick8TR = point(199, 350)
brick8BL = point(101, 300)
brick8BR = point(199, 300)
brick8 = brick(brick8TL, brick8TR, brick8BL, brick8BR)

brick9TL = point(201, 350)
brick9TR = point(299, 350)
brick9BL = point(201, 300)
brick9BR = point(299, 300)
brick9 = brick(brick9TL, brick9TR, brick9BL, brick9BR)

brick10TL = point(301, 350)
brick10TR = point(399, 350)
brick10BL = point(301, 300)
brick10BR = point(399, 300)
brick10 = brick(brick10TL, brick10TR, brick10BL, brick10BR)

brick10tTL = point(401, 350)
brick10tTR = point(499, 350)
brick10tBL = point(401, 300)
brick10tBR = point(499, 300)
brick10t = brick(brick10tTL, brick10tTR, brick10tBL, brick10tBR)

brick11TL = point(-99, 300)
brick11TR = point(-1, 300)
brick11BL = point(-100, 250)
brick11BR = point(-1, 250)
brick11 = brick(brick11TL, brick11TR, brick11BL, brick11BR)

brick12TL = point(1, 300)
brick12TR = point(99, 300)
brick12BL = point(1, 250)
brick12BR = point(99, 250)
brick12 = brick(brick12TL, brick12TR, brick12BL, brick12BR)

brick13TL = point(101, 300)
brick13TR = point(199, 300)
brick13BL = point(101, 250)
brick13BR = point(199, 250)
brick13 = brick(brick13TL, brick13TR, brick13BL, brick13BR)

brick14TL = point(201, 300)
brick14TR = point(299, 300)
brick14BL = point(201, 250)
brick14BR = point(299, 250)
brick14 = brick(brick14TL, brick14TR, brick14BL, brick14BR)

brick15TL = point(301, 300)
brick15TR = point(399, 300)
brick15BL = point(301, 250)
brick15BR = point(399, 250)
brick15 = brick(brick15TL, brick15TR, brick15BL, brick15BR)

brick15tTL = point(401, 300)
brick15tTR = point(499, 300)
brick15tBL = point(401, 250)
brick15tBR = point(499, 250)
brick15t = brick(brick15tTL, brick15tTR, brick15tBL, brick15tBR)

originPoint = point(-1000,-800)
ballStart = ball(point(200, -200), 7, 14, 12)
ballDead = ball(point(200, -200), 7, 0, 0)
paddleStart = paddle(pTL, pTR, pBL, pBR)

def brickStart():
    return [brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9, brick10, brick11, brick12, brick13, brick14, brick15, brick5t, brick15t, brick10t]
topBorder = seg(boardTL, boardTR, dBlack)
leftBorder = seg(boardTL, boardBL, dBlack)
rightBorder = seg(boardTR, boardBR, dBlack)
botBorder = seg(boardBL, boardBR, dBlack)

rtBorder = seg(resetTL, resetTR, dGreen)
rlBorder = seg(resetTL, resetBL, dGreen)
rrBorder = seg(resetTR, resetBR, dGreen)
rbBorder = seg(resetBL, resetBR, dGreen)

staticImgs = [reset, topBorder, leftBorder, rightBorder, botBorder, rtBorder, rlBorder, rrBorder, rbBorder]

initState = buildState(ballStart, paddleStart, brickStart(),0,0,[],[],0)
deadState = buildState(ballDead, paddleStart, brickStart(), False, True, [], [], 0)
winState = buildState(ballDead, paddleStart, [], True, False, [], [], 0)

def init():
    global S
    S = buildState(ballStart, paddleStart, brickStart(),0,0,[],[],0)

def windowDimensions():
    return(1100,800)

def update():
    global S
    ballMove= sClean(sHelper(motionHelper(S)))
    paddleMoveL = paddleHelper(ballMove, False)
    paddleMoveR = paddleHelper(ballMove, True)
    S = winState if len(S[2])==0 else \
            initState if clickReset() else \
            deadState if deadthCollide(S[0]) else \
            paddleMoveR if rightDown() else \
            paddleMoveL if leftDown() else \
            ballMove 

def leftDown():
    return K_LEFT in keysDown or K_a in keysDown
def rightDown():
    return K_RIGHT in keysDown or K_d in keysDown
def sounds():
    global S
    if S == deadState:
        return [BOING]
    if S == winState:
        return [BANG]
    if collided():
        return [DING]
    if brickCollide(S[0],S[1]) in ["b","v","h"]:
        return [BANG]
def collided():
    global S
    tempB=S[0]
    for brick in S[2]:
        if brickCollide(tempB,brick) in ["b","v","h"]:
            return True
    return False

def mouseClick():
    return mouseDown and not oldMouseDown

def clickReset():
    clicked = mouseClick()
    click = mouseX, mouseY
    return clicked and inBox(click,point(-500,400),point(-300,400),point(-500,300),point(-300,300))

def inBox(click,topL,topR,botL,botR):
    x=click[0]
    y=click[1]
    return x>topL[0] and x>botL[0] and x<topR[0] and x<botR[0] and y>botR[0] and y>botL[1] and y<topR[1] and y<topL[1] 
def equalList(keys,char):
    return len(keys)>0 and keys[0]==char

def paddleHelper(S,flag):
    nextPaddle = paddleMove(S[1],flag)
    return buildState(S[0],nextPaddle,S[2],S[3],S[4],S[5],S[6],S[7]) 

def paddleMove(pad,flag):
    l=outOfBoundsL(pad[0])
    r = outOfBoundsR(pad[1])
    TL=nextPaddle(pad[0],flag,l,r)
    TR=nextPaddle(pad[1],flag,l,r)
    BL = nextPaddle(pad[2],flag,l,r)
    BR = nextPaddle(pad[3],flag,l,r)
    return paddle(TL,TR,BL,BR) 

def nextPaddle(p,flag,l,r):
    nextX = nextPX(p,flag,l,r)
    return point(nextX,p[1])

def nextPX(p,flag,l,r):
    val=20
    return p[0]+val if flag and not r else \
    p[0]-val if not flag and not l else \
    p[0]

def outOfBoundsL(p):
    return p[0]<=-100
def outOfBoundsR(p):
    return p[0] >=500

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
    return (box[0][0] <= -100) or (box[1][0] >= 500) or \
		(nBox[0][0] <= -100) or (nBox[1][0] >= 500)
def hWallCollide(B):
    box=ballBox(B) 
    nBox=ballBox(B)
    return (box[2][1] <= -400) or (box[1][1] >= 400) or \
		(nBox[2][1] <= -400) or (nBox[1][1] >= 400)

def deadthCollide(B):
    box=ballBox(B)
    nBox=ballBox(ballMove(B))
    return box[2][1]<=-400 or nBox[2][1]<=-400

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

def pCollide(B,brick):
    return "b" if cornerCollision(ballMove(B), brick) or cornerCollision(B, brick) else \
        "v" if (vCollision(ballMove(B), brick) or vCollision(B, brick)) else \
        "h" if (hCollision(ballMove(B), brick) or hCollision(B, brick)) else \
        "n"

def vCollision(B,L):
    box = ballBox(B)
    bTop = box[0][1]
    bBot = box[3][1]
    bLeft = box[2][0]
    bRight = box[1][0]
    rTop = L[0][1]
    rBot = L[3][1]
    rLeft = L[2][0]
    rRight = L[1][0]
    return ((bTop >= rBot and bBot < rBot) or (bBot <= rTop and bTop > rTop)) and (between(rLeft, rRight, range(bLeft,bRight)))

def hCollision(B,L):
    box = ballBox(B)
    bTop = box[0][1]
    bBot = box[3][1]
    bLeft = box[2][0]
    bRight = box[1][0]
    rTop = L[0][1]
    rBot = L[3][1]
    rLeft = L[2][0]
    rRight = L[1][0]
    return ((bRight >= rLeft and bLeft < rLeft) or (bLeft <= rRight and bRight > rRight)) and between(rBot, rTop, range(bBot,bTop))
def cornerCollision(B,L):
    return vCollision(B,L) and hCollision(B,L)
def between(bot,top,vals):
    return any([x<=top and x>=bot for x in vals])

def ballBox(B):
    return (point(B[0][0]-B[1],B[0][1]+B[1]),point(B[0][0]+B[1],B[0][1]+B[1]), point(B[0][0]-B[1],B[0][1]-B[1]), point(B[0][0]+B[1],B[0][1]-B[1]))

def motionHelper(S):
    tempB=S[0]
    deadBricks=None
    for brick in S[2]:
        if brickCollide(tempB,brick) in ["b","v","h"]:
            deadBricks=brick
            break
    if not deadBricks==None:
        S[2].remove(deadBricks)
    return buildState(ballMove(nextBall(S)), S[1], S[2], S[3], S[4], S[5],S[6],S[7]+1)

def sHelper(S):
    return S

def sClean(S):
    return (S[0],S[1],S[2],S[3],S[4],S[5],S[6],S[7]+1)
def display():
    global S
    return staticImgs + ballImg(S[0]) +padImg(S[1]) + brImg(S[2]) if not S[4] and not S[3] else \
            staticImgs + [txt("You win",point(215,0),65,dBlue)]  if S[3] else \
            staticImgs + [txt("You died",point(215,0),65,dRed)]

def ballImg(b):
    p=b[0]
    r=b[1]
    c=dViolet
    return [disc(p,r,c)]

def padImg(pad):
    return boxImg(pad,dBlue)

def boxImg(L,c):
    TL=L[0]
    TR=L[1]
    BL=L[2]
    BR=L[3]
    return [ftri(TL, BR, BL, c), ftri(TL, TR, BR, c),seg(TL,TR,dBlack),seg(TL, BL, dBlack), seg(BL, BR, dBlack), seg(TR, BR, dBlack)]

def brImg(B):
    bricks = []
    for br in B:
        bricks = bricks+ boxImg(br,dOrange)
    return bricks

def sImg(dust):
    return [] if len(dust)==0 else disc(dust[2],dust[3],dRed)
