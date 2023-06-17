#heart shap using turtle


import math
from turtle import*
def heart(k):
    return 10*math.sin(k)**3
def heart_v(k):
    return 6*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)
speed(1000)
bgcolor("black")
for i in range(15):
    goto(heart(i)*20,heart_v(i)*20)
    for j in range(5):
        color("#f73487")
    goto(0,0)
done()
