# Import libraries
import threading
import time
import datetime
import random
import math
import turtle
import keyboard

# Timer
def countdown():
    global t, timeformat
    while t >= 0:
        timeLong = str(datetime.timedelta(seconds=t))
        timeformat = timeLong[3:]
        t -= 1
        time.sleep(1)

# Game function for running the game
def main_game_function():
    global t, timeformat
    # Initial score
    score_a = 0
    score_b = 0
    playera_name = "Player A"
    playerb_name = "Player B"

    # Pongerfall walls falling list
    pwxList = []

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

    # Pause the game
    def pause():
        global t
        ya = paddle_a.ycor()
        yb = paddle_b.ycor()
        tim = t
        t = 0
        pen2.write("Paused", align="center", font=("Ink Free", 70, "bold"))
        while True:
            if keyboard.is_pressed("shift"):
                win.update()
                paddle_a.sety(ya)
                paddle_b.sety(yb)
                t = tim
                threading.Thread(target=countdown).start()
                pen2.clear()
                break

    # Create window screen
    win = turtle.Screen()
    win.setup(width=800, height=600)
    win.tracer(0)
    win.title("Pongerfall")
    win.bgcolor("green")
    win.bgpic("title_background.png")

    # Pen 0
    pen0 = turtle.Turtle()
    pen0.speed(0)
    pen0.color("dark orange")
    pen0.penup()
    pen0.hideturtle()

    # Pen 1
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.color("black")
    pen1.penup()
    pen1.hideturtle()

    # Pen 2
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color("red")
    pen2.penup()
    pen2.hideturtle()

    # Pen 3
    pen3 = turtle.Turtle()
    pen3.speed(0)
    pen3.color("yellow")
    pen3.penup()
    pen3.hideturtle()

    # Pen 4
    pen4 = turtle.Turtle()
    pen4.speed(0)
    pen4.color("gold")
    pen4.penup()
    pen4.hideturtle()

    # Title screen balls
    ballMass = 1
    ball1 = turtle.Turtle()
    ball1.speed(0)
    ball1.shape("circle")
    ball1.color("magenta")
    ball1.penup()
    ball1.goto(random.randint(-375, 375), random.randint(-275, 275))
    ball1.dx = random.uniform(-0.65, 0.65)
    ball1.dy = random.uniform(-0.65, 0.65)
    ball2 = turtle.Turtle()
    ball2.speed(0)
    ball2.shape("circle")
    ball2.color("lime")
    ball2.penup()
    ball2.goto(random.randint(-375, 375), random.randint(-275, 275))
    ball2.dx = random.uniform(-0.65, 0.65)
    ball2.dy = random.uniform(-0.65, 0.65)
    ball3 = turtle.Turtle()
    ball3.speed(0)
    ball3.shape("circle")
    ball3.color("red")
    ball3.penup()
    ball3.goto(random.randint(-375, 375), random.randint(-275, 275))
    ball3.dx = random.uniform(-0.65, 0.65)
    ball3.dy = random.uniform(-0.65, 0.65)
    ball4 = turtle.Turtle()
    ball4.speed(0)
    ball4.shape("circle")
    ball4.color("blue")
    ball4.penup()
    ball4.goto(random.randint(-375, 375), random.randint(-275, 275))
    ball4.dx = random.uniform(-0.65, 0.65)
    ball4.dy = random.uniform(-0.65, 0.65)
    ball5 = turtle.Turtle()
    ball5.speed(0)
    ball5.shape("circle")
    ball5.color("purple")
    ball5.penup()
    ball5.goto(random.randint(-375, 375), random.randint(-275, 275))
    ball5.dx = random.uniform(-0.65, 0.65)
    ball5.dy = random.uniform(-0.65, 0.65)

    # Ball spawn overlapping check
    if ball2.xcor() - 17 < ball1.xcor() < ball2.xcor() + 17 or ball2.ycor() - 17 < ball1.ycor() < ball2.ycor() + 17:
        ball1.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball3.xcor() - 17 < ball1.xcor() < ball3.xcor() + 17 or ball3.ycor() - 17 < ball1.ycor() < ball3.ycor() + 17:
        ball1.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball4.xcor() - 17 < ball1.xcor() < ball4.xcor() + 17 or ball4.ycor() - 17 < ball1.ycor() < ball4.ycor() + 17:
        ball1.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball5.xcor() - 17 < ball1.xcor() < ball5.xcor() + 17 or ball5.ycor() - 17 < ball1.ycor() < ball5.ycor() + 17:
        ball1.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball3.xcor() - 17 < ball2.xcor() < ball3.xcor() + 17 or ball3.ycor() - 17 < ball2.ycor() < ball3.ycor() + 17:
        ball2.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball4.xcor() - 17 < ball2.xcor() < ball4.xcor() + 17 or ball4.ycor() - 17 < ball2.ycor() < ball4.ycor() + 17:
        ball2.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball5.xcor() - 17 < ball2.xcor() < ball5.xcor() + 17 or ball5.ycor() - 17 < ball2.ycor() < ball5.ycor() + 17:
        ball2.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball4.xcor() - 17 < ball3.xcor() < ball4.xcor() + 17 or ball4.ycor() - 17 < ball3.ycor() < ball4.ycor() + 17:
        ball3.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball5.xcor() - 17 < ball3.xcor() < ball5.xcor() + 17 or ball5.ycor() - 17 < ball3.ycor() < ball5.ycor() + 17:
        ball3.goto(random.randint(-375, 375), random.randint(-275, 275))
    if ball5.xcor() - 17 < ball4.xcor() < ball5.xcor() + 17 or ball5.ycor() - 17 < ball4.ycor() < ball5.ycor() + 17:
        ball4.goto(random.randint(-375, 375), random.randint(-275, 275))

    # Title screen
    pen0.goto(0, 50)
    pen0.write("Let's Play Pongerfall!", align="center", font=("Ink Free", 45, "bold"))
    pen1.goto(0, 0)
    pen1.write("Press the 'P' key to start", align="center", font=("Ink Free", 20, "bold"))
    pen1.goto(0, -50)
    pen1.write("Press the 'N' key to change the player names", align="center", font=("Ink Free", 15, "bold"))
    pen1.goto(0, -200)
    pen1.write("Player A (left orange paddle) uses the 'W' and 'S' keys to move", align="center", font=("Ink Free", 15, "bold"))
    pen1.goto(0, -240)
    pen1.write("Player B (right cyan paddle) uses the 'UP' and 'DOWN' arrow keys to move", align="center", font=("Ink Free", 15, "bold"))
    pen1.goto(0, -280)
    pen1.write("Click the 'SPACE BAR' at anytime to pause and click the 'SHIFT' key to unpause", align="center", font=("Ink Free", 15, "bold"))
    pen4.goto(220, 265)
    pen4.write("Player B Name: " + playerb_name, align="center", font=("Ink Free", 15, "bold"))
    pen4.goto(-220, 265)
    pen4.write("Player A Name: " + playera_name, align="center", font=("Ink Free", 15, "bold"))

    while True:
        # Move the balls
        win.update()
        ball1.setx(ball1.xcor() + ball1.dx)
        ball1.sety(ball1.ycor() + ball1.dy)
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)
        ball3.setx(ball3.xcor() + ball3.dx)
        ball3.sety(ball3.ycor() + ball3.dy)
        ball4.setx(ball4.xcor() + ball4.dx)
        ball4.sety(ball4.ycor() + ball4.dy)
        ball5.setx(ball5.xcor() + ball5.dx)
        ball5.sety(ball5.ycor() + ball5.dy)
        # Balls border checking
        if ball1.ycor() > 290:
            ball1.sety(290)
            ball1.dy *= -1
        if ball2.ycor() > 290:
            ball2.sety(290)
            ball2.dy *= -1
        if ball3.ycor() > 290:
            ball3.sety(290)
            ball3.dy *= -1
        if ball4.ycor() > 290:
            ball4.sety(290)
            ball4.dy *= -1
        if ball5.ycor() > 290:
            ball5.sety(290)
            ball5.dy *= -1
        if ball1.ycor() < -290:
            ball1.sety(-290)
            ball1.dy *= -1
        if ball2.ycor() < -290:
            ball2.sety(-290)
            ball2.dy *= -1
        if ball3.ycor() < -290:
            ball3.sety(-290)
            ball3.dy *= -1
        if ball4.ycor() < -290:
            ball4.sety(-290)
            ball4.dy *= -1
        if ball5.ycor() < -290:
            ball5.sety(-290)
            ball5.dy *= -1
        if ball1.xcor() > 390:
            ball1.setx(390)
            ball1.dx *= -1
        if ball2.xcor() > 390:
            ball2.setx(390)
            ball2.dx *= -1
        if ball3.xcor() > 390:
            ball3.setx(390)
            ball3.dx *= -1
        if ball4.xcor() > 390:
            ball4.setx(390)
            ball4.dx *= -1
        if ball5.xcor() > 390:
            ball5.setx(390)
            ball5.dx *= -1
        if ball1.xcor() < -390:
            ball1.setx(-390)
            ball1.dx *= -1
        if ball2.xcor() < -390:
            ball2.setx(-390)
            ball2.dx *= -1
        if ball3.xcor() < -390:
            ball3.setx(-390)
            ball3.dx *= -1
        if ball4.xcor() < -390:
            ball4.setx(-390)
            ball4.dx *= -1
        if ball5.xcor() < -390:
            ball5.setx(-390)
            ball5.dx *= -1
        # Title balls collisions
        if ball2.xcor() - 17 < ball1.xcor() < ball2.xcor() + 17 and ball2.ycor() - 17 < ball1.ycor() < ball2.ycor() + 17:
            x1 = 0
            y1 = 0
            ball1.setx(ball1.xcor())
            ball1.sety(ball1.ycor())
            ball2.setx(ball2.xcor())
            ball2.sety(ball2.ycor())
            dx = ball2.xcor() - ball1.xcor()
            dy = ball2.ycor() - ball1.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball1.dy * cosAngle) - (ball1.dx * sinAngle)
            vy2 = (ball2.dy * cosAngle) - (ball2.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball2.dx * cosAngle) + (ball2.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball1.dx * cosAngle) + (ball1.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball2.setx(ball1.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball2.sety(ball1.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball1.setx(ball1.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball1.sety(ball1.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball1.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball1.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball2.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball2.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball3.xcor() - 17 < ball1.xcor() < ball3.xcor() + 17 and ball3.ycor() - 17 < ball1.ycor() < ball3.ycor() + 17:
            x1 = 0
            y1 = 0
            ball1.setx(ball1.xcor())
            ball1.sety(ball1.ycor())
            ball3.setx(ball3.xcor())
            ball3.sety(ball3.ycor())
            dx = ball3.xcor() - ball1.xcor()
            dy = ball3.ycor() - ball1.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball1.dy * cosAngle) - (ball1.dx * sinAngle)
            vy2 = (ball3.dy * cosAngle) - (ball3.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball3.dx * cosAngle) + (ball3.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball1.dx * cosAngle) + (ball1.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball3.setx(ball1.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball3.sety(ball1.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball1.setx(ball1.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball1.sety(ball1.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball1.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball1.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball3.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball3.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball4.xcor() - 17 < ball1.xcor() < ball4.xcor() + 17 and ball4.ycor() - 17 < ball1.ycor() < ball4.ycor() + 17:
            x1 = 0
            y1 = 0
            ball1.setx(ball1.xcor())
            ball1.sety(ball1.ycor())
            ball4.setx(ball4.xcor())
            ball4.sety(ball4.ycor())
            dx = ball4.xcor() - ball1.xcor()
            dy = ball4.ycor() - ball1.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball1.dy * cosAngle) - (ball1.dx * sinAngle)
            vy2 = (ball4.dy * cosAngle) - (ball4.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball4.dx * cosAngle) + (ball4.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball1.dx * cosAngle) + (ball1.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball4.setx(ball1.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball4.sety(ball1.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball1.setx(ball1.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball1.sety(ball1.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball1.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball1.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball4.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball4.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball5.xcor() - 17 < ball1.xcor() < ball5.xcor() + 17 and ball5.ycor() - 17 < ball1.ycor() < ball5.ycor() + 17:
            x1 = 0
            y1 = 0
            ball1.setx(ball1.xcor())
            ball1.sety(ball1.ycor())
            ball5.setx(ball5.xcor())
            ball5.sety(ball5.ycor())
            dx = ball5.xcor() - ball1.xcor()
            dy = ball5.ycor() - ball1.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball1.dy * cosAngle) - (ball1.dx * sinAngle)
            vy2 = (ball5.dy * cosAngle) - (ball5.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball5.dx * cosAngle) + (ball5.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball1.dx * cosAngle) + (ball1.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball5.setx(ball1.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball5.sety(ball1.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball1.setx(ball1.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball1.sety(ball1.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball1.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball1.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball5.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball5.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball3.xcor() - 17 < ball2.xcor() < ball3.xcor() + 17 and ball3.ycor() - 17 < ball2.ycor() < ball3.ycor() + 17:
            x1 = 0
            y1 = 0
            ball2.setx(ball2.xcor())
            ball2.sety(ball2.ycor())
            ball3.setx(ball3.xcor())
            ball3.sety(ball3.ycor())
            dx = ball3.xcor() - ball2.xcor()
            dy = ball3.ycor() - ball2.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball2.dy * cosAngle) - (ball2.dx * sinAngle)
            vy2 = (ball3.dy * cosAngle) - (ball3.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball3.dx * cosAngle) + (ball3.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball2.dx * cosAngle) + (ball2.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball3.setx(ball2.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball3.sety(ball2.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball2.setx(ball2.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball2.sety(ball2.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball2.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball2.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball3.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball3.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball4.xcor() - 17 < ball2.xcor() < ball4.xcor() + 17 and ball4.ycor() - 17 < ball2.ycor() < ball4.ycor() + 17:
            x1 = 0
            y1 = 0
            ball2.setx(ball2.xcor())
            ball2.sety(ball2.ycor())
            ball4.setx(ball4.xcor())
            ball4.sety(ball4.ycor())
            dx = ball4.xcor() - ball2.xcor()
            dy = ball4.ycor() - ball2.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball2.dy * cosAngle) - (ball2.dx * sinAngle)
            vy2 = (ball4.dy * cosAngle) - (ball4.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball4.dx * cosAngle) + (ball4.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball2.dx * cosAngle) + (ball2.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball4.setx(ball2.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball4.sety(ball2.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball2.setx(ball2.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball2.sety(ball2.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball2.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball2.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball4.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball4.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball5.xcor() - 17 < ball2.xcor() < ball5.xcor() + 17 and ball5.ycor() - 17 < ball2.ycor() < ball5.ycor() + 17:
            x1 = 0
            y1 = 0
            ball2.setx(ball2.xcor())
            ball2.sety(ball2.ycor())
            ball5.setx(ball5.xcor())
            ball5.sety(ball5.ycor())
            dx = ball5.xcor() - ball2.xcor()
            dy = ball5.ycor() - ball2.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball2.dy * cosAngle) - (ball2.dx * sinAngle)
            vy2 = (ball5.dy * cosAngle) - (ball5.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball5.dx * cosAngle) + (ball5.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball2.dx * cosAngle) + (ball2.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball5.setx(ball2.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball5.sety(ball2.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball2.setx(ball2.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball2.sety(ball2.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball2.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball2.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball5.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball5.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball4.xcor() - 17 < ball3.xcor() < ball4.xcor() + 17 and ball4.ycor() - 17 < ball3.ycor() < ball4.ycor() + 17:
            x1 = 0
            y1 = 0
            ball3.setx(ball3.xcor())
            ball3.sety(ball3.ycor())
            ball4.setx(ball4.xcor())
            ball4.sety(ball4.ycor())
            dx = ball4.xcor() - ball3.xcor()
            dy = ball4.ycor() - ball3.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball3.dy * cosAngle) - (ball3.dx * sinAngle)
            vy2 = (ball4.dy * cosAngle) - (ball4.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball4.dx * cosAngle) + (ball4.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball3.dx * cosAngle) + (ball3.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball4.setx(ball3.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball4.sety(ball3.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball3.setx(ball3.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball3.sety(ball3.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball3.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball3.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball4.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball4.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball5.xcor() - 17 < ball3.xcor() < ball5.xcor() + 17 and ball5.ycor() - 17 < ball3.ycor() < ball5.ycor() + 17:
            x1 = 0
            y1 = 0
            ball3.setx(ball3.xcor())
            ball3.sety(ball3.ycor())
            ball5.setx(ball5.xcor())
            ball5.sety(ball5.ycor())
            dx = ball5.xcor() - ball3.xcor()
            dy = ball5.ycor() - ball3.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball3.dy * cosAngle) - (ball3.dx * sinAngle)
            vy2 = (ball5.dy * cosAngle) - (ball5.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball5.dx * cosAngle) + (ball5.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball3.dx * cosAngle) + (ball3.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball5.setx(ball3.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball5.sety(ball3.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball3.setx(ball3.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball3.sety(ball3.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball3.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball3.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball5.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball5.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        if ball5.xcor() - 17 < ball4.xcor() < ball5.xcor() + 17 and ball5.ycor() - 17 < ball4.ycor() < ball5.ycor() + 17:
            x1 = 0
            y1 = 0
            ball4.setx(ball4.xcor())
            ball4.sety(ball4.ycor())
            ball5.setx(ball5.xcor())
            ball5.sety(ball5.ycor())
            dx = ball5.xcor() - ball4.xcor()
            dy = ball5.ycor() - ball4.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball4.dy * cosAngle) - (ball4.dx * sinAngle)
            vy2 = (ball5.dy * cosAngle) - (ball5.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball5.dx * cosAngle) + (ball5.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball4.dx * cosAngle) + (ball4.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball5.setx(ball4.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball5.sety(ball4.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball4.setx(ball4.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball4.sety(ball4.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball4.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball4.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball5.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball5.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        # User name input
        if keyboard.is_pressed("n"):
            playera_name = win.textinput("Pongerfall", "Enter Player A's name (12 characters or less)")
            playerb_name = win.textinput("Pongerfall", "Enter Player B's name (12 characters or less)")
            if len(playera_name) > 12:
                playera_name = "TOO LONG!"
            if len(playerb_name) > 12:
                playerb_name = "TOO LONG!"
            pen4.clear()
            pen4.goto(220, 265)
            pen4.write("Player B Name: " + playerb_name, align="center", font=("Ink Free", 15, "bold"))
            pen4.goto(-220, 265)
            pen4.write("Player A Name: " + playera_name, align="center", font=("Ink Free", 15, "bold"))
        # Start of the game
        if keyboard.is_pressed("p"):
            # Clears the screen
            pen0.clear()
            pen1.clear()
            pen4.clear()
            ball1.hideturtle()
            ball2.hideturtle()
            ball3.hideturtle()
            ball4.hideturtle()
            ball5.hideturtle()
            win.bgpic("game_background.png")
            win.update()
            break

    # Player score
    pen3.goto(0, 260)
    pen3.write("{}: 0    Timer: 7:00    {}: 0".format(playera_name, playerb_name), align="center", font=("Ink Free", 20, "bold"))

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("cyan")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("orange")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Pongerfall wall
    wall0 = turtle.Turtle()
    wall0.speed(0)
    wall0.shape("square")
    wall0.color("light blue")
    wall0.penup()
    wall0StretchWidth = random.randint(4, 10)
    wall0.shapesize(stretch_wid=wall0StretchWidth, stretch_len=1)
    wall0Stretch = wall0StretchWidth * 10
    pwxList.append(random.randint(50, 200))
    pwxList.append(random.randint(-200, -50))
    wall0.goto(random.choice(pwxList), random.randint(410, 700))
    wall0.dy = random.uniform(0.2, 0.5)

    # Game ball for phase 1
    ballxSlopValue = [0.3, -0.3]
    ballySlopValue = [0.3, -0.3]
    ball0 = turtle.Turtle()
    ball0.speed(0)
    ball0.shape("circle")
    ball0.color("purple")
    ball0.penup()
    ball0.goto(0, 0)
    ball0.dx = random.choice(ballxSlopValue)
    ball0.dy = random.choice(ballySlopValue)

    # Count down to start phase 1
    pen2.goto(0, -60)
    pen2.write("Phase 1", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(3)
    pen2.clear()
    pen2.write("3", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("2", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("1", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("GO!", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(0.5)
    pen2.clear()

    # Keyboard bindings
    win.onkeypress(paddle_a_up, "w")
    win.onkeypress(paddle_a_down, "s")
    win.onkeypress(paddle_b_up, "Up")
    win.onkeypress(paddle_b_down, "Down")
    win.onkeypress(pause, "space")
    win.listen()
    threading.Thread(target=countdown).start()

    # Main phase 1 game loop
    while (score_a < 5) and (score_b < 5) and (t > 0):
        # Move the ball and update timer/score
        win.update()
        pen3.clear()
        pen3.write("{}: {}    Timer: {}    {}: {}".format(playera_name, score_a, timeformat, playerb_name, score_b), align="center", font=("Ink Free", 20, "bold"))
        ball0.setx(ball0.xcor() + ball0.dx)
        ball0.sety(ball0.ycor() + ball0.dy)
        # Move pongerfall wall
        wall0.sety(wall0.ycor() - wall0.dy)
        # Ball border checking
        if ball0.ycor() > 290:
            ball0.sety(290)
            ball0.dy *= -1
        if ball0.ycor() < -290:
            ball0.sety(-290)
            ball0.dy *= -1
        if ball0.xcor() > 390:
            ball0.goto(0, 0)
            ball0.dx *= -1
            score_a += 1
        if ball0.xcor() < -390:
            ball0.goto(0, 0)
            ball0.dx *= -1
            score_b += 1
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
        if (330 < ball0.xcor() < 350) and (paddle_b.ycor() + 50 > ball0.ycor() > paddle_b.ycor() - 50):
            ball0.setx(330)
            ball0.dx *= -1
        if (-330 > ball0.xcor() > -350) and (paddle_a.ycor() + 50 > ball0.ycor() > paddle_a.ycor() - 50):
            ball0.setx(-330)
            ball0.dx *= -1
        # Pongerfall wall and ball collision
        if (wall0.xcor() - 20 < ball0.xcor() < wall0.xcor()) and (wall0.ycor() + wall0Stretch > ball0.ycor() > wall0.ycor() - wall0Stretch):
            ball0.setx(wall0.xcor() - 20)
            ball0.dx *= -1
        if (wall0.xcor() < ball0.xcor() < wall0.xcor() + 20) and (wall0.ycor() + wall0Stretch > ball0.ycor() > wall0.ycor() - wall0Stretch):
            ball0.setx(wall0.xcor() + 20)
            ball0.dx *= -1
        # Resetting pongerfall wall
        if wall0.ycor() < -410:
            pwxList.clear()
            wall0StretchWidth = random.randint(4, 10)
            wall0.shapesize(stretch_wid=wall0StretchWidth, stretch_len=1)
            wall0Stretch = wall0StretchWidth * 10
            pwxList.append(random.randint(50, 200))
            pwxList.append(random.randint(-200, -50))
            wall0.goto(random.choice(pwxList), random.randint(410, 700))
            wall0.dy = random.uniform(0.2, 0.5)

    # Disappear all turtles
    wall0.hideturtle()
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    ball0.hideturtle()
    win.update()

    # Reset score board
    pen3.clear()
    pen3.write("{}: {}               {}: {}".format(playera_name, score_a, playerb_name, score_b), align="center", font=("Ink Free", 20, "bold"))

    # Reset paddles
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)

    # Reset pongerfall wall
    pwxList.clear()
    wall0StretchWidth = random.randint(4, 10)
    wall0.shapesize(stretch_wid=wall0StretchWidth, stretch_len=1)
    wall0Stretch = wall0StretchWidth * 10
    pwxList.append(random.randint(50, 200))
    pwxList.append(random.randint(-200, -50))
    wall0.goto(random.choice(pwxList), random.randint(410, 700))
    wall0.dy = random.uniform(0.2, 0.5)

    # Game balls for phase 2
    ballxSlopValue = [0.3, -0.3]
    ballySlopValue = [0.3, -0.3]
    ball0.goto(0, 15)
    ball0.dx = random.choice(ballxSlopValue)
    ball0.dy = random.choice(ballySlopValue)
    ballxSlopValue.remove(ball0.dx)
    ballySlopValue.remove(ball0.dy)
    ball6 = turtle.Turtle()
    ball6.speed(0)
    ball6.shape("circle")
    ball6.color("purple")
    ball6.penup()
    ball6.goto(0, -15)
    ball6.dx = ballxSlopValue[0]
    ball6.dy = ballySlopValue[0]

    # Count down to start phase 2
    pen2.write("Phase 2", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(3)
    pen2.clear()
    pen2.write("3", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("2", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("1", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(1)
    pen2.clear()
    pen2.write("GO!", align="center", font=("Ink Free", 70, "bold"))
    time.sleep(0.5)
    pen2.clear()
    wall0.showturtle()
    paddle_a.showturtle()
    paddle_b.showturtle()
    ball0.showturtle()

    # Main phase 2 game loop
    while (score_a >= 5) or (score_b >= 5) or (t <= 0):
        # Move the ball and update timer/score
        win.update()
        pen3.clear()
        pen3.write("{}: {}               {}: {}".format(playera_name, score_a, playerb_name, score_b), align="center", font=("Ink Free", 20, "bold"))
        ball0.setx(ball0.xcor() + ball0.dx)
        ball0.sety(ball0.ycor() + ball0.dy)
        ball6.setx(ball6.xcor() + ball6.dx)
        ball6.sety(ball6.ycor() + ball6.dy)
        # Move pongerfall wall
        wall0.sety(wall0.ycor() - wall0.dy)
        # Ball border checking
        if ball0.ycor() > 290:
            ball0.sety(290)
            ball0.dy *= -1
        if ball0.ycor() < -290:
            ball0.sety(-290)
            ball0.dy *= -1
        if ball6.ycor() > 290:
            ball6.sety(290)
            ball6.dy *= -1
        if ball6.ycor() < -290:
            ball6.sety(-290)
            ball6.dy *= -1
        if ball0.xcor() > 390:
            ball0.goto(0, 15)
            ball0.dx *= -1
            score_a += 1
        if ball0.xcor() < -390:
            ball0.goto(0, 15)
            ball0.dx *= -1
            score_b += 1
        if ball6.xcor() > 390:
            ball6.goto(0, -15)
            ball6.dx *= -1
            score_a += 1
        if ball6.xcor() < -390:
            ball6.goto(0, -15)
            ball6.dx *= -1
            score_b += 1
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
        if (330 < ball0.xcor() < 350) and (paddle_b.ycor() + 50 > ball0.ycor() > paddle_b.ycor() - 50):
            ball0.setx(330)
            ball0.dx *= -1
        if (-330 > ball0.xcor() > -350) and (paddle_a.ycor() + 50 > ball0.ycor() > paddle_a.ycor() - 50):
            ball0.setx(-330)
            ball0.dx *= -1
        if (330 < ball6.xcor() < 350) and (paddle_b.ycor() + 50 > ball6.ycor() > paddle_b.ycor() - 50):
            ball6.setx(330)
            ball6.dx *= -1
        if (-330 > ball6.xcor() > -350) and (paddle_a.ycor() + 50 > ball6.ycor() > paddle_a.ycor() - 50):
            ball6.setx(-330)
            ball6.dx *= -1
        # Pongerfall wall and ball collision
        if (wall0.xcor() - 20 < ball0.xcor() < wall0.xcor()) and (wall0.ycor() + wall0Stretch > ball0.ycor() > wall0.ycor() - wall0Stretch):
            ball0.setx(wall0.xcor() - 20)
            ball0.dx *= -1
        if (wall0.xcor() < ball0.xcor() < wall0.xcor() + 20) and (wall0.ycor() + wall0Stretch > ball0.ycor() > wall0.ycor() - wall0Stretch):
            ball0.setx(wall0.xcor() + 20)
            ball0.dx *= -1
        if (wall0.xcor() - 20 < ball6.xcor() < wall0.xcor()) and (wall0.ycor() + wall0Stretch > ball6.ycor() > wall0.ycor() - wall0Stretch):
            ball6.setx(wall0.xcor() - 20)
            ball6.dx *= -1
        if (wall0.xcor() < ball6.xcor() < wall0.xcor() + 20) and (wall0.ycor() + wall0Stretch > ball6.ycor() > wall0.ycor() - wall0Stretch):
            ball6.setx(wall0.xcor() + 20)
            ball6.dx *= -1
        # Game balls collision
        if ball6.xcor() - 17 < ball0.xcor() < ball6.xcor() + 17 and ball6.ycor() - 17 < ball0.ycor() < ball6.ycor() + 17:
            x1 = 0
            y1 = 0
            ball0.setx(ball0.xcor())
            ball0.sety(ball0.ycor())
            ball6.setx(ball6.xcor())
            ball6.sety(ball6.ycor())
            dx = ball6.xcor() - ball0.xcor()
            dy = ball6.ycor() - ball0.ycor()
            sinAngle = math.sin(math.atan2(dy, dx))
            cosAngle = math.cos(math.atan2(dy, dx))
            x2 = (dx * cosAngle) + (dy * sinAngle)
            y2 = (dy * cosAngle) - (dx * sinAngle)
            vy1 = (ball0.dy * cosAngle) - (ball0.dx * sinAngle)
            vy2 = (ball6.dy * cosAngle) - (ball6.dx * sinAngle)
            vx1Final = (2 * ballMass * ((ball6.dx * cosAngle) + (ball6.dy * sinAngle))) / (ballMass + ballMass)
            vx2Final = (2 * ballMass * ((ball0.dx * cosAngle) + (ball0.dy * sinAngle))) / (ballMass + ballMass)
            x1 += vx1Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            x2 += vx2Final / ((abs(vx1Final) + abs(vx2Final)) * (40 - abs(math.sqrt((dx ** 2) + (dy ** 2)))))
            ball6.setx(ball0.xcor() + ((x2 * cosAngle) - (y2 * sinAngle)))
            ball6.sety(ball0.ycor() + ((y2 * cosAngle) + (x2 * sinAngle)))
            ball0.setx(ball0.xcor() + ((x1 * cosAngle) - (y1 * sinAngle)))
            ball0.sety(ball0.ycor() + ((y1 * cosAngle) + (x1 * sinAngle)))
            ball0.dx = (vx1Final * cosAngle) - (vy1 * sinAngle)
            ball0.dy = (vy1 * cosAngle) + (vx1Final * sinAngle)
            ball6.dx = (vx2Final * cosAngle) - (vy2 * sinAngle)
            ball6.dy = (vy2 * cosAngle) + (vx2Final * sinAngle)
        # Resetting pongerfall wall
        if wall0.ycor() < -410:
            pwxList.clear()
            wall0StretchWidth = random.randint(4, 10)
            wall0.shapesize(stretch_wid=wall0StretchWidth, stretch_len=1)
            wall0Stretch = wall0StretchWidth * 10
            pwxList.append(random.randint(50, 200))
            pwxList.append(random.randint(-200, -50))
            wall0.goto(random.choice(pwxList), random.randint(410, 700))
            wall0.dy = random.uniform(0.2, 0.5)


# Thread to run all functions at once
t = 420
timeformat = 0
threading.Thread(target=main_game_function).start()
