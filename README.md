# Easel_PY
Easel is an engine for creating real time games.This version, EaselPY, allows the programmer to create games by writing Python code, and runs on Windows or Mac OS. 

# The Tiny Python Game Engine
The tiny Python game engine (TPGE) is a simple piece of Python code which, when combined with Peter Zelle's graphics library and code supplied by a student-developer, creates an interactive GUI program (typically a simple game, hence the name) that runs in a 600 by 500 pixel window. 

While Python is (unfortunately) an untyped langauge, the use of TPGE requires the programmer to use the following data model. This is not Python code, but specifies an understanding of how certain Python data structures are to  be intuitively interpreted: 

- A point is a pair (x,y) of integers where 0 ≤ x ≤ 600 and 0≤ y ≤ 500. 
- A line segment is a 4-tuple (x1,y1,x2,y2) of integers where 0 ≤ x1, x2 ≤ 600 and 0≤ y1, y2≤ 500. Intuitively, it is the line segment   connecting the points (x1,y1) and (x2,y2) in the coordinate system whose origin is the lower left corner of the display screen. 
- A Circle is a triple (x,y,R) where (x,y) is a point and R is an integer. It is thought of as the circle whose center is (x,y) and whose radius is R, in the coordinate system whose origin is the lower left corner of the display screen. 
- A displayText is 4-tuple (c,x,y,s) where c is a string, x and y are nonnegative integers, and s is an integer in the interval [5,37). Intuitively, displayText (c,x,y,s) is the image of a text string, centered at point (x,y) of height s in pixels.
- An image is a line segment, a circle, or a displayText. 
- An imageList is a list of images.
- A state is whatever sort of Python data structure the student-developer wants it to be -- but they should be clear in their mind about it.

The student-supplied functions consist of the following three functions, along with any helpers necessary to implement them:
- initialState : state --InitialState() is the initial state of the program.
- successor: state x point  → state -- successor(S,p) is the state resulting from clicking point p in state S
- displayImages: state  → imageList -- displayImages(S) is a list containing the images to be displayed on the screen in program state S. Images occurring later in the list overwrite images that occur earlier if they overlap. 

Below is an example of a trivial game created using the engine, followed by code for the game engine itself. It should run if you have Python 3.x and  graphics.py installed. 
