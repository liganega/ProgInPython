#Turtle Review
import turtle
turtle.fd(0)
turtle.bgcolor("black")


class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.color(color)
		self.penup()
		self.goto(startx, starty)
		self.speed = 1
		
	def move(self):
		self.fd(self.speed)
		
	def turn_left(self):
		self.lt(45)

	def turn_right(self):
		self.rt(45)
		
	def accelerate(self):
		self.speed += 1

	def decelerate(self):
		self.speed -= 1


player = Sprite("triangle", "white", 0, 0)
player2 = Sprite("triangle", "green", 100, 0)
player3 = Sprite("triangle", "red", -100, 0)


#Keyboard Bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

while True:
	player.move()
	player2.move()
	player3.move()

delay = raw_input("Press enter to finish. >")