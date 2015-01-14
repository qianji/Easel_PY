from EaselLib import *

def windowDimensions():
    return (800,600)
def init():
    global S
    S=1
def display():
    return background()+line()
   
def sounds():
    if leftBoxClicked():
        return [BOING]
    if rightBoxClicked():
        return [BOING,CLAP]
    if mouseClicked():
        return [CLICK]
    else:
        return []
def background():
    W,H = windowDimensions()
    L1 = segment(200,200,200,300)
    L2 = segment(400,200,400,300)
    L3 = segment(200,300,400,300)
    L4 = segment(200,200,400,200)
    L5 = segment(300,200,300,300)
    L6 = segment(-W//2,0,W//2,0)
    L7= segment(0,H//2,0,-H//2)
    return [L1,L2,L3,L4,L5,L6,L7]

def segment(x1,y1,x2,y2):
    p=(x1,y1)
    r=(x2,y2)
    c=(0,0,0)
    return seg(p,r,c)

def update():
    global S
    if leftBoxClicked(): S=1
    if rightBoxClicked(): S=2


def mouseClicked(): 
    return mouseDown and not oldMouseDown

def line():
    if S==2: return [segment(300,300,400,200)]
    if S==1: return [segment(200,300,300,200)]

def leftBoxClicked():
    click = mouseClicked()
    (x,y) = mouseX,mouseY
    return click and x<300 and x>200 and y<300 and y>200
    (x,y) = mouseX,mouseY
def rightBoxClicked():
    click = mouseClicked()
    (x,y) = mouseX,mouseY
    return click and x>300 and x<400 and y<300 and y>200
