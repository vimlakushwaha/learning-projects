import turtle as tur
import colorsys as cs
tur.setup(1000,800)
tur.tracer(50)
tur.width(0.0071)
tur.bgcolor("black")
def squre(x,y):
    for i in range(1):
        tur.forward(x)
        tur.right(30)
        tur.forward(y)
        tur.left(10)

    tur.forward(x)
def circle1(x,y):
    for i in range(1):
        tur.forward(x)
        tur.right(90)
        tur.forward(y)
        tur.left(130)

    tur.forward(x)

for j in range(20):
    for i in range(50):
        tur.color(cs.hsv_to_rgb(i/10,1-j/20,1))
        tur.right(130)
        squre(200-j*4,50)
        tur.right(100)
        circle1(100,60)
        tur.circle(80,6)

tur.hideturtle()
tur.done()
