import turtle
ball = turtle.Turtle()
###print(ball)
##ball.forward(100)
##ball.left(45)
##ball.pensize(5)
##ball.color("dark salmon")
##ball.forward(50)
##ball.right(90)
##ball.penup()
##ball.forward(100)
##ball.right(135)
##ball.pensize(10)
##ball.color("light green")
##ball.pendown()
##ball.forward(200)
##ball.shape("circle")
##turtle.done()
##
gravity  =  -0.05
velocity = 0
ball.penup()
ball.color("green")
ball.shape("circle")
while True:
    ball.sety(ball.ycor()+velocity)
    velocity += gravity
