import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
wn.bgpic("bobyum.gif")

turtle.register_shape("space_ship.gif")
turtle.register_shape("AAliane.gif")
turtle.register_shape("bulllet2.gif")
turtle.register_shape("alian_boss.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-280, 275)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

name = turtle.Turtle()
name.speed(0)
name.color("white")
name.penup()
name.setposition(-280, 260)
name.write("SPACE INVADERS! by Jack.R")
name.hideturtle()

player = turtle.Turtle()
player.color("red")
player.shape("space_ship.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

enemy = turtle.Turtle()

enemyspeed = 2

enemies = []

def setup_enemies(alien_gif, number_of_enemies):
    global enemies
    for enemy in enemies:
        enemy.hideturtle()
    enemies = []
    for i in range(number_of_enemies):
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("green")
        enemy.shape(alien_gif)
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint (100, 250)
        enemy.setposition(x, y)
    return enemies

enemies = setup_enemies("AAliane.gif", random.randint(4,7))

bullet = turtle.Turtle()
bullet.color("grey")
bullet.shape("bulllet2.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

bulletstate = "ready"
bullet_distance = 500

def move_left(_):
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = - 280
    player.setx(x)

def fire_bullet(_):
    global bulletstate
    global bullet_distance
    bullet_distance = 500
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollison(t1, t2) :
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor() ,2))
    global bullet_distance
    if distance < bullet_distance :
        bullet_distance = distance
    if distance < 15:
        return True
    else:
        return False

def move_right(_):
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

turtle.listen()
turtle.getcanvas().bind('<Left>', move_left)
turtle.getcanvas().bind('<Right>', move_right)
turtle.getcanvas().bind('<space>', fire_bullet)


while True:

    for enemy in enemies:

        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollison(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s" % (score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollison(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if score == 100 and enemies.__len__() > 1:
        enemies = setup_enemies("alian_boss.gif",1)