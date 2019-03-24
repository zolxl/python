#e2.13TargetPlate.py
from turtle import *
for i in range(25):
    if i == 0:
        seth(-90)
        penup()
        fd(1)
        pendown()
        seth(0)
    else:
        seth(-90)
        penup()
        fd(2*i-1)
        pendown()
        seth(0)
    circle(i**2+1)

