import turtle
import time

wn = turtle.Screen()
wn.title("flappy Taha")
wn.bgcolor("blue")
wn.setup(width=500, height=800)
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.goto(-200, 0)
player.dx = 0
player.dy = 1

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 300)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -200)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0

gravity = -0.3

def go_up():
    player.dy += 8

    if player.dy > 8:
        player.dy = 8

wn.listen()
wn.onkeypress(go_up, "space")

player.score = 0

while True:
    time.sleep(0.02)
    wn.update()
    player.dy += gravity
    y = player.ycor()
    y += player.dy
    player.sety(y)
    if player.ycor() < -390:
        player.dy = 0
        player.sety(-390)
    x = pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x)
    x = pipe1_bottom.xcor()
    x += pipe1_bottom.dx
    pipe1_bottom.setx(x)
    if pipe1_top.xcor() < -350:
        pipe1_top.setx(350)
        pipe1_bottom.setx(350)
        pipe1_top.value = 1
    x = pipe2_top.xcor()
    x += pipe2_top.dx
    pipe2_top.setx(x)
    x = pipe2_bottom.xcor()
    x += pipe2_bottom.dx
    pipe2_bottom.setx(x)
    if pipe2_top.xcor() < -350:
        pipe2_top.setx(350)
        pipe2_bottom.setx(350)
        pipe2_top.value = 1
    if (player.xcor() + 10 > pipe1_top.xcor() - 30) and (player.xcor() - 10 < pipe1_top.xcor() + 30):
        if (player.ycor() + 10 > pipe1_top.ycor() - 180) or (player.ycor() - 10 < pipe1_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
            wn.update()
            time.sleep(3)
            player.score = 0
            pipe1_top.setx(300)
            pipe1_bottom.setx(300)
            pipe1_top.setx(600)
            pipe1_bottom.setx(600)
            player.goto(-200, 0)
            player.dy = 0
    if pipe1_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe1_top.value
        pipe1_top.value = 0
        pen.clear()
        pen.write(player.score, move=False, align="center", font=("Arial", 32, "normal"))
    if (player.xcor() + 10 > pipe2_top.xcor() - 30) and (player.xcor() - 10 < pipe2_top.xcor() + 30):
        if (player.ycor() + 10 > pipe2_top.ycor() - 180) or (player.ycor() - 30 < pipe2_bottom.ycor() + 180):
            pen.clear()
            pen.write("Game Over", move=False, align="left", font=("Arial", 16, "normal"))
            wn.update()
            time.sleep(3)
            player.score = 0
            pipe2_top.setx(300)
            pipe2_bottom.setx(300)
            pipe2_top.setx(600)
            pipe2_bottom.setx(600)
            player.goto(-200, 0)
            player.dy = 0
            pen.clear()
    if pipe2_top.xcor() + 30 < player.xcor() - 10:
        player.score += pipe2_top.value
        pipe2_top.value = 0
        pen.clear()
        pen.write(player.score, move=False, align="left", font=("Arial", 32, "normal"))
wn.mainloop()
