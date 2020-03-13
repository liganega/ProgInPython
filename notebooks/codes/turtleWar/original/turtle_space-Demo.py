#Simple Turtle Graphics Game
#By @TokyoEdTech
#Python 2.7
import os
import random
# import tkMessageBox      						# for Python 2
import tkinter.messagebox as tkMessageBox		# for Python 3
import time
import math

#Import the turtle module
import turtle
#Change the window size
turtle.setup(800, 800)
#Required on Mac to create turtle window
turtle.fd(0)
#Max animation speed
turtle.speed(0)
#Change the background color of the screen
turtle.bgcolor("black")
#Load the background image
turtle.bgpic("splash-screen.gif")
#Set the window title
turtle.title("SpaceWar")
#Hide the turtle
turtle.ht()
#Set the undo buffer to 1 (to save memory and speed things up)
turtle.setundobuffer(1)
#Speed up drawing (Draw every 6 frames)
turtle.tracer(0)

#Register shapes
turtle.register_shape("enemy.gif")
turtle.register_shape("enemybase.gif")
turtle.register_shape("allybase.gif")
turtle.register_shape("ally.gif")

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 0

	def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and \
			(self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() - 20)) and \
			(self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False

	def move(self):
		self.fd(self.speed)

		if self.xcor() < -290:
			self.rt(60)
			self.setx(-290)

		elif self.xcor() > 290:
			self.rt(60)
			self.setx(290)

		if self.ycor() < -290:
			self.rt(60)
			self.sety(-290)

		elif self.ycor() > 290:
			self.rt(60)
			self.sety(290)

class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 0
		self.lives = 3
		self.shield = 100
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
		self.thrust = 1
		self.dx = 0
		self.dy = 0
		self.rotation_speed = 0

	def turn_left(self):
		self.rotation_speed = 30
		h = self.heading() + self.rotation_speed
		self.setheading(h)

	def turn_right(self):
		self.rotation_speed = -30
		h = self.heading() + self.rotation_speed
		self.setheading(h)

	def accelerate(self):
		h = self.heading()
		self.dx += math.cos(h*math.pi/180)*self.thrust
		self.dy += math.sin(h*math.pi/180)*self.thrust

	def decelerate(self):
		self.speed -= 1

	def hyperspace(self):
		os.system("afplay hyperspace.mp3&")
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		self.goto(x, y)
		self.speed *= 0.5

	def move(self):
		self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

		if self.xcor() < -290:
			self.dx = -self.dx

		elif self.xcor() > 290:
			self.dx = -self.dx

		if self.ycor() < -290:
			self.dy = -self.dy

		elif self.ycor() > 290:
			self.dy = -self.dy

		#Simulate gravity in the center
		#Not exactly correct due to angles being wrong
		# if self.xcor() > 0 and (self.ycor() > 0 or self.ycor()<0):
# 			self.dx -= game.gravity
# 		else:
# 			self.dx += game.gravity
#
# 		if self.ycor() > 0 and (self.ycor() > 0 or self.ycor()<0):
# 			self.dy -= game.gravity
# 		else:
# 			self.dy += game.gravity

class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 2
		self.setheading(random.randint(0,360))


	def move(self):
		self.fd(self.speed)

		if self.xcor() < -290:
			self.lt(60)
			self.setx(-290)

		elif self.xcor() > 290:
			self.lt(60)
			self.setx(290)

		if self.ycor() < -290:
			self.lt(60)
			self.sety(-290)

		elif self.ycor() > 290:
			self.lt(60)
			self.sety(290)

class EnemyBase(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 1
		self.setheading(random.randint(0,360))
		if self.xcor() < -290:
			self.rt(degrees)
			self.setx(-290)

		elif self.xcor() > 290:
			self.rt(degrees)
			self.setx(290)

		if self.ycor() < -290:
			self.rt(degrees)
			self.sety(-290)

		elif self.ycor() > 290:
			self.rt(degrees)
			self.sety(290)

class Ally(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 3
		self.setheading(random.randint(0,360))

	def move(self):
		self.fd(self.speed)

		degrees = random.randint(20, 60)

		if self.xcor() < -290:
			self.lt(degrees)
			self.setx(-290)

		elif self.xcor() > 290:
			self.lt(degrees)
			self.setx(290)

		if self.ycor() < -290:
			self.lt(degrees)
			self.sety(-290)

		elif self.ycor() > 290:
			self.lt(degrees)
			self.sety(290)

	def avoid(self, other):
		if (self.xcor() >= (other.xcor() -40)) and \
			(self.xcor() <= (other.xcor() + 40)) and \
			(self.ycor() >= (other.ycor() -40)) and \
			(self.ycor() <= (other.ycor() + 40)):
			self.lt(30)

class AllyBase(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 1
		self.setheading(random.randint(0,360))

	def move(self):
		self.fd(self.speed)

		degrees = random.randint(20, 60)

		if self.xcor() < -290:
			self.lt(degrees)
			self.setx(-290)

		elif self.xcor() > 290:
			self.lt(degrees)
			self.setx(290)

		if self.ycor() < -290:
			self.lt(degrees)
			self.sety(-290)

		elif self.ycor() > 290:
			self.lt(degrees)
			self.sety(290)

	def avoid(self, other):
		if (self.xcor() >= (other.xcor() -40)) and \
			(self.xcor() <= (other.xcor() + 40)) and \
			(self.ycor() >= (other.ycor() -40)) and \
			(self.ycor() <= (other.ycor() + 40)):
			self.lt(30)

class Bullet(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
		self.status = "ready"
		self.speed = 15

	def fire(self):
		if self.status == "ready":
			self.status = "shoot"

	def move(self):
		if self.status == "ready":
			self.hideturtle()
			#Move the turtle offscreen
			self.goto(-1000,1000)

		if self.status == "shoot":
			os.system("afplay laser.mp3&")
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.showturtle()
			self.status = "firing"
			#Get out of this if a bullet is shooting
			return True

		if self.status == "firing":
			self.fd(self.speed)


		#Border Check
		if self.xcor() < -290 or self.xcor() > 290 \
			or self.ycor() < -290 or self.ycor() > 290:
			self.status = "ready"

class EnemyBullet(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
		self.status = "ready"
		self.speed = 8
		self.heading_offset = 0

	def fire(self, startx, starty, heading):
		if self.status == "ready":
			self.status = "shoot"
			self.goto(startx, starty)
			#self.setheading(heading)
			#Get heading to Player
			px = player.xcor()
			py = player.xcor()
			heading = 0
			if player.xcor() > self.xcor() and player.ycor() > self.ycor():
				heading = random.randint(25, 65)
			elif player.xcor() < self.xcor() and player.ycor() > self.ycor():
				heading = random.randint(115, 155)
			if player.xcor() > self.xcor() and player.ycor() < self.ycor():
				heading = random.randint(195, 335)
			if player.xcor() < self.xcor() and player.ycor() < self.ycor():
				heading = random.randint(200, 245)

			self.setheading(heading)

	def move(self):
		if self.status == "ready":
			self.hideturtle()
			#Move the turtle offscreen
			self.goto(-1000,1000)


		if self.status == "shoot":
			os.system("afplay missile.mp3&")
			self.showturtle()
			self.status = "firing"

		if self.status == "firing":
			self.fd(self.speed)

		#Border Check
		if self.xcor() < -290 or self.xcor() > 290 \
			or self.ycor() < -290 or self.ycor() > 290:
			self.status = "ready"

class Particle(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, -1000, -1000)
		self.frame = 0
		self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)

	def explode(self, startx, starty):
		self.goto(startx, starty)
		self.setheading(random.randint(0, 360))
		self.frame = 1


	def move(self):
		if self.frame != 0:
			self.fd((20-self.frame)/2)
			self.frame += 1

			if self.frame < 6:
				self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
			elif self.frame < 11:
				self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
			else:
				self.shapesize(stretch_wid=0.05, stretch_len=0.05, outline=None)

			if self.frame > 18:
				self.frame = 0
				self.goto(-1000, -1000)

		#Border Check
		if self.xcor() < -290 or self.xcor() > 290 \
			or self.ycor() < -290 or self.ycor() > 290:
			self.frame = 0
			self.goto(-1000, -1000)

class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "splash"
		self.pen = turtle.Turtle()
		self.lives = 3
		self.gravity = 0.1

	def draw_border(self):
		#Draw Border
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.ht()
		self.pen.penup()

	def show_status(self):
		self.pen.undo()
		if game.lives > 0:
			msg = "Level: %s Lives: %s Score: %s" %(self.level, self.lives, self.score)
		else:
			msg = "Game Over Score: %s" %(self.score)
		self.pen.penup()
		self.pen.goto(-300, 310)
		self.pen.write(msg, font=("Arial", 16, "normal"))

	def fire_weapon(self):
		for bullet in bullets:
			if bullet.status == "ready":
				bullet.fire()
				break

	def show_splash(self):
		turtle.bgpic("splash-screen.gif")
		turtle.update()
		time.sleep(5)
		turtle.bgpic("starfield.gif")
		self.state = "setup"

	def set_state(self, state):
		states = ["splash", "setup", "playing", "restart", "gameover"]
		if state in states:
			self.state = state
		else:
			state = "splash"

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Show the level and score
game.show_status()

#Set up the game
#Create lists for sprites
#Add Enemies
if game.state == "splash":
	game.show_splash()

if game.state == "setup":
	#Create player and enemy objects
	player = Player("triangle", "white", 0, 0)
	#enemy = Enemy("circle", "red", 100.0, 0.0)
	#bullet = Bullet("triangle", "yellow", 0.0, 0.0)
	#ally = Ally("square", "blue", 100, 100)
	enemybase = EnemyBase("enemybase.gif", "orange", -200.0, -200.0)
	allybase = AllyBase("allybase.gif", "green", 200.0, 200.0)
	enemybullet = EnemyBullet("triangle", "red", 0.0, 0.0)

	enemies = []

	for e in range(game.level):
		enemies.append(Enemy("enemy.gif", "red", enemybase.xcor(), enemybase.ycor()))

	#Add Allies
	allies = []
	for a in range(game.level):
		allies.append(Ally("ally.gif", "blue", allybase.xcor(), allybase.ycor()))

	particles = []
	colors = ["red", "yellow", "orange"]
	for p in range(20):
		particles.append(Particle("circle", random.choice(colors), -1000, -1000))

	bullets = []
	for b in range(2):
		bullets.append(Bullet("triangle", "yellow", 0.0, 0.0))

	game.set_state("playing")

#Keyboard Bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.hyperspace, "Down")
turtle.onkey(game.fire_weapon, "space")
turtle.listen()

while True:
	turtle.update()
	if game.state == "restart":
		game.lives = 3
		game.score = 0
		player.speed = 0
		player.goto(0,0)
		player.setheading(0)
		player.dx = 0
		player.dy = 0

		enemybase.goto(-200, -200)
		allybase.goto(200,200)

		for enemy in enemies:
			enemy.goto(enemybase.xcor(), enemybase.ycor())
			enemy.speed = 1

		for ally in allies:
			ally.goto(allybase.xcor(), allybase.ycor())
			ally.speed = 1

		game.set_state("playing")

	if game.state == "playing":
		player.move()
		enemybase.move()
		allybase.move()
		enemybullet.move()

		#Check Collision for enemy bullet
		if player.is_collision(enemybullet):
			enemybullet.status = "ready"
			os.system("afplay explosion.mp3&")
			player.color("red")
			for particle in particles:
				particle.explode(player.xcor(), player.ycor())
			player.rt(random.randint(100, 200))
			game.lives -= 1
			if game.lives < 1:
				game.set_state("gameover")
			game.show_status()
			player.color("white")



		for bullet in bullets:
			bullet.move()

		for enemy in enemies:
			enemy.move()

			#Check collisions
			if player.is_collision(enemy):
				os.system("afplay explosion.mp3&")
				player.color("red")
				for particle in particles:
					particle.explode(enemy.xcor(), enemy.ycor())
				player.rt(random.randint(100, 200))
				enemy.goto(enemybase.xcor(), enemybase.ycor())
				enemy.speed += 1
				game.lives -= 1
				if game.lives < 1:
					game.set_state("gameover")
				game.show_status()
				player.color("white")

			for bullet in bullets:
				if bullet.is_collision(enemy):
					os.system("afplay explosion.mp3&")
					for particle in particles:
						particle.explode(enemy.xcor(), enemy.ycor())

					bullet.status = "ready"
					enemy.goto(enemybase.xcor(), enemybase.ycor())
					enemy.setheading(random.randint(0,360))
					enemy.speed += 0.2
					game.score += 100
					game.show_status()

			#Fire bullet at player
			if random.randint(1, 1000/game.level) == 1:
				if enemybullet.status == "ready":
					enemybullet.fire(enemy.xcor(), enemy.ycor(), enemy.heading())

		for ally in allies:
			ally.move()

			#Avoid enemy
			for enemy in enemies:
				ally.avoid(enemy)

			#Allies should avoid player as well
			ally.avoid(player)

			#Check collisions
			for bullet in bullets:
				if bullet.is_collision(ally):
					os.system("afplay explosion.mp3&")
					for particle in particles:
						particle.explode(ally.xcor(), ally.ycor())
					bullet.status = "ready"
					ally.goto(allybase.xcor(), allybase.ycor())
					ally.speed += 1
					game.score -= 50
					game.show_status()

	for particle in particles:
		particle.move()

	if game.state == "gameover":
		for i in range(360):
			player.rt(1)

		if tkMessageBox.askyesno("Game Over", "Play again?") == True:
			game.set_state("restart")
			game.level = 1
			game.score = 0
			game.show_status()

			for enemy in enemies:
				enemy.ht()
				enemy.clear()
				del enemy


			for ally in allies:
				ally.ht()
				ally.clear()
				del ally


			enemies=[]
			enemies.append(Enemy("enemy.gif", "red", enemybase.xcor(), enemybase.ycor()))
			allies = []
			allies.append(Ally("ally.gif", "blue", allybase.xcor(), allybase.ycor()))
		else:
			exit()

	if game.score / (game.level) > 500:
		game.level += 1
		enemies.append(Enemy("enemy.gif", "red", enemybase.xcor(), enemybase.ycor()))
		allies.append(Ally("ally.gif", "blue", allybase.xcor(), allybase.ycor()))

delay = raw_input("Press enter to finish. > ")
