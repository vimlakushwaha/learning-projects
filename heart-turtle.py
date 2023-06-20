#heart shap using turtle


import math
from turtle import*
def heart(k):
    return 15*math.sin(k)**3
def heart_v(k):
    return 10*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)
speed(60)
bgcolor("black")
for i in range(1500):
    goto(heart(i)*20,heart_v(i)*24)
    for j in range(2):
        color("#f73487")
    goto(0,0)
done()
