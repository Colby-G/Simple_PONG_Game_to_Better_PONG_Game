# Import libraries
import turtle
import keyboard

# Functions for moving paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Create window screen
win = turtle.Screen()
win.title("Pong: The Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

# Score
score_a = 0
score_b = 0

while True:
    # Title screen
    pen.goto(0, 0)
    pen.write("Let's play PONG!", align="center", font=("Courier", 20, "normal"))
    pen.goto(0, -40)
    pen.write("Press the ENTER key to start!", align="center", font=("Courier", 15, "normal"))
    if keyboard.is_pressed("Return"):
        break


# Clears and resets the window screen
win.clear()
win.title("Pong: The Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.18
ball.dy = -0.18

# Player Score
pen.goto(0, 260)
pen.write("Player A: 0     Player B: 0", align="center", font=("Courier", 18, "normal"))

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Ball border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
    # Paddle border checking
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)
    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
