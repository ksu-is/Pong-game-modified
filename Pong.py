

import turtle

wn = turtle.Screen()
wn.title("Pong by Nathan Dupree" + " Credit to @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)


#Player 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#Player 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1


#Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

#bindings
wn.listen()
wn.onkeypress(paddle_1_up, "w")

wn.listen()
wn.onkeypress(paddle_1_down, "s")

wn.listen()
wn.onkeypress(paddle_2_up, "Up")

wn.listen()
wn.onkeypress(paddle_2_down, "Down")

#Main

while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1



    #Paddle meets ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

