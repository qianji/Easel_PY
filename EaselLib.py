import pygame,os
import sys


#######################################################################################
# Begin Define functions and class for image drawing
#######################################################################################

# use a global image library to store the images to prevent reloading for performance purpose
_image_library={}

# draw the list of images to the screen 
def drawImages(screen,images):
    WHITE = (255,255,255)
    screen.fill(WHITE)
    for x in images:
        if x.isDrawable(screen):
            x.draw(screen)
        else:
            print("Error drawing",x)
            pygame.quit()

# isPoint(point,screen) is true iff point is a point in the screen's dimension
def isPoint(point,screen):
    '''image * surface -> bool
    A point a pair (x,y)  where x and y are integers. 
    The point (x,y) is thought of in a coordinate plane with (0,0) in the center of the game screen, the x-axis point right and y axis pointing up. 
    '''
    W,H=screen.get_size()
    if isinstance(point,tuple):
        if len(point)==2:
            x=point[0]
            y=point[1]
            return x >= -W/2 and x<=W/2 and y>=-H/2 and y<=H/2
    return False

# A color is written (R,G,B) where R, G, and B are integers and 0 ≤ R,G,B ≤ 255
def isColor(color):
    if isinstance(color,tuple):
        if len(color)==3:
            return all(0<=c and c<=256 for c in color)
    return False

##############
# define images class and its sub-class
##############
class Image:
    '''
    An image is  a segment, circle, filled triangle, text image, disc or an image loaded from a file. 
    Image should be written as a polymorphic class, with a different draw function for each kind of image. 
    '''
    def __init__(self):
        pass
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")
    # check to see if the image can be drawed in the screen
    def isDrawable(self,screen):
        raise NotImplementedError("Subclass must implement abstract method")

class seg(Image):
    '''
    A segment is written seg( p,q,C) where p and q are points, interpreted as the endpoints of the segment, and C is a color. 
    '''
    def __init__(self,p,q,c):
        self.category = "seg"
        self.start = p # the start endpoint of the segment
        self.end = q # the end endpoint of the segment
        self.color = c # the color of the segment

    def draw(self,screen):
        (x1,y1),(x2,y2),color= self.start, self.end,self.color
        W,H=screen.get_size()
        p1 = [x1+W/2,H/2-y1]
        p2 = [x2+W/2,H/2-y2]
        pygame.draw.line(screen, tuple(color), p1,p2, 2)

    def isDrawable(self,screen):
        return isPoint(self.start,screen) and isPoint(self.end,screen) and isColor(self.color)
    
    def __str__(self):
        return "seg(" + str(self.start) + "," + str(self.end) + ")"
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
        
    def __str__(self):
        return "circ(" + str(self.center) + "," + str(self.radius)+")"
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
    def __str__(self):
        return "ftri(" + str(self.v1) + "," + str(self.v2)+ "," + str(self.v3)+")"

class fileImg(Image):
    '''
    A file image is written fileImg (x,m,n) where x is an image loaded from a file and m and n are integers.
    The point (m,n) is coordinate of the top-left pixel of the image
    '''
    def __init__ (self,img,pos):
        self.category = "fileImg"
        self.image = img
        self.pos = pos
        
    def draw(self,screen):
        image,p = self.image,self.pos
        W,H=screen.get_size()
        p=(p[0]+W/2,H/2-p[1])
        screen.blit(image,p)

    def isDrawable(self,screen):
        return isinstance(self.image,pygame.Surface) and isPoint(self.pos,screen)

    def __str__(self):
        return "fileImg(" + self.image +","+ str(self.pos) + ")"

# load the image from the file under the sub-directory named 'media', 
def loadImageFile(name):
    global _image_library
    image = _image_library.get(name)
    if image == None:
        fullname = os.path.join('media', name)
        try:
            image = pygame.image.load(fullname)
            _image_library[name] = image
        except:
            print("Cannot load images: ",fullname)
            pygame.quit()
    return image

#######################################################################################
# Begin Define functions and class for sound playing
#######################################################################################
import pygame.mixer, pygame.time
time = pygame.time
mixer = pygame.mixer
mixer.init(frequency=11025, size=-16, channels=2,buffer=512)
#mixer.init(11025)
main_dir = os.path.split(os.path.abspath(__file__))[0]

# use a global sound library to store the sound
_sound_library={}
def playSounds(S):
    if S==None:
        return
    for sound in S:
        if not sound==None:
            channel = sound.play(loops=0, maxtime=0, fade_ms=0)

# check to see the sound is already loaded before loading
def loadSoundFile(name):
    global _sound_library
    sound = _sound_library.get(name)
    if sound ==None:
        try:
            file_path = os.path.join(main_dir,'media',name)
            sound = mixer.Sound(file_path)
            _sound_library[name] = sound
        except:
            print("Cannot load sound: ", file_path)
            pygame.quit()
    return sound

def playBackGroundMusic(name):
    if pygame.mixer:
        music = os.path.join(main_dir, 'media', name)
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        
def playSound(s):
    if s==None:
        return
    channel = s.play(loops=0, maxtime=0, fade_ms=0)


####################################################
# Begin defining global variables
####################################################
# default sounds for the game engine
DING = loadSoundFile("ding.wav")
BANG = loadSoundFile("bang.wav")
BOING =loadSoundFile("boing.wav")
CLAP = loadSoundFile("clap.wav")
CLICK = loadSoundFile("click.wav")

# define global varibale for keyboard and mouse action
mouseDown =None
mouseX = None
mouseY = None
keysDown = None
oldKeysDown = None 
oldMouseDown = None
keysPressed = None

# define key
# A key is an integer. Keys are named by global variables which are imported with EaselLib.py, given in the first column of the following table:
K_BACKSPACE  = pygame.K_BACKSPACE   
K_TAB        = pygame.K_TAB         
K_CLEAR      = pygame.K_CLEAR               
K_RETURN     = pygame.K_RETURN      
K_PAUSE      = pygame.K_PAUSE               
K_ESCAPE     = pygame.K_ESCAPE      
K_SPACE      = pygame.K_SPACE               
K_EXCLAIM    = pygame.K_EXCLAIM     
K_QUOTEDBL   = pygame.K_QUOTEDBL    
K_HASH       = pygame.K_HASH        
K_DOLLAR     = pygame.K_DOLLAR      
K_AMPERSAND  = pygame.K_AMPERSAND   
K_QUOTE      = pygame.K_QUOTE               
K_LEFTPAREN  = pygame.K_LEFTPAREN   
K_RIGHTPAREN = pygame.K_RIGHTPAREN  
K_ASTERISK   = pygame.K_ASTERISK    
K_PLUS       = pygame.K_PLUS        
K_COMMA      = pygame.K_COMMA       
K_MINUS      = pygame.K_MINUS       
K_PERIOD     = pygame.K_PERIOD      
K_SLASH      = pygame.K_SLASH       
K_0          = pygame.K_0           
K_1          = pygame.K_1           
K_2          = pygame.K_2           
K_3          = pygame.K_3           
K_4          = pygame.K_4           
K_5          = pygame.K_5           
K_6          = pygame.K_6           
K_7          = pygame.K_7           
K_8          = pygame.K_8           
K_9          = pygame.K_9           
K_COLON      = pygame.K_COLON       
K_SEMICOLON  = pygame.K_SEMICOLON   
K_LESS       = pygame.K_LESS        
K_EQUALS     = pygame.K_EQUALS      
K_GREATER    = pygame.K_GREATER     
K_QUESTION   = pygame.K_QUESTION    
K_AT         = pygame.K_AT          
K_LEFTBRACKET= pygame.K_LEFTBRACKET 
K_BACKSLASH  = pygame.K_BACKSLASH   
K_RIGHTBRACKET= pygame.K_RIGHTBRACKET 
K_CARET      = pygame.K_CARET       
K_UNDERSCORE = pygame.K_UNDERSCORE  
K_BACKQUOTE  = pygame.K_BACKQUOTE   
K_a          = pygame.K_a          
K_b          = pygame.K_b          
K_c          = pygame.K_c          
K_d     = pygame.K_d      
K_e         = pygame.K_e          
K_f          = pygame.K_f           
K_g          = pygame.K_g           
K_h          = pygame.K_h           
K_i          = pygame.K_i           
K_j          = pygame.K_j           
K_k          = pygame.K_k           
K_l          = pygame.K_l           
K_m          = pygame.K_m           
K_n          = pygame.K_n           
K_o          = pygame.K_o           
K_p          = pygame.K_p           
K_q          = pygame.K_q           
K_r          = pygame.K_r           
K_s          = pygame.K_s           
K_t          = pygame.K_t           
K_u          = pygame.K_u           
K_v          = pygame.K_v           
K_w          = pygame.K_w           
K_x          = pygame.K_x           
K_y          = pygame.K_y           
K_z          = pygame.K_z           
K_DELETE     = pygame.K_DELETE              
K_KP0        = pygame.K_KP0                 
K_KP1                = pygame.K_KP1                 
K_KP2                = pygame.K_KP2                 
K_KP3                = pygame.K_KP3                 
K_KP4                = pygame.K_KP4                 
K_KP5                = pygame.K_KP5                 
K_KP6                = pygame.K_KP6                 
K_KP7                = pygame.K_KP7                 
K_KP8                = pygame.K_KP8                 
K_KP9                = pygame.K_KP9                 
K_KP_PERIOD  = pygame.K_KP_PERIOD   
K_KP_DIVIDE  = pygame.K_KP_DIVIDE   
K_KP_MULTIPLY= pygame.K_KP_MULTIPLY 
K_KP_MINUS   = pygame.K_KP_MINUS    
K_KP_PLUS    = pygame.K_KP_PLUS     
K_KP_ENTER   = pygame.K_KP_ENTER    
K_KP_EQUALS  = pygame.K_KP_EQUALS   
K_UP                 = pygame.K_UP                  
K_DOWN               = pygame.K_DOWN                
K_RIGHT              = pygame.K_RIGHT               
K_LEFT               = pygame.K_LEFT                
K_INSERT             = pygame.K_INSERT              
K_HOME               = pygame.K_HOME                
K_END                = pygame.K_END                 
K_PAGEUP             = pygame.K_PAGEUP              
K_PAGEDOWN           = pygame.K_PAGEDOWN            
K_F1                 = pygame.K_F1                  
K_F2                 = pygame.K_F2                  
K_F3                 = pygame.K_F3                  
K_F4                 = pygame.K_F4                  
K_F5                 = pygame.K_F5                  
K_F6                 = pygame.K_F6                  
K_F7                 = pygame.K_F7                  
K_F8                 = pygame.K_F8                  
K_F9                 = pygame.K_F9                  
K_F10                = pygame.K_F10                 
K_F11                = pygame.K_F11                 
K_F12                = pygame.K_F12                 
K_F13                = pygame.K_F13                 
K_F14                = pygame.K_F14                 
K_F15                = pygame.K_F15                 
K_NUMLOCK            = pygame.K_NUMLOCK             
K_CAPSLOCK           = pygame.K_CAPSLOCK            
K_SCROLLOCK          = pygame.K_SCROLLOCK           
K_RSHIFT             = pygame.K_RSHIFT              
K_LSHIFT             = pygame.K_LSHIFT              
K_RCTRL              = pygame.K_RCTRL               
K_LCTRL              = pygame.K_LCTRL               
K_RALT               = pygame.K_RALT                
K_LALT               = pygame.K_LALT                
K_RMETA              = pygame.K_RMETA               
K_LMETA              = pygame.K_LMETA               
K_LSUPER             = pygame.K_LSUPER              
K_RSUPER             = pygame.K_RSUPER              
K_MODE               = pygame.K_MODE                
K_HELP               = pygame.K_HELP                
K_PRINT              = pygame.K_PRINT               
K_SYSREQ             = pygame.K_SYSREQ              
K_BREAK              = pygame.K_BREAK               
K_MENU               = pygame.K_MENU                
K_POWER              = pygame.K_POWER               
K_EURO               = pygame.K_EURO                

