import turtle
import os
import math
import random
import winsound

#Arrumando a tela
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("background.gif")

#register shapes
turtle.register_shape("player1.gif")
turtle.register_shape("lazer.gif")
turtle.register_shape("invader.gif")


#desenhar bordas
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-270,-270)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(540)
	border_pen.lt(90)
border_pen.hideturtle()	

#Definir score
score = 0

#desenhar score na tela
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-255,250)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",12,"normal"))
score_pen.hideturtle()


#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player1.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15



#Escolher numero de inimigos
number_of_enemies = 5
#Criar uma lista vazia
enemies = []

#add inimigos na lista
for i in range(number_of_enemies):
	#Criar o inimigo
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100,250)
	enemy.setposition(x, y)

enemyspeed = 2


#Criar arma
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("lazer.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#Definir estado da bullet
#ready - readry to fire
#fire - bullets is firing
bulletstate = "ready"

#Mover o player pela esquerda e direita
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -255:
		x = -255
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 255:
		x = 255
	player.setx(x)

def fire_bullet():
	#Declarar bala como global 
	global bulletstate
	if bulletstate == "ready":
		winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
		bulletstate = "fire"
		#mover bala logo acima do player
		x = player.xcor()
		y = player.ycor() +10
		bullet.setposition(x,y)
		bullet.showturtle()

def isCollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False

#Criar keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


#Main game loop
while True:

	for enemy in enemies:
		#Mover inimigos
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Mover inimigos frente e pra tras
		if enemy.xcor() > 255:
			#Move todos inimigos para baixo
			for e in enemies:
				y = e.ycor()
				y -= 30	
				e.sety(y)
			#muda direção
			enemyspeed *= -1
		if enemy.xcor() < -255:
			#Move todos inimigos para baixo
			for e in enemies:
				y = e.ycor()
				y -= 30	
				e.sety(y)
			#muda direção
			enemyspeed *= -1
		#chcar a colisao da bala e o inimigo
		if isCollision(bullet, enemy):	
			winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
			#Resetar bala
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#resetar inimigo
			x = random.randint(-200, 200)
			y = random.randint(100,250)
			enemy.setposition(x, y)
			#update score
			score += 10
			score_pen.clear()
			scorestring = "Score: %s" %score
			score_pen.write(scorestring, False, align="left", font=("Arial",12,"normal"))


		if isCollision(player,enemy):
			winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
			winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break	

	#mvoer a bala
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#checar se bala atingiu borda
	if bullet.ycor() > 257:
		bullet.hideturtle()
		bulletstate = "ready"




