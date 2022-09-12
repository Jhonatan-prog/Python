import turtle

wn = turtle.Screen()

wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=500)
wn.tracer(0)

## Score
scoreA = 0
scoreB = 0

## left wall
wallOne = turtle.Turtle()
wallOne.speed(0)
wallOne.shape("square")
wallOne.shapesize(stretch_len=1, stretch_wid=5)

wallOne.color("white")
wallOne.penup()
wallOne.goto(-390, 0)

## rigth wall
wallTwo = turtle.Turtle()
wallTwo.speed(0)
wallTwo.shape("square")

wallTwo.shapesize(stretch_len=1, stretch_wid=5)
wallTwo.color("white")
wallTwo.penup()
wallTwo.goto(380, 0)


## ball
chooseRandom = [.2,.3,.4,1]

ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

## pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)

## functions of movement
## wall 1
def wallOne_go_up():
    y = wallOne.ycor()
    y += 12

    wallOne.sety(y)

def wallOne_go_down():
    y = wallOne.ycor()
    y -= 12

    wallOne.sety(y)

## wall 2
def wallTwo_go_up():
    y = wallTwo.ycor()
    y += 12

    wallTwo.sety(y)

def wallTwo_go_down():
    y = wallTwo.ycor()
    y -= 12

    wallTwo.sety(y)

## ball movement


wn.listen()
wn.onkeypress(wallOne_go_up, "w")
wn.onkeypress(wallOne_go_down, "s")
wn.onkeypress(wallTwo_go_up, "Up")
wn.onkeypress(wallTwo_go_down, "Down")

## Game devoloment
while True:
    wn.update()

    ## move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    ## border checking
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1

    if ball.ycor() < -250:
        ball.sety(-250)
        ball.dy *= -1
    
    ## counter
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= 1
        scoreA += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(scoreA, scoreB), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= 1
        scoreB += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(scoreA, scoreB), align="center", font=("courier", 24, "normal"))

    ## wall and ball collision
    if (ball.xcor() > 370 and ball.xcor() < 400) and (ball.ycor() < wallTwo.ycor() + 50 and ball.ycor() > wallTwo.ycor() -50):
        ball.setx(370)
        ball.dx *= -1

    if (ball.xcor() < -370 and ball.xcor() > -400) and (ball.ycor() < wallOne.ycor() + 50 and ball.ycor() > wallOne.ycor() -50):
        ball.setx(-370)
        ball.dx *= -1