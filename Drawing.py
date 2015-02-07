############################################################################
# Easel_Python
# 
# by Qianji Zheng
# Texas Tech Dept. of Computer Science
# January 3, 2015

import pygame,os
# use a global image library to store the images to prevent reloading for performance purpose
_image_library={}

# draw the list of images to screen 
def drawImages(screen,images):
    WHITE = (255,255,255)
    screen.fill(WHITE)
    for x in images:
        if x.isDrawable(screen):
            x.draw(screen)
        else:
            print("error drawing",x)
def isPoint(I,screen):
    '''image * surface -> bool
    '''
    # extact the tuple from the LED point
    W,H=screen.get_size()
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

class Image:
    '''
    An image is  a segment, circle, filled triangle, text image, disc or an image loaded from a file. 
    Image should be written as a polymorphic class, with a different draw function for each kind of image. 
    '''
    def __init__(self):
        pass
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def isDrawable(self,screen):
        raise NotImplementedError("Subclass must implement abstract method")

class seg(Image):
    '''
    A segment is written seg( p,q,C) where p and q are points, interpreted as the endpoints of the segment, and C is a color. 
    '''
    def __init__(self,p,q,c):
        self.category = "seg"
        self.start = p
        self.end = q
        self.color = c

    def draw(self,screen):
        (x1,y1),(x2,y2),color= self.start, self.end,self.color
        W,H=screen.get_size()
        p1 = [x1+W/2,H/2-y1]
        p2 = [x2+W/2,H/2-y2]
        pygame.draw.line(screen, tuple(color), p1,p2, 2)

    def isDrawable(self,screen):
        return isPoint(self.start,screen) and isPoint(self.end,screen) and isColor(self.color)
    
class circ(Image):
    '''
    A circle is written circ( p, r, C)  where p is a point, r is a positive integer, and C is a color. 
    We interpret p and r as the center and radius of the circle, respectively.
    '''
    def __init__(self,p,r,c):
        self.category = "circ"
        self.center = p
        self.radius = r
        self.color = c
    def draw(self,screen):
        (x,y),radius,color= self.center, self.radius,self.color
        x=int(x)
        y=int(y)
        W,H=screen.get_size()
        center = [x+W//2,H//2-y]
        pygame.draw.circle(screen, tuple(color), center, radius,1)
    def isDrawable(self,screen):
        return isPoint(self.center,screen) and isinstance(self.radius,int) and self.radius>0 and isColor(self.color)
        
class disc(Image):
    '''
    A Disc is written disc(p, r, C)   where p is a point, r is a positive integer, and C is a color.
    We interpret p and r as the center and radius of the circle, respectively.
    '''
    def __init__(self,p,r,c):
        self.category = "disc"
        self.center = p
        self.radius = r
        self.color = c
    def draw(self,screen):
        (x,y),radius,color= self.center, self.radius,self.color
        x=int(x)
        y=int(y)
        W,H=screen.get_size()
        center = [x+W//2,H//2-y]
        pygame.draw.circle(screen, tuple(color), center, radius,0)
    def isDrawable(self,screen):
        return isPoint(self.center,screen) and isinstance(self.radius,int) and self.radius>0 and isColor(self.color)        
    def __str__(self):
        return "disc("+str((self.center)) +","+ str(self.radius) + ")"
class txt(Image):
    '''
    A text image is written txt(S, p, n, C) where S is a string, p a point, n integer in [4,100], and C is a color.
    The text image  txt(S, p, n, C)  represents the text string S, displayed with height n centered at p with  color C.
    '''
    def __init__(self,s,p,n,c):
        self.category = "txt"
        self.text = s
        self.center = p
        self.height = n
        self.color = c
    def draw(self,screen):
        string,center,fontScreenSize,color = self.text,self.center,self.height,self.color
        [x,y]= center
        # (0,0) is left botton
        W,H=screen.get_size()
        y=H/2-y
        x=W/2+x
        T = string
        if pygame.font:
            font = pygame.font.Font(None, fontScreenSize)
            text = font.render(T, 1, color)
            textpos = text.get_rect(centerx=int(x),centery=int(y))
            #screen.blit(text, [x,y])
            screen.blit(text, textpos)
    def isDrawable(self,screen):
        return isinstance(self.text,str) and isPoint(self.center,screen) and isColor(self.color) and isinstance(self.height,int) and self.height in range(4,101)

class ftri(Image):
    '''
    A filled triangle is written ftri( p, q, r, C) where p, q, and r are points and C is a color. 
    The filled triangle ftri(p, q, r, C), where p, q, and r are noncollinear points and C is a color, represents the filled triangle with vertices p, q, and r, of color C.
    '''
    def __init__(self,p,q,r,c):
        self.category = "fTri"
        self.v1 = p
        self.v2 = q
        self.v3 = r
        self.color = c
    def draw(self,screen):
        p,q,r,color= self.v1,self.v2,self.v3,self.color
        W,H=screen.get_size()
        p=(p[0]+W/2,H/2-p[1])
        q=(q[0]+W/2,H/2-q[1])
        r=(r[0]+W/2,H/2-r[1])
        pygame.draw.polygon(screen, tuple(color), [p,q,r], 0)

    def isDrawable(self,screen):
        return self.isNonCollinear(self.v1,self.v2,self.v3,screen) and isColor(self.color)
    
    def isNonCollinear(self,p,q,r,screen):
        if isPoint(p,screen) and isPoint(q,screen) and isPoint(r,screen):
            return not self.slope(p,q,screen)==self.slope(q,r,screen)
        return False
    def slope(self,p,q,screen):
        if isPoint(p,screen) and isPoint(q,screen):
            (px,py)=p
            (qx,qy)=q
            if not px-qx==0:
                return float(py-qy)/float(px-qx)
            else:
                return None

class loadImageFile(Image):
    '''
    A file image is a triple (x,m,n) where x is an image loaded from a file and m and n are integers. 
    '''
    def __init__ (self,name,x,y):
        self.category = "load"
        self.image = self.get_image(name)
        self.pos = (x,y)
        
    def get_image(self,name):
        global _image_library
        image = _image_library.get(name)
        if image == None:
            fullname = os.path.join('images', name)        
            image = pygame.image.load(fullname)
            _image_library[name] = image
        return image

    def draw(self,screen):
        image,p = self.image,self.pos
        W,H=screen.get_size()
        p=(p[0]+W/2,H/2-p[1])
        screen.blit(image,p)

    def isDrawable(self,screen):
        return isinstance(self.image,pygame.Surface) and isPoint(self.pos,screen)
    

