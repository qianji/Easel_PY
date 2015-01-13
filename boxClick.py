def windowDimensions():
    return (1000,800)
def init():
    global S
    S=1

def display():
    global S
    return background()+line(S)
   
def sounds(IN):
    if leftBoxClicked(IN):
        return ["boing"]
    if rightBoxClicked(IN):
        return ["boing","clap"]
    if mouseClicked(IN):
        return ["click"]
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
    return ("seg",p,r,c)

def update(IN):
    global S
    if leftBoxClicked(IN): S=1
    if rightBoxClicked(IN): S=2


def mouseClicked(IN): 
    return IN.mouseDown and not IN.oldMouseDown

def line(S):
    if S==2: return [segment(300,300,400,200)]
    if S==1: return [segment(200,300,300,200)]

def leftBoxClicked(IN):
    click = mouseClicked(IN)
    (x,y) = IN.mouseX, IN.mouseY
    return click and x<300 and x>200 and y<300 and y>200

def rightBoxClicked(IN):
    click = mouseClicked(IN)
    (x,y) = IN.mouseX,IN.mouseY
    return click and x>300 and x<400 and y<300 and y>200
