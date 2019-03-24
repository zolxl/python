#等边三角形a2.4EquilateralTriangle.py a2.5SuperpositionTriangle.py
import turtle as t
t.setup(1000,1000,20,20)
t.penup()
t.fd(-200)
t.seth(-90)
t.fd(200)
t.seth(0)
t.pendown()
def DrawEquilateralTriangle(length,angle):
    t.fd(length)
    t.seth(angle)
    t.fd(length)
    t.seth(-angle)
    t.fd(length)
DrawEquilateralTriangle(400,120)

t.seth(60)
t.fd(200)
t.seth(0)
t.fd(200)
t.seth(240)
t.fd(200)
t.seth(120)
t.fd(200)

