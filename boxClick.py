def init():
    global S,windowDimensions
    windowDimensions = (1000,800)
    S=1
def output():
    global S
    return background()+line(S)
   
def background():
    global windowDimensions
    W,H = windowDimensions
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
    return ("seg",p,r,c)

def update(IN):
    global S
    p = IN.mouseX,IN.mouseY
    if p[0]==None and p[1]==None: return
    if inLeftBox(p): S=1
    if inRightBox(p): S=2

def line(S):
    if S==2: return [segment(300,300,400,200)]
    if S==1: return [segment(200,300,300,200)]

def inLeftBox(p):
    (x,y) = p
    return x<300 and x>200 and y<300 and y>200

def inRightBox(p):
    (x,y) = p
    return x>300 and x<400 and y<300 and y>200




