#Draw Python
import turtle
turtle.setup(0.6,400)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("violet")
turtle.seth(-90)
for i in range(3):
    turtle.circle(40,180)
    turtle.circle(-40,180)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
