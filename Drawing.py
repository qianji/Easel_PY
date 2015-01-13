############################################################################
# Easel_Python
# 
# by Qianji Zheng
# Texas Tech Dept. of Computer Science
# January 3, 2015

import pygame

# ScreenSize is the ScreenSize of the display window, (width, height)

def isPoint(I):
    '''image -> bool
    '''
    # extact the tuple from the LED point
    W,H=ScreenSize
    if isinstance(I,tuple):
        point = I
        if len(point)==2:
            x=point[0]
            y=point[1]
            return x >= -W/2 and x<=W/2 and y>=-H/2 and y<=H/2
    return False

def isColor(I):
    if isinstance(I,tuple):
        color = I
        if len(color)==3:
            return all(0<=c and c<=256 for c in color)
    return False

def isSegment(I):
    if isinstance(I,tuple):
        segment = I
        if len(segment)==4:
            t,p,q,c=segment
            return t=="seg" and isPoint(p) and isPoint(q) and isColor(c)
    return False

def isTriangle(I):
    if isinstance(I,tuple):
        triangle = I
        if len(triangle)==5:
            t,p,q,r,c=triangle
            return t=="fTri" and isNonCollinear(p,q,r) and isColor(c)
    return False

def isNonCollinear(p,q,r):
    if isPoint(p) and isPoint(q) and isPoint(r):
        return not slope(p,q)==slope(q,r)
    return False

def slope(p,q):
    if isPoint(p) and isPoint(q):
        (px,py)=p
        (qx,qy)=q
        if not px-qx==0:
            return float(py-qy)/float(px-qx)
        else:
            return None

def isCircle(I):
    if isinstance(I,tuple):
        circle = I
        if len(circle)==4:
            t,p,r,c=circle
            return t=="circ" and isPoint(p) and isinstance(r,int) and r>0 and isColor(c)
    return False

def isDisc(I):
    if isinstance(I,tuple):
        circle = I
        if len(circle)==4:
            t,p,r,c=circle
            return t=="disc" and isPoint(p) and isinstance(r,int) and r>0 and isColor(c)
    return False

def isText(I):
    if isinstance(I,tuple):
        text = I
        if len(text)==5:
            t,s,p,n,c=text
            return t=="txt" and isinstance(s,str) and isPoint(p) and isColor(c) and isinstance(n,int) and n in range(4,101)
    return False

def isClick(C):
    return isPoint(C) or C==None

def drawSegment(screen,L):
    tup,(x1,y1),(x2,y2),color=L
    W,H=ScreenSize
    p1 = [x1+W/2,H/2-y1]
    p2 = [x2+W/2,H/2-y2]
    pygame.draw.line(screen, tuple(color), p1,p2, 2)

def drawCircle(screen,C):
    tup,(x,y),radius,color= C
    x=int(x)
    y=int(y)
    W,H=ScreenSize
    center = [x+W//2,H//2-y]
    pygame.draw.circle(screen, tuple(color), center, radius,1)

def drawDisc(screen,C):
    tup,(x,y),radius,color= C
    x=int(x)
    y=int(y)
    W,H=ScreenSize
    center = [x+W//2,H//2-y]
    pygame.draw.circle(screen, tuple(color), center, radius,0)

def drawText(screen,Text):
    (tup,string,center,fontScreenSize,color) = Text
    [x,y]= center
    # (0,0) is left botton
    W,H=ScreenSize    
    y=H/2-y
    x=W/2+x
    #string = prettyString(string)
    T = string
    if pygame.font:
        font = pygame.font.Font(None, fontScreenSize)
        text = font.render(T, 1, color)
        textpos = text.get_rect(centerx=int(x),centery=int(y))
        #screen.blit(text, [x,y])
        screen.blit(text, textpos)

def drawTriangle(screen,Tri):
    tup,p,q,r,color= Tri
    W,H=ScreenSize
    p=(p[0]+W/2,H/2-p[1])
    q=(q[0]+W/2,H/2-q[1])
    r=(r[0]+W/2,H/2-r[1])
    pygame.draw.polygon(screen, tuple(color), [p,q,r], 0)

def drawImages(screen,images,s):

    # Define the colors we will use in RGB format

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    global ScreenSize
    ScreenSize = s
    WHITE = (255,255,255)
    screen.fill(WHITE)
    #print(images)
    for x in images:
        #draw segment
        if isSegment(x): 
            drawSegment(screen,x)
        # draw circle
        elif isCircle(x): drawCircle(screen,x)
        elif isDisc(x): drawDisc(screen,x)
        elif isText(x): drawText(screen,x)
        elif isTriangle(x): drawTriangle(screen,x)

    ## Draw a rectangle outline
    #pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
     
    ## Draw a solid rectangle
    #pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
     
    ## Draw an ellipse outline, using a rectangle as the outside boundaries
    #pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 

    ## Draw an solid ellipse, using a rectangle as the outside boundaries
    #pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])   

