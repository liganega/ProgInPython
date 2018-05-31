#SpaceWar by @TokyoEdTech / Written in Python 2.7
#Part I: Getting Started

import os
import random

#Import the Turtle module
import turtle
#Set the animations speed to the maximum
# turtle.speed(0)
#Hide the default turtle
# turtle.hideturtle()
#This saves memory
turtle.setundobuffer(1)

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.showturtle()
		self.speed = 1
		# self.pendown()


wn = turtle.Screen()
#Change the background color
wn.bgcolor("black")
#This speeds up drawing
wn.tracer(1)

#Create my sprites
player = Sprite("triangle", "white", 0, 0)

player.forward(100)

wn.mainloop()




# delay = raw_input("Press enter to finish. > ")
