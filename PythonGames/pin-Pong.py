## same code but with classes

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=500)
wn.tracer(0)

class Objects(object):
    ## panels
    def __init__(self):
        self.panelOne = turtle.Turtle()
        self.panelTwo = turtle.Turtle()
        self.ball = turtle.Turtle()   
        
    def panel1Attributes(self):
        self.panelOne.color("white")
        self.panelOne.shape("square")
        self.panelOne.speed(0)
        self.panelOne.shapesize(stretch_len=1, stretch_wid=5)
        self.panelOne.penup()
        self.panelOne.goto(380,0)

    def panel2Attributes(self):
        self.panelTwo.color("white")
        self.panelTwo.shape("square")
        self.panelTwo.speed(0)
        self.panelTwo.penup()
        self.panelTwo.shapesize(stretch_len=1, stretch_wid=5)
        self.panelTwo.goto(-390,0)

    def ballAttribute(self):
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.speed(0)
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx = .2
        self.ball.dy = .2

    ## movement functions
    ## panel 1
    def panelOne_up(self):
        y = self.panelOne.ycor()
        y += 12

        self.panelOne.sety(y)
    
    def panelOne_down(self):
        y = self.panelOne.ycor()
        y -= 12

        self.panelOne.sety(y)

    ## panel 2
    def panelTwo_up(self):
        y = self.panelTwo.ycor()
        y += 12

        self.panelTwo.sety(y)
    
    def panelTwo_down(self):
        y = self.panelTwo.ycor()
        y -= 12

        self.panelTwo.sety(y)

    ## ball movement
    def ballMove(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
    ## check the border
    def check(self):
        if self.ball.ycor() > 250:
            self.ball.sety(250)
            self.ball.dy *= -1

        if self.ball.ycor() < -250:
            self.ball.sety(-250)
            self.ball.dy *= -1  

    ## collision xcor
    def collisionXCor(self):
        if self.ball.xcor() > 400 or self.ball.xcor() < -400:
            self.ball.goto(0,0)
            self.ball.dx *= 1

    ## ball and panel collision
    def collision(self):
        ## issue in the panel part
        if (self.ball.xcor() > 370 and self.ball.xcor() < 400) and (self.ball.ycor() < self.panelOne.ycor() + 160 and self.ball.ycor() > self.panelOne.ycor() - 160):
            self.ball.setx(370)
            self.ball.dx *= -1

        if (self.ball.xcor() < -380 and self.ball.xcor() > -400) and (self.ball.ycor() < self.panelTwo.ycor() + 160 and self.ball.ycor() > self.panelTwo.ycor() - 160):
            self.ball.setx(-380)
            self.ball.dx *= -1

rightPanel = Objects()
rightPanel.panel1Attributes()

leftPanel = Objects()
leftPanel.panel2Attributes()

pingBall = Objects()
pingBall.ballAttribute()

wn.listen()
wn.onkeypress(leftPanel.panelTwo_up, "w")
wn.onkeypress(leftPanel.panelTwo_down, "s")
wn.onkeypress(rightPanel.panelOne_up, "Up")
wn.onkeypress(rightPanel.panelOne_down, "Down")

while True:
    wn.update()

    ## ball movement
    pingBall.ballMove()
    
    ## check the border
    pingBall.check()
    pingBall.collisionXCor()
    
    ## ball and panel collision
    pingBall.collision()