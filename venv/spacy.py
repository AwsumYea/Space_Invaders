import turtle
import os

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

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

player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15

enemy = turtle.Turtle()
enemy.color("green")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

bullet = turtle.Turtle()
bullet.color("grey")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

def move_left(_):
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = - 280
    player.setx(x)

def fire_bullet(_):
    global  bulletstate
    x = player.xcor()
    y = player.ycor()
    bullet.setposition(x, y +10)
    bullet.showturtle()




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

    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)


    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y  )






turtle.mainloop()






delay = input("Press enter to exit")