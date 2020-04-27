
import tkinter as tk
import turtle
import tkinter.messagebox

HEIGHT = 700
WIDTH = 800


window = tk.Tk()
window.configure(background='blue')

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()


background_image = tk.PhotoImage(file= r"pictures/pong_start.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg='gray13', bd=5)
frame.place(relx=0.51, rely=0.75, relwidth=0.45, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Start Game", font=40, command= lambda: start_game(entry.get()))
button.pack()


window.mainloop()


wn = turtle.Screen()
wn.title("Pong by Nathan Dupree" + " Credit to @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width = 800, height=600)
wn.tracer(0)


score_1 = 0
score_2 = 0

#Player 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("blue")
paddle_1.shapesize(stretch_wid=5, stretch_len=0.2)
paddle_1.penup()
paddle_1.goto(-385, 0)

#Player 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("red")
paddle_2.shapesize(stretch_wid=5, stretch_len=0.2)
paddle_2.penup()
paddle_2.goto(385, 0)

#Table Line
line = turtle.Turtle()
line.color("white")
line.left(90)
line.right(180)
line.fd(500)

line_2 = turtle.Turtle()
line_2.color("white")
line_2.left(180)
line_2.right(90)
line_2.fd(500)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


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
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))



    #Paddle meets ball
    if (ball.xcor() > 349 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -349 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1



