from graphics import *
from time import *
# Create a window of a suitable size
window = GraphWin("Visualisation", 500, 500)
data=[52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54 ]

y=100
x=100
yspeed=10   
xspeed=10

while True:
    for item in data:

# Create and draw a circle

      #  if x<499: x=x+5 
       # if y<499: y=y+5
            
        
       
        ball = Circle(Point(x,y), item)
        ball.setFill(color_rgb(255,255,0))
        y=y+yspeed
        x=x+xspeed
        ball.draw(window)
        sleep(0.2)
        ball.undraw()
        if y>= 490:
            yspeed=-25
        if y<=10:
            yspeed=25
        if x>= 490:
            xspeed=-25
        if x<=10:
            xspeed=25
 #Create and draw a rectangle
        box = Rectangle(Point(item,item),Point(x,y))
        box.setOutline(color_rgb(0,0,0))
        box.setFill(color_rgb(150,item,item))
        box.draw(window)
        


# Wait until the mouse is clicked before closing the window
window.getMouse()