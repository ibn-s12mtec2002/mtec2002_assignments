#import turtle.
#import random
#print question do you like hearts yes or no?
#create a variable named hearts set it raw_input. 
#create for loop that iterates range 50.
#for each iteration  draw a heart using turtle.

#set color to random for each heart drawn.


import random
import turtle
draw = 0
print "Do you Like hearts yes or no"
hearts = raw_input("> ");
if hearts == "yes" or  hearts == "yeah":
	for x in range(25):
		turtle.pencolor("pink")
		xpos = random.randint(-300,300)
		ypos =random.randint(-300,300)
		turtle.up()
		turtle.goto(xpos,ypos)
		turtle.left(135)
		turtle.down()
		turtle.forward(100)
		turtle.circle(-75,180)
		turtle.up()
		turtle.goto(xpos,ypos)
		turtle.left(70)
		turtle.down()
		turtle.forward(100)
		turtle.circle(75,180)
		turtle.fillcolor("blue")
turtle.mainloop()
	
#turtle.color(blue)
#turtle_x = turtle.position(x,y)
#if turtle_x == turtle.color():
#turtle.goto(-turtle.position)
#class Pen();
#window_width = 500 px;
#window_height = 500 px;
	
	
	

	